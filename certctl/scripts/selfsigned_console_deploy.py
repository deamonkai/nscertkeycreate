#!/usr/bin/env python3
"""Generate a self-signed cert and deploy it to Console and ADCs."""

from __future__ import annotations

import argparse
import getpass
import os
import re
import time
from pathlib import Path
from typing import List, Optional

from certctl.ca.selfsigned import SelfSignedAdapter, SelfSignedConfig
from certctl.console import NitroConsoleClient, NitroError
from certctl.scripts import csr_create, keygen, nsconsole_deploy


def _normalize_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value or "").strip("_")


def _timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def _load_console_password(args: argparse.Namespace) -> str:
    if args.console_password:
        return args.console_password
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {args.user}@{args.console}: ")


def _selfsign_passphrase(args: argparse.Namespace) -> str:
    if args.selfsign_passphrase:
        return args.selfsign_passphrase
    env_pw = os.environ.get("CERTCTL_SELFSIGN_PASSPHRASE") or os.environ.get("CERTCTL_KEY_PASSPHRASE")
    if env_pw:
        return env_pw
    return getpass.getpass("Self-signed CA passphrase (AES-256): ")


def _extract_chain_cas(chain_pem: str) -> str:
    blocks = re.findall(
        r"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----",
        chain_pem,
        flags=re.DOTALL,
    )
    if len(blocks) <= 1:
        return ""
    return "\n".join(blocks[1:]) + "\n"


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _is_basicauth_enabled(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "y", "on"}
    return False


def _maybe_enable_basicauth(client: NitroConsoleClient) -> bool:
    settings = client.get_system_settings()
    enabled = _is_basicauth_enabled(settings.get("basicauth"))
    if enabled:
        print("[console] basicauth already enabled; no change needed.")
        return False
    print("[console] basicauth disabled; enabling temporarily for upload.")
    client.set_basicauth(True)
    return True


def _restore_basicauth(client: NitroConsoleClient, *, changed: bool) -> None:
    if not changed:
        return
    print("[console] Restoring basicauth to disabled state.")
    client.set_basicauth(False)


def _upload_console_certkey(
    client: NitroConsoleClient,
    *,
    certkeypair_name: str,
    cert_file: Path,
    key_file: Path,
    passphrase: str,
    console_user: str,
    console_password: str,
) -> None:
    cert_pem = _read_text(cert_file)
    key_pem = _read_text(key_file)
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": certkeypair_name,
            "certificate_data": cert_pem,
            "key_data": key_pem,
            "password": passphrase,
            "cert_format": "PEM",
        }
    }
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)
        return
    except NitroError as exc:
        message = str(exc.message).lower()
        if "certificate file" not in message:
            raise

    try:
        client.upload_file(
            "/nitro/v2/upload/ns_ssl_key",
            str(key_file),
            basic_user=console_user,
            basic_password=console_password,
        )
    except NitroError as exc:
        message = str(exc.message).lower()
        if "file upload not allowed" in message:
            raise SystemExit(
                "Console disallows file uploads and requires certificate files for certkey creation. "
                "Enable file uploads in Console or import the cert/key via UI."
            ) from exc
        raise
    algo = "RSA" if "rsa" in key_file.name.lower() else "ECDSA"
    keysize = keygen.DEFAULT_RSA_BITS if algo == "RSA" else None
    ec_curve = keygen.DEFAULT_EC_CURVE if algo == "ECDSA" else None
    client.create_key(
        key_file.name,
        algo=algo,
        keyform="PEM",
        keysize=keysize,
        ec_curve=ec_curve,
        password=passphrase,
    )

    try:
        client.upload_file(
            "/nitro/v2/upload/ns_ssl_cert",
            str(cert_file),
            basic_user=console_user,
            basic_password=console_password,
        )
    except NitroError as exc:
        message = str(exc.message).lower()
        if "file upload not allowed" in message:
            raise SystemExit(
                "Console disallows certificate file uploads required for certkey creation. "
                "Enable file uploads in Console or import the certificate via UI."
            ) from exc
        raise
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": certkeypair_name,
            "certificate_file_name": cert_file.name,
            "key_file_name": key_file.name,
            "ssl_certificate": cert_file.name,
            "ssl_key": key_file.name,
            "password": passphrase,
            "cert_format": "PEM",
        }
    }
    client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)


def _upload_console_ca(
    client: NitroConsoleClient,
    *,
    ca_name: str,
    ca_file: Path,
    console_user: str,
    console_password: str,
) -> None:
    ca_pem = _read_text(ca_file)
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": ca_name,
            "certificate_data": ca_pem,
            "cert_format": "PEM",
        }
    }
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)
        return
    except NitroError as exc:
        message = str(exc.message).lower()
        if "certificate file" not in message:
            raise

    try:
        client.upload_file(
            "/nitro/v2/upload/ns_ssl_cert",
            str(ca_file),
            basic_user=console_user,
            basic_password=console_password,
        )
    except NitroError as exc:
        message = str(exc.message).lower()
        if "file upload not allowed" in message:
            raise SystemExit(
                "Console disallows CA file uploads required for CA cert creation. "
                "Enable file uploads in Console or import the CA certificate via UI."
            ) from exc
        raise
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": ca_name,
            "certificate_file_name": ca_file.name,
            "ssl_certificate": ca_file.name,
            "cert_format": "PEM",
        }
    }
    client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)


