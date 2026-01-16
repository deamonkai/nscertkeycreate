from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List

from .console import ConsoleSession


def _parse_valid_to(s: str) -> datetime | None:
    """Parse a `valid_to` string returned by Console.

    Observed formats include:
      - "Jan 09 2026 04:09:55"
      - "2026-01-09 04:09:55"

    Returns a timezone-aware datetime (UTC) if parsing succeeds.
    """

    if not s:
        return None

    s = s.strip()
    fmts = [
        "%b %d %Y %H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%b %d %Y",
        "%Y-%m-%d",
    ]
    for fmt in fmts:
        try:
            dt = datetime.strptime(s, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


@dataclass
class CertKeyRow:
    file_name: str
    display_name: str
    days_to_expiry: int | None
    valid_to: str
    no_of_bound_entities: int | None


def poll_console_certkeys(
    session: ConsoleSession,
    *,
    window_days: int = 30,
) -> Dict[str, Any]:
    """Fetch cert inventory and produce filtered views.

    Returns a dict with:
      - all: list[CertKeyRow]
      - expired: list[CertKeyRow]
      - expiring: list[CertKeyRow] (0 < days <= window_days)
      - raw: raw NITRO JSON response
    """

    attrs = ",".join(
        [
            "file_name",
            "display_name",
            "valid_to",
            "days_to_expiry",
            "no_of_bound_entities",
        ]
    )
    raw = session.list_ssl_certkeys(attrs=attrs)
    items = raw.get("ns_ssl_certkey") or raw.get("ns_ssl_certkey_response") or []

    rows: List[CertKeyRow] = []
    for it in items:
        file_name = str(it.get("file_name", "") or "")
        display_name = str(it.get("display_name", "") or "")
        valid_to = str(it.get("valid_to", "") or "")

        dte_raw = it.get("days_to_expiry")
        days_to_expiry: int | None = None
        if dte_raw is not None and str(dte_raw).strip() != "":
            try:
                days_to_expiry = int(str(dte_raw))
            except ValueError:
                days_to_expiry = None

        bound_raw = it.get("no_of_bound_entities")
        bound: int | None = None
        if bound_raw is not None and str(bound_raw).strip() != "":
            try:
                bound = int(str(bound_raw))
            except ValueError:
                bound = None

        rows.append(
            CertKeyRow(
                file_name=file_name,
                display_name=display_name,
                days_to_expiry=days_to_expiry,
                valid_to=valid_to,
                no_of_bound_entities=bound,
            )
        )

    def key_sort(r: CertKeyRow):
        if r.days_to_expiry is None:
            dt = _parse_valid_to(r.valid_to)
            if dt:
                delta = dt - datetime.now(timezone.utc)
                return int(delta.total_seconds())
            return 10**9
        return r.days_to_expiry * 24 * 3600

    rows_sorted = sorted(rows, key=key_sort)

    expired = [r for r in rows_sorted if r.days_to_expiry is not None and r.days_to_expiry <= 0]
    expiring = [
        r
        for r in rows_sorted
        if r.days_to_expiry is not None and 0 < r.days_to_expiry <= window_days
    ]

    return {"all": rows_sorted, "expired": expired, "expiring": expiring, "raw": raw}


def write_report(
    report: Dict[str, Any],
    *,
    fmt: str = "table",
    out_path: str | None = None,
    include_all: bool = False,
) -> str:
    """Write report to a file (or return as a string for stdout)."""

    rows: List[CertKeyRow] = report["all"] if include_all else (report["expired"] + report["expiring"])

    if fmt == "json":
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "expired": [r.__dict__ for r in report["expired"]],
            "expiring": [r.__dict__ for r in report["expiring"]],
        }
        s = json.dumps(payload, indent=2)
    elif fmt == "csv":
        import io

        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["file_name", "display_name", "days_to_expiry", "valid_to", "no_of_bound_entities"])
        for r in rows:
            w.writerow([r.file_name, r.display_name, r.days_to_expiry, r.valid_to, r.no_of_bound_entities])
        s = buf.getvalue()
    else:
        # simple fixed-width table
        headers = ["File", "Display", "Days", "Valid To", "Bound"]
        data = [
            [
                r.file_name,
                r.display_name,
                "" if r.days_to_expiry is None else str(r.days_to_expiry),
                r.valid_to,
                "" if r.no_of_bound_entities is None else str(r.no_of_bound_entities),
            ]
            for r in rows
        ]
        cols = list(zip(headers, *data)) if data else [(h,) for h in headers]
        widths = [min(60, max(len(str(x)) for x in col)) for col in cols]

        def fmt_row(vals: List[str]) -> str:
            return "  ".join(str(v)[:w].ljust(w) for v, w in zip(vals, widths))

        lines = [fmt_row(headers), fmt_row(["-" * w for w in widths])]
        for row in data:
            lines.append(fmt_row(row))
        s = "\n".join(lines)

    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(s)
    return s
