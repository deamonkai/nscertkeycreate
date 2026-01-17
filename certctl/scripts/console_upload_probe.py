#!/usr/bin/env python3
"""Probe Console file upload endpoints to see if uploads are blocked."""

from __future__ import annotations

import argparse
import getpass
import os
import tempfile
from pathlib import Path
from typing import Optional

from certctl.console import NitroConsoleClient, NitroError


def _load_password(user: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {user}@{console}: ")


def _probe_upload(client: NitroConsoleClient, resource: str, payload: Path, *, user: str, password: str) -> None:
    try:
        client.upload_file(
            f"/nitro/v2/upload/{resource}",
            str(payload),
            basic_user=user,
            basic_password=password,
        )
        print(f"[ok] upload succeeded: {resource}")
    except NitroError as exc:
        print(f"[error] upload failed: {resource} -> {exc}")


def run(args: argparse.Namespace) -> int:
    if not args.console or not args.user:
        raise SystemExit("Console URL and user are required.")

    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    password = _load_password(args.user, args.console, args.password)
    client = NitroConsoleClient(base=args.console, verify=verify, timeout=args.timeout)
    client.login(args.user, password)

    with tempfile.TemporaryDirectory() as td:
        payload = Path(td) / "probe.txt"
        payload.write_text("upload probe", encoding="utf-8")
        for resource in args.resource:
            _probe_upload(client, resource, payload, user=args.user, password=password)

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Probe Console upload endpoints.")
    parser.add_argument("--console", help="Console URL (e.g., https://192.0.2.10)")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--password", help="Console password (optional; env CERTCTL_CONSOLE_PASSWORD used by default)")
    parser.add_argument("--insecure", action="store_true", help="Skip TLS verification")
    parser.add_argument("--ca-bundle", help="CA bundle path for TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    parser.add_argument(
        "--resource",
        action="append",
        default=["mps_image", "ns_ssl_cert", "ns_ssl_key"],
        help="Upload resource name (repeatable). Default: mps_image, ns_ssl_cert, ns_ssl_key",
    )
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
