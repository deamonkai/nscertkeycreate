#!/usr/bin/env python3
"""Inspect Console settings that can impact file uploads."""

from __future__ import annotations

import argparse
import getpass
import json
import os
from typing import Any, Dict, Optional

from certctl.console import NitroConsoleClient, NitroError


def _load_password(user: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {user}@{console}: ")


def _select_settings(settings: Dict[str, Any]) -> Dict[str, Any]:
    keys = [
        "basicauth",
        "secure_access_only",
        "enable_certificate_download",
        "enable_shell_access",
        "enable_apiproxy_credentials",
        "authorize_deviceapiproxy",
        "session_timeout",
        "session_timeout_unit",
    ]
    return {k: settings.get(k) for k in keys if k in settings}


def _get_settings(client: NitroConsoleClient) -> Dict[str, Any]:
    data = client.get_json("/nitro/v2/config/system_settings")
    settings = data.get("system_settings")
    if isinstance(settings, list) and settings:
        return settings[0]
    if isinstance(settings, dict):
        return settings
    return {}


def _get_summary(client: NitroConsoleClient) -> Dict[str, Any]:
    try:
        data = client.get_json("/nitro/v2/config/mas_summary")
    except NitroError:
        return {}
    summary = data.get("mas_summary")
    if isinstance(summary, list) and summary:
        return summary[0]
    if isinstance(summary, dict):
        return summary
    return {}


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

    settings = _get_settings(client)
    if not settings:
        print("No system_settings returned.")
    else:
        selected = _select_settings(settings)
        print("System settings (selected):")
        print(json.dumps(selected, indent=2, sort_keys=True))
        if args.full:
            print("System settings (full):")
            print(json.dumps(settings, indent=2, sort_keys=True))

    summary = _get_summary(client)
    if summary:
        print("MAS summary (selected):")
        pick = {k: summary.get(k) for k in ["ns_count", "ns_ssl_certkey_count", "sdx_count", "tenant_count"]}
        print(json.dumps(pick, indent=2, sort_keys=True))

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect Console settings relevant to file uploads.")
    parser.add_argument("--console", help="Console URL (e.g., https://192.0.2.10)")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--password", help="Console password (optional; env CERTCTL_CONSOLE_PASSWORD used by default)")
    parser.add_argument("--insecure", action="store_true", help="Skip TLS verification")
    parser.add_argument("--ca-bundle", help="CA bundle path for TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    parser.add_argument("--full", action="store_true", help="Include full system_settings output")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
