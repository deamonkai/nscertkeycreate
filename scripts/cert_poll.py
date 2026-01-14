#!/usr/bin/env python3
"""
cert_poll.py

Poll NetScaler Console for certificate inventory + expiry dates and generate a report.

Goals:
- Cross-platform (macOS/Windows/Linux)
- No external dependencies beyond requests (and optionally keyring)
- Uses NITRO v2 login once -> session token -> Cookie: NITRO_AUTH_TOKEN=...
- Produces JSON + Markdown report
- File lock to prevent concurrent runs on same machine

NOTE:
- NetScaler Console NITRO resources vary by build/license.
- This script tries a few known endpoints and will fall back gracefully.
"""

import argparse
import datetime as dt
import getpass
import json
import os
import platform
import re
import socket
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests


# -----------------------------
# Utilities
# -----------------------------

class NitroError(RuntimeError):
    def __init__(self, status_code: int, message: str, payload: Optional[dict] = None):
        super().__init__(f"NITRO error (HTTP {status_code}): {message}")
        self.status_code = status_code
        self.message = message
        self.payload = payload or {}


def _now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _ts_local_compact() -> str:
    # Example: 20260109-231530
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def _safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _write_bytes(path: Path, content: bytes) -> None:
    path.write_bytes(content)


def _iso(dt_obj: Optional[dt.datetime]) -> Optional[str]:
    if not dt_obj:
        return None
    return dt_obj.astimezone(dt.timezone.utc).isoformat()


def _parse_datetime_any(s: str) -> Optional[dt.datetime]:
    """
    Attempts to parse common date formats seen in Console inventory.
    Examples observed:
      - "2026-01-09 04:09:55"
      - "2026-01-09T04:09:55Z"
      - epoch seconds as string
    """
    if not s:
        return None

    s = str(s).strip()
    if not s:
        return None

    # epoch seconds
    if re.fullmatch(r"\d{9,12}", s):
        try:
            return dt.datetime.fromtimestamp(int(s), tz=dt.timezone.utc)
        except Exception:
            return None

    # "YYYY-MM-DD HH:MM:SS"
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"):
        try:
            return dt.datetime.strptime(s, fmt).replace(tzinfo=dt.timezone.utc)
        except Exception:
            pass

    # ISO-ish
    try:
        # normalize trailing Z
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        return dt.datetime.fromisoformat(s)
    except Exception:
        return None


# -----------------------------
# Cross-platform file lock
# -----------------------------

class FileLock:
    """
    Simple cross-platform lock using atomic directory creation.
    This avoids platform-specific fcntl/msvcrt issues and works well on local filesystems.

    Lock is represented by a directory, e.g.:
      /tmp/certctl.lock/

    We also write metadata inside for debugging.
    """

    def __init__(self, lock_dir: Path, stale_seconds: int = 3600):
        self.lock_dir = lock_dir
        self.stale_seconds = stale_seconds

    def acquire(self, wait_seconds: int = 0) -> None:
        start = time.time()
        while True:
            try:
                self.lock_dir.mkdir(parents=True, exist_ok=False)
                # write metadata
                meta = {
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                    "user": getpass.getuser(),
                    "platform": platform.platform(),
                    "created": _now_utc().isoformat(),
                }
                _write_text(self.lock_dir / "meta.json", json.dumps(meta, indent=2))
                return
            except FileExistsError:
                # check staleness
                meta_path = self.lock_dir / "meta.json"
                if meta_path.exists():
                    try:
                        m = json.loads(meta_path.read_text(encoding="utf-8"))
                        created = _parse_datetime_any(m.get("created", ""))
                        if created:
                            age = (_now_utc() - created.astimezone(dt.timezone.utc)).total_seconds()
                            if age > self.stale_seconds:
                                # stale lock -> remove
                                self.release(force=True)
                                continue
                    except Exception:
                        pass

                if wait_seconds <= 0:
                    raise RuntimeError(f"Lock already held: {self.lock_dir}")

                if time.time() - start > wait_seconds:
                    raise RuntimeError(f"Timed out waiting for lock: {self.lock_dir}")

                time.sleep(0.25)

    def release(self, force: bool = False) -> None:
        if not self.lock_dir.exists():
            return
        # best effort cleanup
        try:
            for child in self.lock_dir.iterdir():
                try:
                    child.unlink()
                except Exception:
                    pass
            self.lock_dir.rmdir()
        except Exception:
            if not force:
                raise


# -----------------------------
# NetScaler Console NITRO v2 client
# -----------------------------

