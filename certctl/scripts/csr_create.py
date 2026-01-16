#!/usr/bin/env python3
"""Create a CSR from an encrypted private key with optional SANs."""

from __future__ import annotations

import argparse
import getpass
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable, Optional


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise SystemExit("OpenSSL not found in PATH.")
    return path


def _normalize_sans(values: Iterable[str]) -> list[str]:
    normalized = []
    for value in values:
        parts = [part.strip() for part in value.split(",") if part.strip()]
        normalized.extend(parts)
    return normalized


def _write_openssl_config(subject: str, sans: Iterable[str]) -> str:
    alt_lines = []
    dns_i = 1
    ip_i = 1
    for san in _normalize_sans(sans):
        if san.lower().startswith("dns:"):
            alt_lines.append(f"DNS.{dns_i} = {san[4:]}")
            dns_i += 1
        elif san.lower().startswith("ip:"):
            alt_lines.append(f"IP.{ip_i} = {san[3:]}")
            ip_i += 1
        elif all(part.isdigit() for part in san.split(".")) and san.count(".") == 3:
            alt_lines.append(f"IP.{ip_i} = {san}")
            ip_i += 1
        else:
            alt_lines.append(f"DNS.{dns_i} = {san}")
            dns_i += 1

    alt_block = "\n".join(alt_lines) if alt_lines else ""
    if alt_lines:
        cfg = f"""[req]
default_bits = 2048
prompt = no
distinguished_name = dn
req_extensions = v3_req

[dn]
{_subject_to_dn(subject)}

[v3_req]
subjectAltName = @alt_names

[alt_names]
{alt_block}
"""
    else:
        cfg = f"""[req]
default_bits = 2048
prompt = no
distinguished_name = dn

[dn]
{_subject_to_dn(subject)}
"""
    handle = tempfile.NamedTemporaryFile("w", delete=False)
    handle.write(cfg)
    handle.close()
    return handle.name


def _timestamp() -> str:
    import datetime as dt

    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def _subject_to_dn(subject: str) -> str:
    subject = subject.strip()
    if subject.startswith("/"):
        parts = [p for p in subject.split("/") if p]
        kv_pairs = [p.split("=", 1) for p in parts if "=" in p]
    else:
        kv_pairs = [p.split("=", 1) for p in subject.split(",") if "=" in p]

    lines = []
    for key, value in kv_pairs:
        lines.append(f"{key.strip()} = {value.strip()}")
    return "\n".join(lines)


def _extract_cn(subject: str) -> str:
    subject = subject.strip()
    if subject.startswith("/"):
        parts = [p for p in subject.split("/") if p]
        for part in parts:
            if part.upper().startswith("CN="):
                return part.split("=", 1)[1].strip()
        return ""
    for part in subject.split(","):
        if part.strip().upper().startswith("CN="):
            return part.split("=", 1)[1].strip()
    return ""


def _build_subject_from_args(args: argparse.Namespace) -> str:
    if args.subject:
        return args.subject
    cn = args.cn
    if not cn:
        cn = input("Common Name (CN): ").strip()
    if not cn:
        raise SystemExit("Common Name (CN) is required.")
    parts = [
        f"/C={args.country}",
        f"/ST={args.state}",
        f"/L={args.locality}",
        f"/O={args.organization}",
        f"/OU={args.org_unit}",
        f"/CN={cn}",
        f"/emailAddress={args.email}",
    ]
    return "".join(parts)


def _run(cmd: list[str], env: Optional[dict[str, str]] = None) -> None:
    subprocess.run(cmd, check=True, env=env)


def _get_passphrase(args: argparse.Namespace) -> str:
    if args.passphrase:
        return args.passphrase
    env = os.environ.get("CERTCTL_KEY_PASSPHRASE")
    if env:
        return env
    return getpass.getpass("Key passphrase (AES-256): ")


def _build_csr_name(cn: str, stamp: str) -> str:
    return f"{cn}-{stamp}.csr"


def run(args: argparse.Namespace) -> int:
    _require_openssl()
    passphrase = _get_passphrase(args)
    key_path = Path(args.key_file)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    subject = _build_subject_from_args(args)
    cn = args.cn or _extract_cn(subject)
    if not cn:
        raise SystemExit("Common Name (CN) is required to build the CSR filename.")
    stamp = args.stamp or _timestamp()
    out_path = out_dir / _build_csr_name(cn, stamp)
    cfg_path = _write_openssl_config(subject, args.san or [])
    try:
        cmd = [
            "openssl",
            "req",
            "-new",
            "-key",
            str(key_path),
            "-out",
            str(out_path),
            "-config",
            cfg_path,
            "-passin",
            f"pass:{passphrase}",
        ]
        _run(cmd)
    finally:
        os.unlink(cfg_path)

    print(f"Wrote CSR: {out_path}")
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a CSR from an encrypted private key.")
    parser.add_argument("--key-file", required=True, help="Path to encrypted private key PEM")
    parser.add_argument("--subject", help="Subject (e.g., /C=US/ST=CA/CN=example.com)")
    parser.add_argument("--cn", help="Common Name (CN) when building a subject from defaults")
    parser.add_argument("--country", default="US", help="CountryName (C)")
    parser.add_argument("--state", default="Alabama", help="StateName (ST)")
    parser.add_argument("--organization", default="Regions Financial Corporation", help="OrganizationName (O)")
    parser.add_argument("--org-unit", default="ECommerce", help="OrganizationITName (OU)")
    parser.add_argument("--locality", default="Birmingham", help="LocalityName (L)")
    parser.add_argument("--email", default="was@regions.com", help="emailAddress")
    parser.add_argument(
        "--san",
        action="append",
        help="SubjectAltName entries (comma-separated or repeatable)",
    )
    parser.add_argument("--out", default="./out", help="Output directory for CSR files")
    parser.add_argument("--passphrase", help="Key passphrase (or set CERTCTL_KEY_PASSPHRASE)")
    parser.add_argument("--stamp", help="Timestamp to use in the filename (e.g., 20260101-120000)")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
