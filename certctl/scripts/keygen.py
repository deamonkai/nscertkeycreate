#!/usr/bin/env python3
"""Generate an AES-encrypted RSA or EC private key in PEM format."""

from __future__ import annotations

import argparse
import getpass
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from certctl.console import NitroConsoleClient
from certctl.secretstore import get_secret, is_available, set_secret

DEFAULT_RSA_BITS = 4096
DEFAULT_EC_CURVE = "secp384r1"


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise SystemExit("OpenSSL not found in PATH.")
    return path


def _timestamp() -> str:
    import datetime as dt

    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def _build_key_name(cn: str, stamp: str) -> str:
    return f"{cn}-{stamp}.key"


def _get_passphrase(args: argparse.Namespace) -> str:
    if args.passphrase:
        return args.passphrase
    env = os.environ.get("CERTCTL_KEY_PASSPHRASE")
    if env:
        return env
    if args.keychain_service and is_available():
        stored = get_secret(args.keychain_service, args.keychain_username)
        if stored:
            return stored
    while True:
        pw = getpass.getpass("Key passphrase (AES-256): ")
        confirm = getpass.getpass("Confirm passphrase: ")
        if pw and pw == confirm:
            if args.keychain_service and args.save_passphrase:
                set_secret(args.keychain_service, args.keychain_username, pw)
            return pw
        print("Passphrases did not match, try again.")


def _run(cmd: list[str], env: Optional[dict[str, str]] = None) -> None:
    subprocess.run(cmd, check=True, env=env)


def _generate_key(kind: str, out_path: Path, passphrase: str) -> None:
    _require_openssl()
    if kind == "rsa":
        cmd = [
            "openssl",
            "genpkey",
            "-algorithm",
            "RSA",
            "-pkeyopt",
            f"rsa_keygen_bits:{DEFAULT_RSA_BITS}",
            "-aes-256-cbc",
            "-pass",
            f"pass:{passphrase}",
            "-out",
            str(out_path),
        ]
    else:
        cmd = [
            "openssl",
            "genpkey",
            "-algorithm",
            "EC",
            "-pkeyopt",
            f"ec_paramgen_curve:{DEFAULT_EC_CURVE}",
            "-pkeyopt",
            "ec_param_enc:named_curve",
            "-aes-256-cbc",
            "-pass",
            f"pass:{passphrase}",
            "-out",
            str(out_path),
        ]
    _run(cmd)
    os.chmod(out_path, 0o600)


def _upload_to_console(args: argparse.Namespace, key_path: Path, passphrase: str) -> None:
    if not args.upload_console:
        return
    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    password = args.console_password or os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if not password:
        password = getpass.getpass(f"Console password for {args.user}@{args.console}: ")

    client = NitroConsoleClient(base=args.console, verify=verify, timeout=args.timeout)
    client.login(args.user, password)
    client.upload_file("/nitro/v2/upload/ns_ssl_key", str(key_path))
    if args.register_console:
        algo = "RSA" if args.kind == "rsa" else "ECDSA"
        keysize = DEFAULT_RSA_BITS if args.kind == "rsa" else None
        ec_curve = DEFAULT_EC_CURVE if args.kind == "ecdsa" else None
        client.create_key(
            key_path.name,
            algo=algo,
            keyform="PEM",
            keysize=keysize,
            ec_curve=ec_curve,
            password=passphrase,
        )


def run(args: argparse.Namespace) -> int:
    passphrase = _get_passphrase(args)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = args.stamp or _timestamp()
    key_name = _build_key_name(args.cn, stamp)
    key_path = out_dir / key_name
    _generate_key(args.kind, key_path, passphrase)
    print(f"Wrote key: {key_path}")

    if args.upload_console:
        if not args.console or not args.user:
            raise SystemExit("Console URL and user are required for --upload-console.")
        _upload_to_console(args, key_path, passphrase)
        print("Uploaded key to NetScaler Console.")
        if args.register_console:
            print("Registered key metadata in NetScaler Console.")

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate an AES-encrypted RSA or EC private key.")
    parser.add_argument("--cn", required=True, help="Common Name (CN) for the key filename")
    parser.add_argument("--kind", choices=["rsa", "ecdsa"], required=True, help="Key type")
    parser.add_argument("--out", default="./out", help="Output directory for key files")
    parser.add_argument("--stamp", help="Timestamp to use in the filename (e.g., 20260101-120000)")
    parser.add_argument("--passphrase", help="Key passphrase (or set CERTCTL_KEY_PASSPHRASE)")
    parser.add_argument("--keychain-service", help="Keychain service name for passphrase storage")
    parser.add_argument(
        "--keychain-username",
        default=getpass.getuser(),
        help="Keychain username (default: current user)",
    )
    parser.add_argument(
        "--save-passphrase",
        action="store_true",
        default=False,
        help="Store passphrase in keychain (requires keyring)",
    )
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