class ConsoleClient:
    def __init__(self, console_url: str, insecure: bool = False, timeout: int = 30):
        self.console_url = console_url.rstrip("/")
        self.insecure = insecure
        self.timeout = timeout
        self.session = requests.Session()
        self.token: Optional[str] = None

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return self.console_url + path

    def login(self, username: str, password: str) -> str:
        """
        POST /nitro/v2/config/login
        Response includes login[0].sessionid, which must be used as NITRO_AUTH_TOKEN cookie.
        """
        payload = {"login": {"username": username, "password": password}}
        r = self.session.post(
            self._url("/nitro/v2/config/login"),
            json=payload,
            verify=not self.insecure,
            timeout=self.timeout,
        )
        j = self._json_or_raise(r)
        try:
            token = j["login"][0]["sessionid"]
        except Exception:
            raise NitroError(r.status_code, "Login response missing sessionid", j)
        self.token = token
        return token

    def _headers(self) -> Dict[str, str]:
        h: Dict[str, str] = {}
        if self.token:
            h["Cookie"] = f"NITRO_AUTH_TOKEN={self.token}"
        return h

    def get(self, path: str, params: Optional[dict] = None) -> dict:
        r = self.session.get(
            self._url(path),
            headers=self._headers(),
            params=params or {},
            verify=not self.insecure,
            timeout=self.timeout,
        )
        return self._json_or_raise(r)

    def _json_or_raise(self, r: requests.Response) -> dict:
        try:
            j = r.json()
        except Exception:
            raise NitroError(r.status_code, f"Non-JSON response: {r.text[:200]}")
        # Console often returns 200 with errorcode != 0
        if r.status_code >= 400:
            msg = j.get("message") or r.reason or "HTTP error"
            raise NitroError(r.status_code, msg, j)
        if isinstance(j, dict) and "errorcode" in j and j.get("errorcode") not in (0, "0", None):
            msg = j.get("message") or "NITRO error"
            raise NitroError(r.status_code, msg, j)
        return j


# -----------------------------
# Report model
# -----------------------------

@dataclass
class CertRecord:
    name: str
    subject: Optional[str]
    issuer: Optional[str]
    not_after: Optional[str]
    days_remaining: Optional[int]
    source: str  # "console"
    raw: Dict[str, Any]


