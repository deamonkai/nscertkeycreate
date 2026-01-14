#!/usr/bin/env python3
"""Create a private key on NetScaler Console, download it, and generate a CSR locally.

This is intentionally narrow-scope ("script 3" + "script 4" from your plan),
so it can be composed by a higher-level orchestrator later.

Outputs (PEM):
- <out_dir>/<key_name>
- <out_dir>/<csr_name>
- (optional) <out_dir>/latest.key and latest.csr symlinks/copies

Security:
- Console password and optional key passphrase can be pulled from the OS keychain
  (macOS Keychain today; enterprise vault adapters can be added later).

NetScaler Console behavior:
- We log in once via /nitro/v2/config/login (POST) to obtain a session token.
- We include Cookie: NITRO_AUTH_TOKEN=<token> on subsequent calls (especially downloads).

Usage example:
  python3 scripts/keycsr_console.py --console https://192.168.113.2 --user nsroot \
    --app-name example.com --out-dir ./out --insecure

"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from certctl.console import ConsoleClient, NitroError
from certctl.csr import Subject, make_csr_openssl
from certctl.secretstore import get_password, set_password
from certctl.san import normalize_san_list


@dataclass(frozen=True)
class DerivedNames:
    key_name: str
    csr_name: str


def _ts() -> str:
    # Stable + filename safe
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def derive_names(app_name: str, rotate: bool) -> DerivedNames:
    if rotate:
        stamp = _ts()
        base = f"{app_name}_{stamp}"
    else:
        base = app_name
    return DerivedNames(key_name=f"{base}.key", csr_name=f"{base}.csr")


def prompt_choice(prompt: str, choices: list[str], default_index: int = 0) -> int:
    while True:
        print(prompt)
        for i, c in enumerate(choices, 1):
            default = " (default)" if i - 1 == default_index else ""
            print(f"  {i}) {c}{default}")
        raw = input(f"Select [1-{len(choices)}]: ").strip()
        if raw == "":
            return default_index
        if raw.isdigit() and 1 <= int(raw) <= len(choices):
            return int(raw) - 1
        print("Invalid selection. Try again.\n")


def prompt_yesno(prompt: str, default_yes: bool = True) -> bool:
    suf = "[Y/n]" if default_yes else "[y/N]"
    raw = input(f"{prompt} {suf} ").strip().lower()
    if raw == "":
        return default_yes
    return raw in ("y", "yes")


def write_latest(out_dir: Path, latest_name: str, target_name: str) -> None:
    latest = out_dir / latest_name
    target = out_dir / target_name
    try:
        if latest.exists() or latest.is_symlink():
            latest.unlink()
        latest.symlink_to(target.name)
    except Exception:
        # Windows / restrictive FS: fall back to copy
        latest.write_bytes(target.read_bytes())


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="keycsr_console.py",
        description="Create key on NetScaler Console, download it, and generate CSR locally.",
    )
    p.add_argument("--console", required=True, help="Console base URL, e.g. https://192.168.113.2")
    p.add_argument("--user", required=True, help="Console username")
    p.add_argument("--app-name", required=True, help="App name / base CN (used for derived filenames)")
    p.add_argument("--out-dir", default="./out", help="Output directory")
    p.add_argument("--rotate", action="store_true", default=True, help="Always timestamp filenames (default: on)")
    p.add_argument(
        "--no-rotate", dest="rotate", action="store_false", help="Do not timestamp filenames (NOT recommended)"
    )
    p.add_argument(
        "--write-latest",
        action="store_true",
        default=True,
        help="Write latest.key/latest.csr pointers (default: on)",
    )
    p.add_argument(
        "--no-write-latest",
        dest="write_latest",
        action="store_false",
        help="Disable writing latest.key/latest.csr",
    )
    p.add_argument("--insecure", action="store_true", help="Disable TLS verification")

    args = p.parse_args(argv)

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    names = derive_names(args.app_name, rotate=args.rotate)

    print("\n[info] Derived names:")
    print(f"       Key: {names.key_name}")
    print(f"       CSR: {names.csr_name}")
    print(f"       Rotate: {'ON' if args.rotate else 'OFF'}")
    print(f"       Write latest: {'ON' if args.write_latest else 'OFF'}")
    if not prompt_yesno("Proceed with these names?", default_yes=True):
        print("Aborted.")
        return 2

    # ---- key type / encryption choices
    key_choice = prompt_choice(
        "Select key type:",
        ["RSA 4096 (common/compatible)", "ECDSA (best-practice default curve)"],
        default_index=1,
    )
    key_algo = "RSA" if key_choice == 0 else "EC"
    keysize = 4096 if key_algo == "RSA" else None
    ec_curve = "P_256" if key_algo == "EC" else None

    encrypt_key = prompt_yesno("Encrypt the private key with a passphrase?", default_yes=True)

    # ---- credentials (keychain)
    

    password = get_password(
        service="netscaler-console",
        account=f"{args.user}@{args.console}",
        prompt=f"Console password for {args.user}@{args.console}: ",
        store_prompt=True,
    )

    key_passphrase: str | None = None
    if encrypt_key:
        key_passphrase = get_password(
            service="cert-private-key",
            account=f"{args.app_name}",
            prompt="Key passphrase (will be stored in keychain if you choose): ",
            store_prompt=True,
        )

    # ---- CSR subject prompts
    cn = input(f"CSR Common Name (CN): ").strip() or args.app_name
    o = input("Organization (O) [optional]: ").strip()
    ou = input("Org Unit (OU) [optional]: ").strip()
    l = input("City/Locality (L) [optional]: ").strip()
    st = input("State/Province (ST) [optional, spell out like 'Alabama' (not 'AL')]: ").strip()
    c = input("Country (C) 2-letter [optional]: ").strip()
    san_raw = input("SubjectAltName string (e.g. DNS:example.com,DNS:www.example.com) [optional]: ").strip()

    san_list = normalize_san_list(san_raw)

    subj = Subject(cn=cn, o=o or None, ou=ou or None, l=l or None, st=st or None, c=c or None)

    # ---- Console operations
    print("\n[console] Logging in to establish session (for download/upload authorization)...")
    client = ConsoleClient(base_url=args.console, username=args.user, password=password, verify_tls=not args.insecure)
    client.login()
    print("[console] Login OK (token acquired).")

    print("\n[console] Creating key on Console (never reuse keys)...")
    try:
        client.create_ssl_key(
            file_name=names.key_name,
            algo=key_algo,
            keyform="PEM",
            keysize=keysize,
            ec_curve=ec_curve,
            password=key_passphrase,
            # prefer AES if supported; Console may fall back internally
            cipher="AES256" if encrypt_key else None,
        )
    except NitroError as e:
        # Common: name collision if rotate is off.
        raise

    print(f"[console] Key create accepted: {names.key_name}")

    print("\n[console] Downloading KEY via /nitro/v2/download ...")
    key_bytes = client.download_key(names.key_name)

    key_path = out_dir / names.key_name
    key_path.write_bytes(key_bytes)
    os.chmod(key_path, 0o600)
    print(f"[local] Wrote key: {key_path}")

    if args.write_latest:
        write_latest(out_dir, "latest.key", names.key_name)
        print(f"[local] Wrote latest.key -> {names.key_name}")

    # ---- CSR generation locally
    print("\n[local] Generating CSR with OpenSSL...")
    csr_pem = make_csr_openssl(
        key_pem_path=str(key_path),
        subject=subj,
        san_entries=san_list,
        key_passphrase=key_passphrase,
    )

    csr_path = out_dir / names.csr_name
    csr_path.write_text(csr_pem, encoding="utf-8")
    os.chmod(csr_path, 0o644)
    print(f"[local] Wrote CSR: {csr_path}")

    if args.write_latest:
        write_latest(out_dir, "latest.csr", names.csr_name)
        print(f"[local] Wrote latest.csr -> {names.csr_name}")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NitroError as e:
        print(str(e), file=sys.stderr)
        return_code = 1
        raise SystemExit(return_code)
