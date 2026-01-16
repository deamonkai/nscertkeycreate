#!/usr/bin/env python3
"""Submit a CSR to a CA adapter and optionally collect the certificate."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import time
import subprocess
from pathlib import Path
from typing import Optional

from certctl.ca.adcs import AdcsAdapter, AdcsConfig
from certctl.secretstore import delete_secret, get_secret, is_available, set_secret
from certctl.ca.sectigo import SectigoAdapter, SectigoConfig


def _load_csr(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def _build_sectigo(args: argparse.Namespace) -> SectigoAdapter:
    base_url = args.sectigo_base_url or os.environ.get("SECTIGO_BASE_URL", "https://cert-manager.com")
    login = args.sectigo_login or os.environ.get("SECTIGO_LOGIN")
    password = args.sectigo_password or os.environ.get("SECTIGO_PASSWORD")
    customer_uri = args.sectigo_customer_uri or os.environ.get("SECTIGO_CUSTOMER_URI")
    org_id = args.sectigo_org_id or os.environ.get("SECTIGO_ORG_ID")
    cert_type = args.sectigo_cert_type or os.environ.get("SECTIGO_CERT_TYPE")
    term_days = args.sectigo_term or os.environ.get("SECTIGO_TERM")

    if not login:
        login = input("Sectigo login: ")
    if not password:
        password = getpass.getpass("Sectigo password: ")
    if not customer_uri:
        customer_uri = input("Sectigo customerUri: ")
    if not org_id or not cert_type or not term_days:
        raise SystemExit("Sectigo org-id, cert-type, and term are required.")

    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    config = SectigoConfig(
        base_url=base_url,
        login=login,
        password=password,
        customer_uri=customer_uri,
        org_id=int(org_id),
        cert_type=int(cert_type),
        term_days=int(term_days),
        verify=verify,
    )
    return SectigoAdapter(config)


def _normalize_sans(values: Optional[str]) -> list[str]:
    if not values:
        return []
    parts = [part.strip() for part in values.split(",") if part.strip()]
    return parts


def _choose_ca(cn: Optional[str], sans: Optional[str]) -> str:
    tokens = []
    if cn:
        tokens.append(cn)
    tokens.extend(_normalize_sans(sans))
    for token in tokens:
        lowered = token.lower()
        if "rgbk.com" in lowered:
            return "adcs"
    return "sectigo"


def _parse_csr_subject_and_sans(csr_path: str) -> tuple[Optional[str], Optional[str]]:
    proc = subprocess.run(
        ["openssl", "req", "-in", csr_path, "-noout", "-text"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True,
    )
    text = proc.stdout
    cn = None
    sans = []
    saw_san = False
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("Subject:"):
            parts = line.split("Subject:", 1)[1].split(",")
            for part in parts:
                part = part.strip()
                if part.startswith("CN="):
                    cn = part.split("=", 1)[1].strip()
        if "Subject Alternative Name" in line:
            saw_san = True
            continue
        if saw_san:
            if line.startswith("DNS:") or line.startswith("IP Address:"):
                entries = [e.strip() for e in line.split(",")]
                for entry in entries:
                    if entry.startswith("DNS:"):
                        sans.append(f"DNS:{entry[4:]}")
                    elif entry.startswith("IP Address:"):
                        sans.append(f"IP:{entry.split(':', 1)[1]}")
            else:
                saw_san = False
    sans_value = ", ".join(sans) if sans else None
    return cn, sans_value


def _load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _adcs_key(service: str, field: str) -> str:
    return f"{service}:{field}"


def _load_adcs_keychain(service: str) -> dict:
    if not is_available():
        return {}
    return {
        "base_url": get_secret(service, _adcs_key(service, "base_url")),
        "username": get_secret(service, _adcs_key(service, "username")),
        "password": get_secret(service, _adcs_key(service, "password")),
        "template": get_secret(service, _adcs_key(service, "template")),
    }


def _save_adcs_keychain(service: str, values: dict) -> None:
    if not is_available():
        return
    for field in ("base_url", "username", "password", "template"):
        value = values.get(field)
        if value:
            set_secret(service, _adcs_key(service, field), str(value))


def _reset_adcs_keychain(service: str) -> None:
    if not is_available():
        return
    for field in ("base_url", "username", "password", "template"):
        delete_secret(service, _adcs_key(service, field))


def _build_adcs(args: argparse.Namespace) -> AdcsAdapter:
    cfg = {}
    if args.adcs_config:
        cfg = _load_json(args.adcs_config)

    service = args.adcs_keychain_service or "certctl.adcs"
    if args.adcs_reset_keychain:
        _reset_adcs_keychain(service)

    keychain_values = _load_adcs_keychain(service)

    base_url = (
        args.adcs_base_url
        or keychain_values.get("base_url")
        or cfg.get("base_url")
        or os.environ.get("ADCS_BASE_URL")
    )
    username = (
        args.adcs_username
        or keychain_values.get("username")
        or cfg.get("username")
        or os.environ.get("ADCS_USERNAME")
    )
    password = (
        args.adcs_password
        or keychain_values.get("password")
        or cfg.get("password")
        or os.environ.get("ADCS_PASSWORD")
    )
    template = (
        args.adcs_template
        or keychain_values.get("template")
        or cfg.get("template")
        or os.environ.get("ADCS_TEMPLATE")
    )

    if not base_url:
        raise SystemExit("ADCS base URL is required.")
    if not username:
        username = input("ADCS username: ")
    if not password:
        password = getpass.getpass("ADCS password: ")

    verify: object
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    if is_available() and (args.adcs_save_keychain or (not args.adcs_config and not keychain_values.get("password"))):
        _save_adcs_keychain(
            service,
            {
                "base_url": base_url,
                "username": username,
                "password": password,
                "template": template or "",
            },
        )

    return AdcsAdapter(
        AdcsConfig(
            base_url=base_url,
            username=username,
            password=password,
            template=template,
            verify=verify,
        )
    )


def run(args: argparse.Namespace) -> int:
    csr_pem = _load_csr(args.csr)

    ca = args.ca
    if not ca and args.auto_ca:
        cn = args.cn
        san = args.san
        if not cn and not san:
            cn, san = _parse_csr_subject_and_sans(args.csr)
        ca = _choose_ca(cn, san)
    if not ca:
        raise SystemExit("--ca is required unless --auto-ca is set.")

    if ca == "sectigo":
        adapter = _build_sectigo(args)
    else:
        adapter = _build_adcs(args)

    submit = adapter.submit_csr(csr_pem, subj_alt_names=args.sectigo_sans)
    print(json.dumps({"ca": submit.ca, "request_id": submit.request_id}, indent=2))

    if not args.wait:
        return 0

    deadline = time.time() + args.timeout
    while True:
        status = adapter.poll_status(submit.request_id)
        if status.status.lower() == "issued":
            cert_pem = adapter.collect_certificate(submit.request_id, format_name=args.collect_format)
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(cert_pem, encoding="utf-8")
            print(f"Wrote certificate: {out_path}")
            if args.adcs_include_chain and hasattr(adapter, "collect_chain"):
                chain_out = Path(args.adcs_chain_out)
                chain_out.parent.mkdir(parents=True, exist_ok=True)
                chain_pem = adapter.collect_chain(submit.request_id)  # type: ignore[attr-defined]
                chain_out.write_text(chain_pem, encoding="utf-8")
                print(f"Wrote certificate chain: {chain_out}")
            return 0

        if time.time() > deadline:
            raise SystemExit(f"Timed out waiting for issuance; last status: {status.status}")
        print(f"Status: {status.status}; waiting {args.interval}s...")
        time.sleep(args.interval)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Submit a CSR to a CA and collect the certificate.")
    parser.add_argument("--ca", choices=["sectigo", "adcs"], help="CA adapter to use")
    parser.add_argument("--auto-ca", action="store_true", default=False, help="Auto-select CA based on CN/SANs")
    parser.add_argument("--cn", help="Common Name for auto CA selection")
    parser.add_argument("--san", help="SAN list for auto CA selection (comma-separated)")
    parser.add_argument("--csr", required=True, help="Path to CSR PEM file")
    parser.add_argument("--out", default="./out/cert.pem", help="Output certificate path")
    parser.add_argument("--wait", action="store_true", default=False, help="Wait for issuance and collect")
    parser.add_argument("--interval", type=int, default=30, help="Polling interval in seconds")
    parser.add_argument("--timeout", type=int, default=1800, help="Polling timeout in seconds")
    parser.add_argument("--collect-format", default="pem", help="Sectigo collect format")
    parser.add_argument("--sectigo-base-url", help="Sectigo API base URL")
    parser.add_argument("--sectigo-login", help="Sectigo login")
    parser.add_argument("--sectigo-password", help="Sectigo password")
    parser.add_argument("--sectigo-customer-uri", help="Sectigo customerUri")
    parser.add_argument("--sectigo-org-id", type=int, help="Sectigo orgId")
    parser.add_argument("--sectigo-cert-type", type=int, help="Sectigo certType profile ID")
    parser.add_argument("--sectigo-term", type=int, help="Sectigo term in days")
    parser.add_argument("--sectigo-sans", help="Comma-separated SANs for Sectigo")
    parser.add_argument("--adcs-config", help="Path to ADCS JSON config")
    parser.add_argument("--adcs-base-url", help="ADCS base URL, e.g. https://adcs/certsrv")
    parser.add_argument("--adcs-username", help="ADCS username")
    parser.add_argument("--adcs-password", help="ADCS password")
    parser.add_argument("--adcs-template", help="ADCS certificate template (optional)")
    parser.add_argument("--adcs-keychain-service", help="Keychain service name for ADCS creds")
    parser.add_argument(
        "--adcs-save-keychain",
        action="store_true",
        default=False,
        help="Save ADCS creds to keychain when prompted",
    )
    parser.add_argument(
        "--adcs-reset-keychain",
        action="store_true",
        default=False,
        help="Reset (delete) ADCS creds stored in keychain",
    )
    parser.add_argument(
        "--adcs-include-chain",
        action="store_true",
        default=False,
        help="Collect certificate chain (ADCS only)",
    )
    parser.add_argument(
        "--adcs-chain-out",
        default="./out/chain.pem",
        help="Output path for ADCS chain PEM",
    )
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for TLS verification")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
