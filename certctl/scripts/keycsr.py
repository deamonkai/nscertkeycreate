#!/usr/bin/env python3
"""Generate a key and CSR with a shared timestamp."""

from __future__ import annotations

import argparse
from pathlib import Path

from certctl.scripts import csr_create, keygen


def run(args: argparse.Namespace) -> int:
    if not args.keychain_username:
        args.keychain_username = keygen.getpass.getuser()
    stamp = args.stamp or keygen._timestamp()
    passphrase = keygen._get_passphrase(args)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    key_name = keygen._build_key_name(args.cn, stamp)
    key_path = out_dir / key_name
    keygen._generate_key(args.kind, key_path, passphrase)
    print(f"Wrote key: {key_path}")

    if args.upload_console:
        if not args.console or not args.user:
            raise SystemExit("Console URL and user are required for --upload-console.")
        keygen._upload_to_console(args, key_path, passphrase)
        print("Uploaded key to NetScaler Console.")
        if args.register_console:
            print("Registered key metadata in NetScaler Console.")

    csr_args = argparse.Namespace(
        key_file=str(key_path),
        subject=args.subject,
        cn=args.cn,
        country=args.country,
        state=args.state,
        organization=args.organization,
        org_unit=args.org_unit,
        locality=args.locality,
        email=args.email,
        san=args.san,
        out=args.out,
        passphrase=passphrase,
        stamp=stamp,
    )
    csr_create.run(csr_args)
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a key and CSR with a shared timestamp.")
    parser.add_argument("--cn", required=True, help="Common Name (CN) for key/CSR filenames")
    parser.add_argument("--kind", choices=["rsa", "ecdsa"], required=True, help="Key type")
    parser.add_argument("--out", default="./out", help="Output directory for key/CSR files")
    parser.add_argument("--stamp", help="Timestamp to use in filenames (e.g., 20260101-120000)")
    parser.add_argument("--passphrase", help="Key passphrase (or set CERTCTL_KEY_PASSPHRASE)")
    parser.add_argument("--keychain-service", help="Keychain service name for passphrase storage")
    parser.add_argument(
        "--keychain-username",
        default=None,
        help="Keychain username (default: current user)",
    )
    parser.add_argument(
        "--save-passphrase",
        action="store_true",
        default=False,
        help="Store passphrase in keychain (requires keyring)",
    )
    parser.add_argument("--subject", help="Full subject string to use for CSR")
    parser.add_argument("--country", default="US", help="CountryName (C)")
    parser.add_argument("--state", default="Alabama", help="StateName (ST)")
    parser.add_argument("--organization", default="Regions Financial Corporation", help="OrganizationName (O)")
    parser.add_argument("--org-unit", default="ECommerce", help="OrganizationITName (OU)")
    parser.add_argument("--locality", default="Birmingham", help="LocalityName (L)")
    parser.add_argument("--email", default="was@regions.com", help="emailAddress")
    parser.add_argument("--san", action="append", help="SubjectAltName entry (repeatable)")
    parser.add_argument(
        "--upload-console",
        action="store_true",
        default=False,
        help="Upload the key to NetScaler Console",
    )
    parser.add_argument(
        "--register-console",
        action="store_true",
        default=False,
        help="Register key metadata in NetScaler Console after upload",
    )
    parser.add_argument("--console", help="Console base URL, e.g. https://console")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--console-password", help="Console password (or set CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
