#!/usr/bin/env python3
"""certctl CLI.

Initial scope (v0):
- `certctl new` : generate key+CSR (PEM), upload/store to NetScaler Console, write artifacts locally.
- `certctl poll`: produce expiry report (default: <=30 days).

Future commands wire into dedicated modules:
- CA submit/poll/download (ADCS, Sectigo, etc.)
- Deploy to ADC via Console
- Deploy to Imperva (and others)

This file intentionally stays thin.
"""

from __future__ import annotations

import argparse
import sys

from certctl.modules.lock import FileLock
from certctl.modules.report import run_poll_report

# Reuse the existing working implementation for key+CSR generation as a module.
# We keep the original behavior but expose it as a subcommand.
try:
    from nscertkeycreate import main as legacy_main  # type: ignore
except Exception:
    legacy_main = None


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="certctl", description="Certificate lifecycle orchestrator")
    sub = p.add_subparsers(dest="cmd", required=True)

    # new (delegates to existing script for now)
    p_new = sub.add_parser("new", help="Create key+CSR via NetScaler Console, write artifacts locally")
    p_new.add_argument("--", dest="passthru", nargs=argparse.REMAINDER,
                       help="Pass remaining args to legacy nscertkeycreate (temporary)")

    # poll
    p_poll = sub.add_parser("poll", help="Poll expiries and produce a report")
    p_poll.add_argument("--console", required=True, help="NetScaler Console base URL")
    p_poll.add_argument("--user", required=True, help="Console username")
    p_poll.add_argument("--days", type=int, default=30, help="Renewal window in days")
    p_poll.add_argument("--out", default="./reports", help="Output directory")
    p_poll.add_argument("--insecure", action="store_true", help="Disable TLS verification")

    # maintenance (placeholder)
    p_maint = sub.add_parser("maint", help="Run maintenance workflow (placeholder)")
    p_maint.add_argument("--lock", default=".certctl.lock", help="Lock file path")

    return p


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    p = build_parser()
    args = p.parse_args(argv)

    if args.cmd == "new":
        if legacy_main is None:
            print("ERROR: legacy nscertkeycreate module is unavailable.", file=sys.stderr)
            return 2
        # Delegate: run `nscertkeycreate.py` behavior directly.
        # Users call: certctl new -- --console ... --app-name ...
        passthru = args.passthru or []
        return int(legacy_main(passthru))

    if args.cmd == "poll":
        with FileLock(".certctl.poll.lock"):
            run_poll_report(console=args.console, user=args.user, days=args.days,
                            out_dir=args.out, insecure=args.insecure)
        return 0

    if args.cmd == "maint":
        with FileLock(args.lock):
            print("maintenance workflow not implemented yet")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
