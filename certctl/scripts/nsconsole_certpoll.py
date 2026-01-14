#!/usr/bin/env python3
"""Poll NetScaler Console for certificate expiry and generate a report.

This is a standalone script meant to be called from cron/CI or by a future
overlay orchestrator.

Data source
---------
Uses NITRO resource `ns_ssl_certkey` on NetScaler Console, which includes
fields like `valid_to` and `days_to_expiry`.

Exit codes
---------
0: No expired certs and none within the renewal window
2: At least one cert is within the renewal window
3: At least one cert is expired

Security
---------
- Console password can be pulled from macOS Keychain via the existing
  secretstore helper.
- Use `--insecure` for self-signed lab certs, or provide `--ca-bundle`.
"""

from __future__ import annotations

# Allow running this script directly from the repo without installation.
import pathlib
import sys

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import argparse
import os
import sys

from certctl.console import ConsoleSession
from certctl.filelock import FileLock
from certctl.poll import poll_console_certkeys, write_report
from certctl import secretstore
from certctl.term import print_error, print_info


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nsconsole_certpoll",
        description="Poll NetScaler Console for expired / expiring certificates.",
    )
    p.add_argument("--console", required=True, help="Console base URL, e.g. https://192.168.113.2")
    p.add_argument("--user", required=True, help="Console username")
    p.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    p.add_argument("--ca-bundle", default=None, help="Path to CA bundle for TLS verify")
    p.add_argument("--window-days", type=int, default=30, help="Renewal window in days (default: 30)")
    p.add_argument("--format", choices=["table", "csv", "json"], default="table", help="Output format")
    p.add_argument(
        "--out",
        default=None,
        help="Write report to this file instead of stdout (csv/json only)",
    )
    p.add_argument(
        "--lock-file",
        default=None,
        help="Optional lock file path (default: <out-dir>/.certctl.lock or ./ .certctl.lock)",
    )
    p.add_argument(
        "--out-dir",
        default=".",
        help="Used only to place default lock file if --lock-file isn't set.",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    # File lock keeps cron from overlapping runs.
    lock_path = args.lock_file or os.path.join(os.path.abspath(args.out_dir), ".certctl.lock")
    os.makedirs(os.path.dirname(lock_path), exist_ok=True)

    # Our lightweight FileLock takes `timeout_seconds` (not `timeout`).
    # timeout_seconds=0 means: fail immediately if another run holds the lock.
    with FileLock(lock_path, timeout_seconds=0.0):
        # Password lookup order:
        #   1) CERTCTL_NSCONSOLE_PASS
        #   2) macOS Keychain (service=certctl:nsconsole, account=<user>@<console_url>)
        #   3) Prompt (optionally store to Keychain)
        password = secretstore.env_or_keychain(
            env_var="CERTCTL_NSCONSOLE_PASS",
            service="certctl:nsconsole",
            account=f"{args.user}@{args.console}",
        )
        if not password:
            import getpass

            password = getpass.getpass(f"Console password for {args.user}@{args.console}: ")
            if password and secretstore.is_macos_keychain_available():
                yn = input("Store Console password in keychain? [Y/n] ").strip().lower()
                if yn in ("", "y", "yes"):
                    secretstore.set_in_keychain(
                        service="certctl:nsconsole",
                        account=f"{args.user}@{args.console}",
                        secret=password,
                    )
        if not password:
            # We intentionally avoid a mandatory interactive prompt here so the script
            # stays automation-friendly. If you want to run interactively, just export
            # CERTCTL_NSCONSOLE_PASS or store it in keychain.
            print_error(
                "No Console password found. Set CERTCTL_NSCONSOLE_PASS, "
                "or store it in keychain under service 'certctl:nsconsole' and account '<user>@<console_url>'."
            )
            return 1


        if args.ca_bundle:
            print_error(
                "--ca-bundle is not wired up yet in this script. "
                "Use --insecure or rely on the system trust store."
            )
            return 1

        sess = ConsoleSession(
            base_url=args.console,
            username=args.user,
            password=password,
            insecure=args.insecure,
        )
        sess.login()

        report = poll_console_certkeys(sess, window_days=args.window_days)
        write_report(report, fmt=args.format, out_path=args.out)
        if args.out:
            print_info(f"Wrote {args.format} report: {args.out}")

        # Exit codes suitable for CI
        expired = report.get("expired", [])
        expiring = report.get("expiring", [])
        if expired:
            return 3
        if expiring:
            return 2
        return 0


if __name__ == "__main__":
    raise SystemExit(main())