def _days_remaining(not_after_dt: Optional[dt.datetime]) -> Optional[int]:
    if not not_after_dt:
        return None
    delta = not_after_dt.astimezone(dt.timezone.utc) - _now_utc()
    return int(delta.total_seconds() // 86400)


# -----------------------------
# Inventory fetch logic
# -----------------------------

def fetch_console_certs(client: ConsoleClient) -> List[CertRecord]:
    """
    Tries multiple known endpoints and normalizes results.

    Console may expose:
      - /nitro/v1/config/ssl_cert
      - /nitro/v1/config/ns_ssl_cert
      - /nitro/v2/config/ssl_cert
      - /nitro/v2/config/ns_ssl_cert
      - /nitro/v1/config/ssl_certificate (analytics type) [not the same thing]

    We'll try v2 first, then v1.
    """
    candidates = [
        ("/nitro/v2/config/ns_ssl_cert?attrs=*", "ns_ssl_cert"),
        ("/nitro/v2/config/ssl_cert?attrs=*", "ssl_cert"),
        ("/nitro/v1/config/ns_ssl_cert?attrs=*", "ns_ssl_cert"),
        ("/nitro/v1/config/ssl_cert?attrs=*", "ssl_cert"),
    ]

    last_err: Optional[Exception] = None
    for path, key in candidates:
        try:
            j = client.get(path)
            objs = j.get(key, [])
            if not isinstance(objs, list):
                continue
            out: List[CertRecord] = []
            for o in objs:
                if not isinstance(o, dict):
                    continue

                # Try common fields
                name = (
                    o.get("file_name")
                    or o.get("certkey")
                    or o.get("name")
                    or o.get("certificate")
                    or "UNKNOWN"
                )

                subject = o.get("subject") or o.get("cert_subject") or o.get("certsubject")
                issuer = o.get("issuer") or o.get("cert_issuer") or o.get("certissuer")

                # expiry fields vary wildly
                not_after = (
                    o.get("notafter")
                    or o.get("not_after")
                    or o.get("valid_to")
                    or o.get("expiry_date")
                    or o.get("cert_expiry")
                    or o.get("expiration")
                )

                not_after_dt = _parse_datetime_any(str(not_after)) if not_after else None
                days = _days_remaining(not_after_dt)

                out.append(
                    CertRecord(
                        name=str(name),
                        subject=str(subject) if subject else None,
                        issuer=str(issuer) if issuer else None,
                        not_after=_iso(not_after_dt),
                        days_remaining=days,
                        source="console",
                        raw=o,
                    )
                )
            # If endpoint exists but empty, still valid
            return out
        except Exception as e:
            last_err = e
            continue

    raise RuntimeError(f"Unable to fetch cert inventory from Console. Last error: {last_err}")


# -----------------------------
# Renderers
# -----------------------------

def render_markdown(records: List[CertRecord], window_days: int, console: str) -> str:
    now = _now_utc()
    lines: List[str] = []
    lines.append(f"# Certificate Expiry Report")
    lines.append("")
    lines.append(f"- Generated (UTC): `{now.isoformat()}`")
    lines.append(f"- Console: `{console}`")
    lines.append(f"- Renewal window: `{window_days} days`")
    lines.append(f"- Total certs discovered: `{len(records)}`")
    lines.append("")

    expiring = [r for r in records if r.days_remaining is not None and r.days_remaining <= window_days]
    expiring.sort(key=lambda r: (r.days_remaining if r.days_remaining is not None else 999999, r.name))

    lines.append(f"## Expiring within {window_days} days ({len(expiring)})")
    lines.append("")
    if not expiring:
        lines.append("_No certificates found in the renewal window._")
        lines.append("")
        return "\n".join(lines)

    lines.append("| Days | Not After (UTC) | Name | Subject | Issuer |")
    lines.append("|---:|---|---|---|---|")
    for r in expiring:
        lines.append(
            f"| {r.days_remaining} | `{r.not_after or ''}` | `{r.name}` | `{r.subject or ''}` | `{r.issuer or ''}` |"
        )
    lines.append("")
    return "\n".join(lines)


# -----------------------------
# Main
# -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Poll NetScaler Console for cert expiry and generate a report."
    )
    ap.add_argument("--console", required=True, help="NetScaler Console base URL (e.g. https://192.168.113.2)")
    ap.add_argument("--user", required=True, help="Console username")
    ap.add_argument("--password", help="Console password (if omitted, prompt)")
    ap.add_argument("--insecure", action="store_true", help="Disable TLS verification (lab use)")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds (default: 30)")
    ap.add_argument("--window-days", type=int, default=30, help="Renewal window in days (default: 30)")
    ap.add_argument("--out-dir", default="./reports", help="Output directory for reports (default: ./reports)")
    ap.add_argument("--lock-file", default="./.certctl.lock", help="Lock dir path (default: ./.certctl.lock)")
    ap.add_argument("--lock-wait", type=int, default=0, help="Seconds to wait for lock (default: 0)")
    ap.add_argument("--lock-stale", type=int, default=3600, help="Stale lock seconds (default: 3600)")

    args = ap.parse_args()

    out_dir = Path(args.out_dir).expanduser().resolve()
    lock_dir = Path(args.lock_file).expanduser().resolve()

    _safe_mkdir(out_dir)

    lock = FileLock(lock_dir, stale_seconds=args.lock_stale)
    lock.acquire(wait_seconds=args.lock_wait)

    try:
        password = args.password or getpass.getpass(f"Console password for {args.user}@{args.console}: ")

        client = ConsoleClient(args.console, insecure=args.insecure, timeout=args.timeout)

        print("[console] Logging in...")
        client.login(args.user, password)
        print("[console] Login OK.")

        print("[console] Fetching cert inventory...")
        records = fetch_console_certs(client)
        print(f"[console] Discovered {len(records)} cert records.")

        # Filter only those with known expiry for reporting relevance
        # (we still include unknown expiry in JSON for troubleshooting)
        window = int(args.window_days)

        report_ts = _ts_local_compact()
        json_path = out_dir / f"expiry_{report_ts}.json"
        md_path = out_dir / f"expiry_{report_ts}.md"

        payload = {
            "generated_utc": _now_utc().isoformat(),
            "console": args.console,
            "window_days": window,
            "total_records": len(records),
            "records": [asdict(r) for r in records],
        }

        _write_text(json_path, json.dumps(payload, indent=2))
        _write_text(md_path, render_markdown(records, window, args.console))

        print(f"[report] Wrote JSON: {json_path}")
        print(f"[report] Wrote MD:   {md_path}")

        # convenience: latest pointers
        latest_json = out_dir / "latest_expiry.json"
        latest_md = out_dir / "latest_expiry.md"
        _write_text(latest_json, json.dumps(payload, indent=2))
        _write_text(latest_md, render_markdown(records, window, args.console))

        print(f"[report] Updated latest_expiry.json / latest_expiry.md")

        # Exit code useful for automation:
        # 0 = ok
        # 2 = certs in renewal window found
        expiring = [r for r in records if r.days_remaining is not None and r.days_remaining <= window]
        if expiring:
            print(f"[alert] {len(expiring)} cert(s) within {window} days of expiry.")
            return 2

        return 0

    finally:
        lock.release(force=True)


if __name__ == "__main__":
    raise SystemExit(main())