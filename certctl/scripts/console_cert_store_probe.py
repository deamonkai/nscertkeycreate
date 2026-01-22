#!/usr/bin/env python3
"""Probe minimal cert_store payloads for Console uploads."""

from __future__ import annotations

import argparse
import base64
import getpass
import os
from pathlib import Path
from typing import Optional

from certctl.console import NitroConsoleClient, NitroError


def _read_bytes(path: str) -> bytes:
    return Path(path).expanduser().read_bytes()


def _b64_bytes(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii").rstrip("%")


def _load_console_password(username: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {username}@{console}: ")


def _load_key_password(provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_KEY_PASSPHRASE")
    if env_pw:
        return env_pw
    return getpass.getpass("Key passphrase (AES-256): ")


def _probe_server(
    client: NitroConsoleClient,
    *,
    name: str,
    cert_path: str,
    key_path: str,
    passphrase: str,
    domain: Optional[str],
    cert_file_name: Optional[str],
    cert_type: Optional[str],
    include_key_file: bool,
    dry_run: bool,
) -> None:
    cert_bytes = _read_bytes(cert_path)
    key_bytes = _read_bytes(key_path)
    cert_b64 = _b64_bytes(cert_bytes)
    key_b64 = _b64_bytes(key_bytes)
    payload = {
        "cert_store": {
            "name": name,
            "cert_format": "PEM",
            "cert_data": {"file_name": cert_file_name or f"{name}.pem", "file_data": cert_b64},
            "key_data": key_b64,
            "password": passphrase,
        }
    }
    if cert_type:
        payload["cert_store"]["cert_type"] = cert_type
    if domain:
        payload["cert_store"]["domain"] = domain
    if include_key_file:
        payload["cert_store"]["key_file"] = name
    print(
        "[probe] server payload sizes:"
        f" cert_b64={len(cert_b64)}"
        f" key_b64={len(key_b64)}"
    )
    if dry_run:
        print("[probe] dry run; skipping server cert_store upload.")
        return
    response = client.post_json("/nitro/v2/config/cert_store", payload)
    print("[probe] server response:", response)


def _probe_ca(
    client: NitroConsoleClient,
    *,
    name: str,
    cert_path: str,
    cert_file_name: Optional[str],
    cert_type: Optional[str],
    dry_run: bool,
) -> None:
    cert_bytes = _read_bytes(cert_path)
    cert_b64 = _b64_bytes(cert_bytes)
    payload = {
        "cert_store": {
            "name": name,
            "cert_format": "PEM",
            "cert_data": {"file_name": cert_file_name or f"{name}.pem", "file_data": cert_b64},
        }
    }
    if cert_type:
        payload["cert_store"]["cert_type"] = cert_type
    print(f"[probe] CA payload sizes: cert_b64={len(cert_b64)}")
    if dry_run:
        print("[probe] dry run; skipping CA cert_store upload.")
        return
    response = client.post_json("/nitro/v2/config/cert_store", payload)
    print("[probe] CA response:", response)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Probe minimal cert_store uploads (server cert/key and optional CA cert)."
    )
    parser.add_argument("--console", required=True, help="Console base URL, e.g. https://192.168.0.1")
    parser.add_argument("--user", required=True, help="Console username")
    parser.add_argument("--password", help="Console password (or CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="CA bundle path for TLS verification")
    parser.add_argument("--dry-run", action="store_true", help="Print sizes only; do not POST")

    parser.add_argument("--name", help="Cert_store name for server cert")
    parser.add_argument("--cert", dest="cert_path", help="Server certificate path (PEM)")
    parser.add_argument("--key", dest="key_path", help="Server key path (PEM)")
    parser.add_argument("--key-pass", dest="key_pass", help="Key passphrase")
    parser.add_argument("--domain", help="Domain for server cert_store entry")
    parser.add_argument("--cert-file-name", help="Override server cert file_name field")
    parser.add_argument("--cert-type", help="Set cert_type in server payload (e.g., server_cert)")
    parser.add_argument(
        "--include-key-file",
        action="store_true",
        help="Include key_file field in payload",
    )

    parser.add_argument("--ca-name", help="Cert_store name for CA cert")
    parser.add_argument("--ca-cert", dest="ca_cert_path", help="CA certificate path (PEM)")
    parser.add_argument("--ca-cert-file-name", help="Override CA cert file_name field")
    parser.add_argument("--ca-cert-type", help="Set cert_type in CA payload (e.g., root_cert)")

    args = parser.parse_args()

    if not args.name and not args.ca_name:
        raise SystemExit("Provide --name for server probe and/or --ca-name for CA probe.")
    if args.name and not (args.cert_path and args.key_path):
        raise SystemExit("Server probe requires --name, --cert, and --key.")
    if args.ca_name and not args.ca_cert_path:
        raise SystemExit("CA probe requires --ca-name and --ca-cert.")

    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    client = NitroConsoleClient(base=args.console, verify=verify, timeout=args.timeout)
    password = _load_console_password(args.user, args.console, args.password)
    client.login(args.user, password)

    if args.ca_name:
        _probe_ca(
            client,
            name=args.ca_name,
            cert_path=args.ca_cert_path,
            cert_file_name=args.ca_cert_file_name,
            cert_type=args.ca_cert_type,
            dry_run=args.dry_run,
        )

    if args.name:
        key_pass = _load_key_password(args.key_pass)
        _probe_server(
            client,
            name=args.name,
            cert_path=args.cert_path,
            key_path=args.key_path,
            passphrase=key_pass,
            domain=args.domain,
            cert_file_name=args.cert_file_name,
            cert_type=args.cert_type,
            include_key_file=args.include_key_file,
            dry_run=args.dry_run,
        )


if __name__ == "__main__":
    try:
        main()
    except NitroError as exc:
        raise SystemExit(str(exc)) from exc