def run(args: argparse.Namespace) -> int:
    if not args.console or not args.user:
        raise SystemExit("Console URL and user are required.")

    stamp = args.stamp or _timestamp()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    key_passphrase = keygen._get_passphrase(args)
    key_name = keygen._build_key_name(args.cn, stamp)
    key_path = out_dir / key_name
    keygen._generate_key(args.kind, key_path, key_passphrase)
    print(f"Wrote key: {key_path}")

    csr_args = argparse.Namespace(
        key_file=str(key_path),
        cn=args.cn,
        out=args.out,
        stamp=stamp,
        san=args.san,
        subject=args.subject,
        country=args.country,
        state=args.state,
        organization=args.organization,
        org_unit=args.organizational_unit,
        locality=args.locality,
        email=args.email,
        passphrase=key_passphrase,
        keychain_service=args.keychain_service,
        keychain_username=args.keychain_username,
        save_passphrase=args.save_passphrase,
    )
    csr_create.run(csr_args)
    csr_path = out_dir / f"{args.cn}-{stamp}.csr"
    csr_pem = csr_path.read_text(encoding="utf-8")

    ca_dir = out_dir / "selfsigned"
    adapter = SelfSignedAdapter(
        SelfSignedConfig(
            ca_dir=str(ca_dir),
            passphrase=_selfsign_passphrase(args),
            ca_days=args.ca_days,
            leaf_days=args.leaf_days,
        )
    )
    submit = adapter.submit_csr(csr_pem)
    leaf_pem = adapter.collect_certificate(submit.request_id)
    chain_pem = adapter.collect_chain(submit.request_id)

    cert_path = out_dir / f"{args.cn}-{stamp}.crt"
    chain_path = out_dir / f"{args.cn}-{stamp}.chain.pem"
    _write_text(cert_path, leaf_pem)
    _write_text(chain_path, chain_pem)
    print(f"Wrote certificate: {cert_path}")
    print(f"Wrote chain: {chain_path}")

    ca_pem = _extract_chain_cas(chain_pem)
    ca_file = None
    if ca_pem:
        ca_file = out_dir / f"{args.cn}-{stamp}.ca.pem"
        _write_text(ca_file, ca_pem)
        print(f"Wrote CA certs: {ca_file}")

    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    client = NitroConsoleClient(base=args.console, verify=verify, timeout=args.timeout)
    password = _load_console_password(args)
    client.login(args.user, password)

    basicauth_changed = False
    try:
        basicauth_changed = _maybe_enable_basicauth(client)

        certkeypair_name = args.certkeypair_name or _normalize_name(args.cn)
        _upload_console_certkey(
            client,
            certkeypair_name=certkeypair_name,
            cert_file=cert_path,
            key_file=key_path,
            passphrase=key_passphrase,
            console_user=args.user,
            console_password=password,
        )
        print(f"Uploaded certkeypair to Console: {certkeypair_name}")

        ca_certkey_name = None
        if ca_file:
            ca_certkey_name = f"{certkeypair_name}_ca"
            _upload_console_ca(
                client,
                ca_name=ca_certkey_name,
                ca_file=ca_file,
                console_user=args.user,
                console_password=password,
            )
            print(f"Uploaded CA certkey to Console: {ca_certkey_name}")

        deploy_args = [
            "--console",
            args.console,
            "--user",
            args.user,
            "--certkeypair",
            certkeypair_name,
        ]
        if args.insecure:
            deploy_args.append("--insecure")
        if args.ca_bundle:
            deploy_args.extend(["--ca-bundle", args.ca_bundle])
        for ip in args.adc_ip or []:
            deploy_args.extend(["--adc-ip", ip])
        if args.list_adc_menu:
            deploy_args.extend(["--list-adc", "menu"])
        if ca_certkey_name and ca_file:
            deploy_args.extend(["--ca-certkey", ca_certkey_name, "--ca-cert-file", str(ca_file)])

        deploy_ns = nsconsole_deploy.build_arg_parser().parse_args(deploy_args)
        return nsconsole_deploy.run(deploy_ns)
    finally:
        _restore_basicauth(client, changed=basicauth_changed)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Self-sign and deploy a cert to Console and ADCs.")
    parser.add_argument("--cn", required=True, help="Common Name (CN) for key/CSR filenames")
    parser.add_argument("--kind", choices=["rsa", "ecdsa"], required=True, help="Key type")
    parser.add_argument("--out", default="./out", help="Output directory for key/CSR files")
    parser.add_argument("--stamp", help="Timestamp for filenames (default: now)")
    parser.add_argument("--san", help="SAN list (comma-separated)")
    parser.add_argument("--subject", help="Subject string override for CSR")
    parser.add_argument("--country", default="US", help="CountryName (C)")
    parser.add_argument("--state", default="Alabama", help="StateName (ST)")
    parser.add_argument("--organization", default="Regions Financial Corporation", help="OrganizationName (O)")
    parser.add_argument("--organizational-unit", default="ECommerce", help="OrganizationalUnitName (OU)")
    parser.add_argument("--locality", default="Birmingham", help="LocalityName (L)")
    parser.add_argument("--email", default="was@regions.com", help="EmailAddress")
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
    parser.add_argument("--selfsign-passphrase", help="Self-signed CA passphrase")
    parser.add_argument("--ca-days", type=int, default=60, help="Self-signed CA validity in days")
    parser.add_argument("--leaf-days", type=int, default=59, help="Self-signed leaf validity in days")
    parser.add_argument("--certkeypair-name", help="Override Console certkeypair name")
    parser.add_argument("--console", help="Console base URL, e.g. https://console")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--console-password", help="Console password (or set CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    parser.add_argument("--adc-ip", action="append", help="Target ADC IP (repeatable)")
    parser.add_argument("--list-adc-menu", action="store_true", help="Select ADCs from Console menu")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
