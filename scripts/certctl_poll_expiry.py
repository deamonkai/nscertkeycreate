#!/usr/bin/env python3
"""
certctl_poll_expiry.py

Poll NetScaler Console for certificate expiry data and generate a report.

Goals:
- Centralized polling via NetScaler Console
- Identify expired certs and certs expiring within N days
- Output human report + optional JSON artifact (for change management)

Auth model:
- POST /nitro/v2/config/login -> returns sessionid like "##ABC..."
- Use Cookie: NITRO_AUTH_TOKEN=<sessionid> for subsequent requests

This script is intentionally read-only.
"""

import argparse
import datetime as dt
import getpass
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import requests


# -----------------------------
# Data model
# -----------------------------

@dataclass
class CertRecord:
    name: str
    subject: str
    issuer: str
    not_after: Optional[dt.datetime]
    days_remaining: Optional[int]
    raw: Dict[str, Any]


# -----------------------------
# Helpers
# -----------------------------

def _now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _parse_console_datetime(s: str) -> Optional[dt.datetime]:
    """
    Console may return dates in a few formats depending on endpoint/resource.

    We attempt:
      - "YYYY-MM-DD HH:MM:SS"
      - "YYYY-MM-DDTHH:MM:SSZ"
      - "YYYY-MM-DDTHH:MM:SS+00:00"
    """
    if not s or not isinstance(s, str):
        return None

    candidates = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S%z",
    ]

    for fmt in candidates:
        try:
            parsed = dt.datetime.strptime(s, fmt)
            # If no tzinfo, assume UTC
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except Exception:
            continue

    return None


