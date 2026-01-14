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
from certctl.poll import poll_console_certkeys
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

    with FileLock(lock_path, timeout=0):
        # For automation, prefer environment variable; fall back to local keychain.
        # You can store the secret under:
        #   service: certctl:nsconsole
        #   account: <user>@<console_url>
        password = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
        if not password:
            password = secretstore.get_secret("certctl:nsconsole", f"{args.user}@{args.console}")
        if password is None:
            # No interactive prompt here (poll scripts should be automatable).
            print_error(
                "No Console password found. Set CERTCTL_CONSOLE_PASSWORD, "
                "or store it in keychain under service 'certctl:nsconsole' and account '<user>@<console_url>'."
            )
            return 1

        verify = (not args.insecure)
        if args.ca_bundle:
            verify = args.ca_bundle

        sess = ConsoleSession(args.console, verify=verify)
        sess.login(args.user, password)

        report = poll_console_certkeys(sess, window_days=args.window_days)

        # Output
        if args.format == "table":
            print(report.to_table())
        else:
            if args.out:
                report.write(args.out, fmt=args.format)
                print_info(f"Wrote {args.format} report: {args.out}")
            else:
                sys.stdout.write(report.dumps(fmt=args.format))
                if not report.dumps(fmt=args.format).endswith("\n"):
                    sys.stdout.write("\n")

        # Exit codes suitable for CI
        if report.expired:
            return 3
        if report.expiring:
            return 2
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
