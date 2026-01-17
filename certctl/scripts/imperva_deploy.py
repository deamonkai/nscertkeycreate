#!/usr/bin/env python3
"""Deploy a Console certificate to Imperva WAF using a combined PEM."""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from certctl.console import NitroConsoleClient


def _parse_cn(subject: str) -> Optional[str]:
    if not subject:
        return None
    match = re.search(r"(?:^|[,/\\s])CN\\s*=\\s*([^,/]+)", subject)
    if match:
        return match.group(1).strip()
    return None


def _normalize_certkey_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", name or "").strip("_")


def _load_password(username: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {username}@{console}: ")


def _get_key_passphrase(provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_KEY_PASSPHRASE")
    if env_pw:
        return env_pw
    return getpass.getpass("Key passphrase (AES-256): ")


def _list_certkeys(client: NitroConsoleClient) -> List[Dict[str, Any]]:
    payload = client.get_json("/nitro/v2/config/ns_ssl_certkey", params={"pagesize": "200"})
    items = payload.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return [items]
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return []


def _find_certkey(client: NitroConsoleClient, name: str) -> Dict[str, Any]:
    payload = client.get_json(
        "/nitro/v2/config/ns_ssl_certkey",
        params={"filter": f"certkeypair_name:{name}"},
    )
    items = payload.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return items
    if isinstance(items, list) and items:
        return items[0]
    normalized = _normalize_certkey_name(name)
    if normalized and normalized != name:
        payload = client.get_json(
            "/nitro/v2/config/ns_ssl_certkey",
            params={"filter": f"certkeypair_name:{normalized}"},
        )
        items = payload.get("ns_ssl_certkey", [])
        if isinstance(items, dict):
            return items
        if isinstance(items, list) and items:
            return items[0]
    candidates = _list_certkeys(client)
    matches = []
    for cert in candidates:
        subject = str(cert.get("subject") or cert.get("certificate_dn") or "")
        cn = _parse_cn(subject)
        if cn and cn.lower() == name.lower():
            matches.append(cert)
    if len(matches) == 1:
        return matches[0]
    if matches:
        names = ", ".join(sorted({m.get("certkeypair_name", "unknown") for m in matches}))
        raise SystemExit(f"Multiple certkeypairs match CN {name}: {names}")
    raise SystemExit(f"Certkeypair not found: {name}")


def _first_value(cert: Dict[str, Any], keys: List[str]) -> Optional[str]:
    for key in keys:
        value = cert.get(key)
        if value:
            return str(value)
    return None


def _extract_chain_files(cert: Dict[str, Any]) -> List[str]:
    chain = cert.get("certkeychain") or []
    if isinstance(chain, dict):
        chain = [chain]
    names = []
    for entry in chain:
        if not isinstance(entry, dict):
            continue
        name = entry.get("certificate_file_name") or entry.get("cert_name") or entry.get("linked_to")
        if name and name not in names:
            names.append(str(name))
    return names


def _auth_type(cert: Dict[str, Any]) -> str:
    algo = str(cert.get("public_key_algorithm") or cert.get("signature_algorithm") or "").upper()
    if "EC" in algo or "ECDSA" in algo:
        return "ECC"
    return "RSA"


def _read_pem(content: bytes) -> str:
    text = content.decode("utf-8", errors="replace")
    return text if text.endswith("\n") else text + "\n"


def _b64(content: str) -> str:
    return base64.b64encode(content.encode("utf-8")).decode("ascii")


def run(args: argparse.Namespace) -> int:
    if not args.console or not args.user:
        raise SystemExit("Console URL and user are required.")
    if not args.site_id:
        raise SystemExit("Imperva site id is required (--site-id).")

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

    cert = _find_certkey(client, args.certkeypair)
    cert_file = _first_value(cert, ["certificate_file_name", "ssl_certificate", "file_name"])
    key_file = _first_value(cert, ["key_file_name", "ssl_key", "key_name"])
    if not cert_file:
        raise SystemExit("Console certkey did not include certificate_file_name.")
    if not key_file:
        raise SystemExit("Console certkey did not include key_file_name.")

    chain_files = _extract_chain_files(cert)
    print(f"Using certificate: {cert_file}")
    print(f"Using key: {key_file}")
    if chain_files:
        print(f"Using CA chain files: {', '.join(chain_files)}")
    else:
        print("No CA chain metadata found; Imperva upload will include only the leaf cert.")

    cert_pem = _read_pem(client.download_file("ns_ssl_cert", cert_file))
    key_pem = _read_pem(client.download_file("ns_ssl_key", key_file))
    chain_pems = []
    for name in chain_files:
        chain_pems.append(_read_pem(client.download_file("ns_ssl_cert", name)))

    full_chain = cert_pem + "".join(chain_pems)
    key_passphrase = _get_key_passphrase(args.key_passphrase)

    api_id = args.api_id or os.environ.get("IMPERVA_API_ID")
    api_key = args.api_key or os.environ.get("IMPERVA_API_KEY")
    if not api_id:
        api_id = input("Imperva API Id: ")
    if not api_key:
        api_key = getpass.getpass("Imperva API Key: ")

    payload = {
        "certificate": _b64(full_chain),
        "private_key": _b64(key_pem),
        "auth_type": _auth_type(cert),
    }
    if key_passphrase:
        payload["passphrase"] = key_passphrase

    base_url = args.imperva_base.rstrip("/")
    url = f"{base_url}/api/prov/v2/sites/{args.site_id}/customCertificate"
    headers = {
        "x-API-Id": api_id,
        "x-API-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    resp = requests.put(url, headers=headers, json=payload, timeout=args.imperva_timeout)
    if resp.status_code >= 400:
        raise SystemExit(f"Imperva upload failed ({resp.status_code}): {resp.text}")
    try:
        data = resp.json()
    except Exception:
        data = {"raw": resp.text}
    print(json.dumps(data, indent=2))
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Deploy a Console certificate to Imperva (combined PEM is built automatically)."
    )
    parser.add_argument("--certkeypair", required=True, help="Console certkeypair name or CN")
    parser.add_argument("--console", help="Console base URL, e.g. https://console")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--password", help="Console password (or set CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification for Console")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for Console TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="Console HTTP timeout in seconds")
    parser.add_argument("--key-passphrase", help="Passphrase for the private key (or CERTCTL_KEY_PASSPHRASE)")
    parser.add_argument("--imperva-base", default="https://my.impervaservices.com", help="Imperva API base URL")
    parser.add_argument("--imperva-timeout", type=int, default=60, help="Imperva HTTP timeout in seconds")
    parser.add_argument("--site-id", required=True, help="Imperva site ID")
    parser.add_argument("--api-id", help="Imperva API ID (or IMPERVA_API_ID)")
    parser.add_argument("--api-key", help="Imperva API key (or IMPERVA_API_KEY)")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