def _days_remaining(not_after: Optional[dt.datetime]) -> Optional[int]:
    if not_after is None:
        return None
    delta = not_after - _now_utc()
    return int(delta.total_seconds() // 86400)


def _print_table(rows: List[CertRecord], window_days: int) -> None:
    if not rows:
        print("[report] No certificates returned by API.")
        return

    print("")
    print("Certificate Expiry Report")
    print("=========================")
    print(f"Generated: {_now_utc().isoformat()}")
    print(f"Window:    {window_days} days")
    print("")

    # sort: expired first, then soonest expiry
    def sort_key(r: CertRecord):
        # None expiry goes last
        if r.not_after is None:
            return (2, dt.datetime.max.replace(tzinfo=dt.timezone.utc))
        if r.days_remaining is not None and r.days_remaining < 0:
            return (0, r.not_after)
        return (1, r.not_after)

    rows_sorted = sorted(rows, key=sort_key)

    # header
    print(f"{'Status':10} {'Days':>5} {'Expires (UTC)':20}  {'Name':35}  Subject")
    print("-" * 120)

    for r in rows_sorted:
        if r.not_after is None:
            status = "UNKNOWN"
            days = "?"
            exp = "?"
        else:
            d = r.days_remaining if r.days_remaining is not None else 999999
            if d < 0:
                status = "EXPIRED"
            elif d <= window_days:
                status = "EXPIRING"
            else:
                status = "OK"
            days = str(d)
            exp = r.not_after.strftime("%Y-%m-%d %H:%M:%S")

        name = (r.name or "")[:35]
        subj = (r.subject or "")[:70]
        print(f"{status:10} {days:>5} {exp:20}  {name:35}  {subj}")

    print("")


# -----------------------------
# NITRO client
# -----------------------------

class NitroError(RuntimeError):
    def __init__(self, status: int, message: str, payload: Optional[dict] = None):
        super().__init__(f"NITRO error (HTTP {status}): {message}")
        self.status = status
        self.message = message
        self.payload = payload


class NSConsoleClient:
    def __init__(self, console: str, insecure: bool = False, timeout: int = 30):
        self.console = console.rstrip("/")
        self.insecure = insecure
        self.timeout = timeout
        self.session = requests.Session()
        self.token: Optional[str] = None

    def login(self, username: str, password: str) -> str:
        url = f"{self.console}/nitro/v2/config/login"
        payload = {"login": {"username": username, "password": password}}

        r = self.session.post(
            url,
            json=payload,
            verify=not self.insecure,
            timeout=self.timeout,
        )

        try:
            j = r.json()
        except Exception:
            raise NitroError(r.status_code, r.text)

        if r.status_code >= 400:
            msg = j.get("message") or r.text
            raise NitroError(r.status_code, msg, j)

        try:
            token = j["login"][0]["sessionid"]
        except Exception:
            raise NitroError(r.status_code, "Login response missing sessionid", j)

        self.token = token
        return token

    def _headers(self) -> Dict[str, str]:
        if not self.token:
            return {}
        return {"Cookie": f"NITRO_AUTH_TOKEN={self.token}"}

    def get_json(self, path: str, params: Optional[dict] = None) -> dict:
        url = f"{self.console}{path}"
        r = self.session.get(
            url,
            headers=self._headers(),
            params=params or {},
            verify=not self.insecure,
            timeout=self.timeout,
        )

        try:
            j = r.json()
        except Exception:
            raise NitroError(r.status_code, r.text)

        if r.status_code >= 400:
            msg = j.get("message") or r.text
            raise NitroError(r.status_code, msg, j)

        return j

    def discover_cert_endpoints(self) -> List[str]:
        """
        Console can vary. We try to discover likely cert inventory resources.
        """
        j = self.get_json("/nitro/v1/config/")
        objs = j.get("configobjects") or []
        candidates = []

        # Most promising first
        for name in [
            "ssl_certificate",
            "ns_ssl_cert",
            "ssl_cert",
            "ns_ssl_certkey",
            "ns_ssl_files",
        ]:
            if name in objs:
                candidates.append(name)

        # fallback: scan for anything containing ssl + cert
        for o in objs:
            if "cert" in o and "ssl" in o and o not in candidates:
                candidates.append(o)

        return candidates

    def fetch_cert_inventory(self) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Best-effort: tries multiple known endpoints until one returns something usable.

        Returns: (resource_name, list_of_cert_dicts)
        """
        endpoints_to_try = [
            "/nitro/v2/config/ssl_certificate",
            "/nitro/v2/config/ns_ssl_cert",
            "/nitro/v1/config/ssl_certificate",
            "/nitro/v1/config/ns_ssl_cert",
            "/nitro/v1/config/ssl_cert",
        ]

        last_err: Optional[Exception] = None

        for ep in endpoints_to_try:
            try:
                j = self.get_json(ep, params={"attrs": "*"})
                # resourceType is sometimes in response
                # actual list key is usually last path segment
                key = ep.split("/")[-1]
                items = j.get(key)
                if isinstance(items, list):
                    return (key, items)
            except Exception as e:
                last_err = e
                continue

        # If none worked, attempt discovery from /nitro/v1/config/
        try:
            candidates = self.discover_cert_endpoints()
        except Exception as e:
            raise RuntimeError(f"Unable to discover Console resources: {e}")

        for name in candidates:
            for base in ["v2", "v1"]:
                ep = f"/nitro/{base}/config/{name}"
                try:
                    j = self.get_json(ep, params={"attrs": "*"})
                    items = j.get(name)
                    if isinstance(items, list):
                        return (name, items)
                except Exception as e:
                    last_err = e
                    continue

        raise RuntimeError(f"Unable to fetch certificate inventory from Console. Last error: {last_err}")


# -----------------------------
# Extraction logic
# -----------------------------

def _extract_cert_record(item: Dict[str, Any]) -> CertRecord:
    """
    Normalize different possible schema shapes into a CertRecord.
    We do not assume exact fields since Console varies.
    """
    name = (
        item.get("certkey") or
        item.get("certname") or
        item.get("file_name") or
        item.get("name") or
        item.get("cert") or
        ""
    )

    subject = item.get("subject") or item.get("cert_subject") or ""
    issuer = item.get("issuer") or item.get("cert_issuer") or ""

    # try common expiry fields
    expiry_raw = (
        item.get("notafter") or
        item.get("not_after") or
        item.get("expiry") or
        item.get("expiration") or
        item.get("validto") or
        item.get("enddate") or
        item.get("cert_expiry") or
        ""
    )

    not_after = _parse_console_datetime(expiry_raw)

    return CertRecord(
        name=str(name),
        subject=str(subject),
        issuer=str(issuer),
        not_after=not_after,
        days_remaining=_days_remaining(not_after),
        raw=item,
    )


# -----------------------------
# Main
# -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Poll NetScaler Console for expired/expiring certificates.")
    ap.add_argument("--console", required=True, help="NetScaler Console base URL (e.g. https://192.168.113.2)")
    ap.add_argument("--user", required=True, help="Console username (e.g. nsroot)")
    ap.add_argument("--password", help="Console password (omit to prompt)")
    ap.add_argument("--insecure", action="store_true", help="Disable TLS verification (lab use)")
    ap.add_argument("--window-days", type=int, default=30, help="Expiring window (days). Default: 30")
    ap.add_argument("--expired-only", action="store_true", help="Only show expired certificates")
    ap.add_argument("--json-out", help="Write JSON report to this path")
    args = ap.parse_args()

    password = args.password or getpass.getpass(f"Console password for {args.user}@{args.console}: ")

    client = NSConsoleClient(args.console, insecure=args.insecure)

    print("[console] Logging in...")
    client.login(args.user, password)
    print("[console] Login OK.")

    print("[console] Fetching certificate inventory...")
    resource_name, items = client.fetch_cert_inventory()
    print(f"[console] Inventory source: {resource_name} ({len(items)} objects)")

    records: List[CertRecord] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        records.append(_extract_cert_record(item))

    # filter
    filtered: List[CertRecord] = []
    for r in records:
        if r.not_after is None or r.days_remaining is None:
            # keep unknowns unless expired-only is set
            if not args.expired_only:
                filtered.append(r)
            continue

        if args.expired_only:
            if r.days_remaining < 0:
                filtered.append(r)
        else:
            # include everything, but report will highlight expiring
            filtered.append(r)

    _print_table(filtered, args.window_days)

    # Optional JSON artifact
    if args.json_out:
        out_obj = {
            "generated_utc": _now_utc().isoformat(),
            "console": args.console,
            "window_days": args.window_days,
            "resource": resource_name,
            "count_total": len(records),
            "count_reported": len(filtered),
            "certs": [
                {
                    "name": r.name,
                    "subject": r.subject,
                    "issuer": r.issuer,
                    "not_after_utc": r.not_after.isoformat() if r.not_after else None,
                    "days_remaining": r.days_remaining,
                    "raw": r.raw,
                }
                for r in filtered
            ],
        }

        os.makedirs(os.path.dirname(args.json_out) or ".", exist_ok=True)
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(out_obj, f, indent=2)
        print(f"[local] Wrote JSON report: {args.json_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())