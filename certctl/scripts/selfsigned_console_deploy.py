#!/usr/bin/env python3
"""Generate a self-signed cert and deploy it to Console and ADCs."""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
import shutil
import subprocess
import time
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

from certctl.ca.selfsigned import SelfSignedAdapter, SelfSignedConfig
from certctl.console import NitroConsoleClient, NitroError
from certctl.scripts import csr_create, keygen, nsconsole_deploy

_DEBUG = False


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


def _set_debug(enabled: bool) -> None:
    global _DEBUG
    _DEBUG = bool(enabled)


def _redact_payload(value: Any) -> Any:
    if isinstance(value, dict):
        redacted = {}
        for key, item in value.items():
            if key in {"password", "key_data", "certificate_data", "token", "secret"}:
                redacted[key] = "<redacted>"
                continue
            if key == "cert_data" and isinstance(item, dict):
                redacted[key] = {**item, "file_data": "<redacted>"} if "file_data" in item else item
                continue
            if key == "certchain_data" and isinstance(item, list):
                redacted[key] = [
                    {**entry, "file_data": "<redacted>"} if isinstance(entry, dict) and "file_data" in entry else entry
                    for entry in item
                ]
                continue
            redacted[key] = _redact_payload(item)
        return redacted
    if isinstance(value, list):
        return [_redact_payload(item) for item in value]
    return value


def _debug_payload(label: str, payload: Dict[str, Any]) -> None:
    if not _DEBUG:
        return
    print(f"[debug] {label}:")
    print(json.dumps(_redact_payload(payload), indent=2, sort_keys=True))


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


def _b64_clean(value: str) -> str:
    encoded = base64.b64encode(value.encode("utf-8")).decode("ascii")
    return encoded.rstrip("%")


def _pem_body_base64(pem: str) -> str:
    lines = []
    for line in pem.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("-----BEGIN ") or line.startswith("-----END "):
            continue
        lines.append(line)
    return "".join(lines)


def _encode_pem(pem: str, mode: str) -> str:
    if mode == "pem-body":
        return _pem_body_base64(pem)
    if mode == "pem-b64":
        return _b64_clean(pem)
    if mode == "raw-pem":
        return pem
    raise ValueError(f"Unsupported PEM encoding mode: {mode}")


def _store_code_error(response: Dict[str, Any]) -> Optional[str]:
    items = response.get("cert_store")
    if isinstance(items, list) and items:
        store_code = items[0].get("store_code")
    elif isinstance(items, dict):
        store_code = items.get("store_code")
    else:
        return None
    if store_code not in (0, "0", None):
        return str(store_code)
    return None


def _post_cert_store(
    client: NitroConsoleClient,
    payload: Dict[str, Any],
    *,
    basic_user: Optional[str],
    basic_password: Optional[str],
    retry_label: str,
) -> Dict[str, Any]:
    use_header_auth = bool(basic_user and basic_password)
    if use_header_auth:
        _debug_payload(f"cert_store POST ({retry_label}, header auth)", payload)
        response = client.post_json(
            "/nitro/v2/config/cert_store",
            payload,
            headers={"X-NITRO-USER": basic_user, "X-NITRO-PASS": basic_password},
            use_cookie=False,
        )
    else:
        _debug_payload(f"cert_store POST ({retry_label}, cookie auth)", payload)
        response = client.post_json("/nitro/v2/config/cert_store", payload)
    store_code = _store_code_error(response)
    items = response.get("cert_store")
    has_id = False
    if isinstance(items, list) and items and items[0].get("id"):
        has_id = True
    if isinstance(items, dict) and items.get("id"):
        has_id = True
    if (store_code or not has_id) and use_header_auth:
        print(f"[console] cert_store {retry_label} did not return id; retrying with cookie auth.")
        _debug_payload(f"cert_store POST ({retry_label}, cookie auth retry)", payload)
        response = client.post_json("/nitro/v2/config/cert_store", payload)
    return response


def _cert_store_payload(
    *,
    name: str,
    cert_file_name: str,
    cert_pem: str,
    key_file_name: Optional[str],
    key_pem: Optional[str],
    passphrase: Optional[str],
    chain_pem: Optional[str],
    cert_data_mode: str,
    chain_data_mode: str,
    key_data_mode: str,
) -> Dict[str, Any]:
    cert_data = _encode_pem(cert_pem, cert_data_mode)
    payload: Dict[str, Any] = {
        "cert_store": {
            "name": name,
            "cert_data": {"file_name": cert_file_name, "file_data": cert_data},
        }
    }
    if key_pem and passphrase is not None:
        if key_file_name:
            payload["cert_store"]["key_file"] = key_file_name
        payload["cert_store"]["key_data"] = _encode_pem(key_pem, key_data_mode)
        payload["cert_store"]["password"] = passphrase
    if chain_pem:
        payload["cert_store"]["certchain_data"] = [
            {
                "file_name": "chain.pem",
                "file_data": _encode_pem(chain_pem, chain_data_mode),
            }
        ]
    return payload


def _normalize_subject(value: str) -> str:
    cleaned = value.replace("&apos;", "'")
    cleaned = re.sub(r"\\s+", "", cleaned)
    return cleaned.lower()


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise SystemExit("OpenSSL not found in PATH.")
    return path


def _split_pem_certs(pem: str) -> List[str]:
    return re.findall(
        r"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----",
        pem,
        flags=re.DOTALL,
    )


def _extract_cn(subject: str) -> Optional[str]:
    if not subject:
        return None
    match = re.search(r"CN\\s*=\\s*([^,/]+)", subject)
    if match:
        return match.group(1).strip()
    return None


def _cert_cn_from_pem(pem: str) -> Optional[str]:
    openssl = _require_openssl()
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as handle:
        handle.write(pem)
        tmp_path = handle.name
    try:
        proc = subprocess.run(
            [openssl, "x509", "-noout", "-subject", "-nameopt", "RFC2253", "-in", tmp_path],
            check=True,
            capture_output=True,
            text=True,
        )
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    subject_line = proc.stdout.strip()
    subject = subject_line.replace("subject=", "", 1).strip()
    cn = _extract_cn(subject)
    if cn:
        return cn
    match = re.search(r"CN\\s*=\\s*([^,/]+)", subject_line)
    if match:
        return match.group(1).strip()
    return None


def _cert_subject_serial_from_pem(pem: str) -> Dict[str, str]:
    openssl = _require_openssl()
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as handle:
        handle.write(pem)
        tmp_path = handle.name
    try:
        proc = subprocess.run(
            [openssl, "x509", "-noout", "-subject", "-serial", "-in", tmp_path],
            check=True,
            capture_output=True,
            text=True,
        )
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    subject = ""
    serial = ""
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("subject="):
            subject = line.replace("subject=", "", 1).strip()
        elif line.startswith("serial="):
            serial = line.replace("serial=", "", 1).strip()
    return {"subject": subject, "serial": serial}


def _cert_store_matches(entry: Dict[str, Any], cert_pem: str) -> bool:
    meta = _cert_subject_serial_from_pem(cert_pem)
    entry_subject = str(entry.get("subject") or "")
    entry_serial = str(entry.get("serial_number") or "")
    if _DEBUG:
        print(
            "[debug] cert_store compare:"
            f" entry_subject={entry_subject!r}"
            f" entry_serial={entry_serial!r}"
            f" new_subject={meta.get('subject', '')!r}"
            f" new_serial={meta.get('serial', '')!r}"
        )
    if not entry_subject or not entry_serial:
        return False
    if _normalize_subject(entry_subject) != _normalize_subject(meta.get("subject", "")):
        return False
    return entry_serial.lower() == meta.get("serial", "").lower()

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


def _upload_console_cert_store(
    client: NitroConsoleClient,
    *,
    certkeypair_name: str,
    cert_file: Path,
    key_file: Path,
    passphrase: str,
    chain_pem: Optional[str] = None,
    basic_user: Optional[str] = None,
    basic_password: Optional[str] = None,
) -> Dict[str, Any]:
    cert_pem = _read_text(cert_file)
    key_pem = _read_text(key_file)
    store_cert_name = f"{certkeypair_name}.pem"
    store_key_name = certkeypair_name
    existing = _find_cert_store_entry(client, name=certkeypair_name, retries=1, wait_seconds=0)
    if existing and existing.get("id"):
        if _cert_store_matches(existing, cert_pem):
            print(f"[console] cert_store entry already matches {certkeypair_name}; skipping update.")
            return {"cert_store": [existing]}
        print(f"[console] cert_store entry exists; updating {certkeypair_name}.")
        try:
            response = _update_cert_store(
                client,
                entry_id=str(existing["id"]),
                name=certkeypair_name,
                cert_file_name=store_cert_name,
                cert_pem=cert_pem,
                key_file_name=store_key_name,
                key_pem=key_pem,
                passphrase=passphrase,
                chain_pem=chain_pem,
                cert_data_mode="pem-b64",
                chain_data_mode="pem-b64",
                key_data_mode="pem-b64",
            )
            return response
        except NitroError as exc:
            if "no updates have been applied" in str(exc.message).lower():
                print(f"[console] cert_store update not needed for {certkeypair_name}.")
                return {"cert_store": [existing]}
            raise
    print(f"[console] cert_store entry not found; creating {certkeypair_name}.")
    encode_modes = ("pem-b64",)
    try:
        response: Dict[str, Any] = {}
        for idx, mode in enumerate(encode_modes, start=1):
            payload = _cert_store_payload(
                name=certkeypair_name,
                cert_file_name=store_cert_name,
                cert_pem=cert_pem,
                key_file_name=store_key_name,
                key_pem=key_pem,
                passphrase=passphrase,
                chain_pem=chain_pem,
                cert_data_mode=mode,
                chain_data_mode=mode,
                key_data_mode="pem-b64",
            )
            response = _post_cert_store(
                client,
                payload,
                basic_user=basic_user,
                basic_password=basic_password,
                retry_label=f"upload ({mode})",
            )
            store_code = _store_code_error(response)
            if store_code:
                print(f"[console] cert_store upload returned store_code={store_code} for {certkeypair_name}.")
                print(
                    "[console] cert_store payload sizes:"
                    f" cert_len={len(_encode_pem(cert_pem, mode))}"
                    f" key_len={len(_encode_pem(key_pem, 'pem-b64'))}"
                    f" chain_len={len(_encode_pem(chain_pem, mode)) if chain_pem else 0}"
                )
            items = response.get("cert_store")
            if isinstance(items, list) and items and items[0].get("id"):
                return response
            if isinstance(items, dict) and items.get("id"):
                return response
            if idx < len(encode_modes):
                print("[console] cert_store upload did not return id; retrying with alternate encoding.")
        print(f"[console] cert_store upload response missing id for {certkeypair_name}: {response}")
        return response
    except NitroError as exc:
        message = str(exc.message).lower()
        if exc.status_code == 409 or "already exists" in message:
            print("[console] cert_store entry already exists; reusing existing entry.")
            existing = _find_cert_store_entry(
                client,
                name=certkeypair_name,
                retries=3,
                wait_seconds=2,
            )
            if existing:
                if _cert_store_matches(existing, cert_pem):
                    print(f"[console] cert_store entry already matches {certkeypair_name}; skipping update.")
                    return {"cert_store": [existing]}
                try:
                    response = _update_cert_store(
                        client,
                        entry_id=str(existing["id"]),
                        name=certkeypair_name,
                        cert_file_name=store_cert_name,
                        cert_pem=cert_pem,
                        key_file_name=store_key_name,
                        key_pem=key_pem,
                        passphrase=passphrase,
                        chain_pem=chain_pem,
                        cert_data_mode="pem-b64",
                        chain_data_mode="pem-b64",
                        key_data_mode="pem-b64",
                    )
                    return response
                except NitroError as update_exc:
                    if "no updates have been applied" in str(update_exc.message).lower():
                        print(f"[console] cert_store update not needed for {certkeypair_name}.")
                        return {"cert_store": [existing]}
                    raise
        raise


def _list_cert_store(client: NitroConsoleClient, *, pagesize: int = 200) -> List[Dict[str, Any]]:
    payload = client.get_json("/nitro/v2/config/cert_store", params={"pagesize": str(pagesize)})
    items = payload.get("cert_store") or []
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    if isinstance(items, dict):
        return [items]
    return []


def _summarize_cert_store(items: List[Dict[str, Any]], *, limit: int = 5) -> str:
    fields = ["name", "domain", "subject", "serial_number", "key_file", "created_time", "id"]
    rows = []
    for item in items[:limit]:
        rows.append({k: item.get(k) for k in fields})
    return str(rows)


def _find_cert_store_entry(
    client: NitroConsoleClient,
    *,
    name: str,
    subject: str = "",
    serial: str = "",
    key_file: str = "",
    retries: int = 3,
    wait_seconds: int = 2,
) -> Optional[dict]:
    for attempt in range(1, retries + 1):
        if name:
            payload = client.get_json(
                "/nitro/v2/config/cert_store",
                params={"filter": f"name:{name}", "pagesize": "200"},
            )
            items = payload.get("cert_store") or []
            if isinstance(items, dict):
                items = [items]
            for item in items:
                if isinstance(item, dict) and item.get("name") == name:
                    return item
        if attempt < retries:
            print(f"[console] Waiting {wait_seconds} seconds for cert_store to refresh...")
            time.sleep(wait_seconds)
    return None


def _register_certkey_from_store(
    client: NitroConsoleClient,
    *,
    certkeypair_name: str,
    cert_store_id: str,
    passphrase: Optional[str],
    chain_pem: Optional[str] = None,
    ns_ip_addresses: Optional[List[str]] = None,
) -> None:
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": certkeypair_name,
            "cert_store_id": cert_store_id,
        }
    }
    if passphrase:
        payload["ns_ssl_certkey"]["password"] = passphrase
    if chain_pem:
        payload["ns_ssl_certkey"]["certchain_data"] = [
            {"file_name": "chain.pem", "file_data": _b64_clean(chain_pem)}
        ]
    if ns_ip_addresses:
        payload["ns_ssl_certkey"]["ns_ip_address_arr"] = ns_ip_addresses
    _debug_payload("ns_ssl_certkey POST (from cert_store)", payload)
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)
    except NitroError as exc:
        message = str(exc.message)
        if "not a directory: /var/mps/tenants/root/ns_ssl_certs/" in message:
            raise SystemExit(
                "Console staging path is not a directory: /var/mps/tenants/root/ns_ssl_certs/. "
                "Fix the path on the Console (directory + permissions), then retry."
            ) from exc
        raise


def _register_ca_certkey_inline(
    client: NitroConsoleClient,
    *,
    ca_name: str,
    ca_pem: str,
    ns_ip_addresses: Optional[List[str]] = None,
) -> None:
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": ca_name,
            "certificate_data": ca_pem,
            "cert_format": "PEM",
        }
    }
    if ns_ip_addresses:
        payload["ns_ssl_certkey"]["ns_ip_address_arr"] = ns_ip_addresses
    _debug_payload("ns_ssl_certkey POST (inline CA)", payload)
    client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)


def _find_certkeypair(
    client: NitroConsoleClient,
    name: str,
    *,
    retries: int = 3,
    wait_seconds: int = 2,
) -> Optional[Dict[str, Any]]:
    for attempt in range(1, retries + 1):
        payload = client.get_json("/nitro/v2/config/ns_ssl_certkey", params={"pagesize": "200"})
        items = payload.get("ns_ssl_certkey") or []
        if isinstance(items, dict):
            items = [items]
        for item in items:
            if isinstance(item, dict) and item.get("certkeypair_name") == name:
                return item
        if attempt < retries:
            print(f"[console] Waiting {wait_seconds} seconds for certkeypair to appear...")
            time.sleep(wait_seconds)
    return None


def _upload_ca_cert_store(
    client: NitroConsoleClient,
    *,
    ca_name: str,
    ca_pem: str,
    basic_user: Optional[str] = None,
    basic_password: Optional[str] = None,
) -> Optional[str]:
    existing = _find_cert_store_entry(client, name=ca_name, retries=1, wait_seconds=0)
    if existing and existing.get("id"):
        if _cert_store_matches(existing, ca_pem):
            print(f"[console] CA cert_store entry already matches {ca_name}; skipping update.")
            return str(existing["id"])
        print(f"[console] CA cert_store entry exists; updating {ca_name}.")
        try:
            _update_cert_store(
                client,
                entry_id=str(existing["id"]),
                name=ca_name,
                cert_file_name=f"{ca_name}.pem",
                cert_pem=ca_pem,
                key_file_name=None,
                key_pem=None,
                passphrase=None,
                chain_pem=None,
                cert_data_mode="pem-b64",
                chain_data_mode="pem-b64",
                key_data_mode="pem-b64",
            )
            return str(existing["id"])
        except NitroError as exc:
            if "no updates have been applied" in str(exc.message).lower():
                print(f"[console] CA cert_store update not needed for {ca_name}.")
                return str(existing["id"])
            raise
    print(f"[console] CA cert_store entry not found; creating {ca_name}.")
    try:
        response: Dict[str, Any] = {}
        for idx, mode in enumerate(("pem-b64",), start=1):
            payload = _cert_store_payload(
                name=ca_name,
                cert_file_name=f"{ca_name}.pem",
                cert_pem=ca_pem,
                key_file_name=None,
                key_pem=None,
                passphrase=None,
                chain_pem=None,
                cert_data_mode=mode,
                chain_data_mode=mode,
                key_data_mode="pem-b64",
            )
            response = _post_cert_store(
                client,
                payload,
                basic_user=basic_user,
                basic_password=basic_password,
                retry_label=f"CA upload ({mode})",
            )
            store_code = _store_code_error(response)
            if store_code:
                print(f"[console] CA cert_store upload returned store_code={store_code} for {ca_name}.")
                print(f"[console] CA cert payload size: cert_len={len(_encode_pem(ca_pem, mode))}")
            items = response.get("cert_store")
            if isinstance(items, list) and items and items[0].get("id"):
                return str(items[0]["id"])
            if isinstance(items, dict) and items.get("id"):
                return str(items["id"])
            if idx < 2:
                print("[console] CA cert_store upload did not return id; retrying with alternate encoding.")
    except NitroError as exc:
        message = str(exc.message).lower()
        if exc.status_code == 409 or "already exists" in message:
            entry = _find_cert_store_entry(client, name=ca_name, retries=3, wait_seconds=2)
            if entry and entry.get("id"):
                try:
                    _update_cert_store(
                        client,
                        entry_id=str(entry["id"]),
                        name=ca_name,
                        cert_file_name=f"{ca_name}.pem",
                        cert_pem=ca_pem,
                        key_file_name=None,
                        key_pem=None,
                        passphrase=None,
                        chain_pem=None,
                        cert_data_mode="pem-b64",
                        chain_data_mode="pem-b64",
                        key_data_mode="pem-b64",
                    )
                    return str(entry["id"])
                except NitroError as update_exc:
                    if "no updates have been applied" in str(update_exc.message).lower():
                        print(f"[console] CA cert_store update not needed for {ca_name}.")
                        return str(entry["id"])
                    raise
        print(f"[console] CA cert_store upload failed for {ca_name}: {exc}")
        return None
    print(f"[console] CA cert_store upload response missing id for {ca_name}: {response}")
    entry = _find_cert_store_entry(client, name=ca_name, retries=10, wait_seconds=3)
    if entry and entry.get("id"):
        return str(entry["id"])
    return None


def _update_cert_store(
    client: NitroConsoleClient,
    *,
    entry_id: str,
    name: str,
    cert_file_name: str,
    cert_pem: str,
    key_file_name: Optional[str],
    key_pem: Optional[str],
    passphrase: Optional[str],
    chain_pem: Optional[str],
    cert_data_mode: str,
    chain_data_mode: str,
    key_data_mode: str,
) -> Dict[str, Any]:
    payload = _cert_store_payload(
        name=name,
        cert_file_name=cert_file_name,
        cert_pem=cert_pem,
        key_file_name=key_file_name,
        key_pem=key_pem,
        passphrase=passphrase,
        chain_pem=chain_pem,
        cert_data_mode=cert_data_mode,
        chain_data_mode=chain_data_mode,
        key_data_mode=key_data_mode,
    )
    payload["cert_store"]["id"] = entry_id
    payload["cert_store"]["update_cert_and_key"] = bool(key_pem)
    payload["cert_store"]["update_cert_chain"] = bool(chain_pem)
    _debug_payload("cert_store PUT", payload)
    return client.put_json(f"/nitro/v2/config/cert_store/{entry_id}", payload)


def _trigger_cert_inventory(client: NitroConsoleClient) -> None:
    payload = {"ns_ssl_certkey": {}}
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload, params={"action": "inventory"})
    except NitroError as exc:
        print(f"[console] Inventory trigger failed: {exc}")


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
        _debug_payload("ns_ssl_certkey POST (inline CA)", payload)
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
    _set_debug(args.debug)
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
    selfsign_passphrase = _selfsign_passphrase(args)
    adapter = SelfSignedAdapter(
        SelfSignedConfig(
            ca_dir=str(ca_dir),
            passphrase=selfsign_passphrase,
            ca_days=args.ca_days,
            leaf_days=args.leaf_days,
        )
    )
    submit = adapter.submit_csr(csr_pem)
    leaf_pem = adapter.collect_certificate(submit.request_id)
    chain_pem = adapter.collect_chain(submit.request_id)
    ca_cn = adapter.config.rsa_cn if args.kind == "rsa" else adapter.config.ecdsa_cn

    cert_path = out_dir / f"{args.cn}-{stamp}.crt"
    chain_path = out_dir / f"{args.cn}-{stamp}.chain.pem"
    _write_text(cert_path, leaf_pem)
    _write_text(chain_path, chain_pem)
    print(f"Wrote certificate: {cert_path}")
    print(f"Wrote chain: {chain_path}")

    ca_pem = _extract_chain_cas(chain_pem)
    ca_file = None
    ca_blocks: List[str] = []
    if ca_pem:
        ca_file = out_dir / f"{args.cn}-{stamp}.ca.pem"
        _write_text(ca_file, ca_pem)
        print(f"Wrote CA certs: {ca_file}")
        ca_blocks = _split_pem_certs(ca_pem)

    if args.dry_run:
        _set_debug(True)
        if args.list_adc_menu:
            raise SystemExit("--list-adc-menu is not supported with --dry-run. Use --adc-ip instead.")
        certkeypair_name = args.certkeypair_name or _normalize_name(args.cn)
        print("[dry-run] Console cert_store payloads:")
        if ca_blocks:
            for ca_block in ca_blocks:
                ca_block_cn = _cert_cn_from_pem(ca_block) or ca_cn or "Root_CA"
                ca_name = _normalize_name(ca_block_cn)
                ca_payload = _cert_store_payload(
                    name=ca_name,
                    cert_file_name=f"{ca_name}.pem",
                    cert_pem=ca_block,
                    key_file_name=None,
                    key_pem=None,
                    passphrase=None,
                    chain_pem=None,
                    cert_data_mode="pem-b64",
                    chain_data_mode="pem-b64",
                    key_data_mode="pem-b64",
                )
                _debug_payload(f"cert_store POST (CA {ca_name})", ca_payload)
        server_payload = _cert_store_payload(
            name=certkeypair_name,
            cert_file_name=cert_path.name,
            cert_pem=leaf_pem,
            key_file_name=key_path.name,
            key_pem=key_path.read_text(encoding="utf-8"),
            passphrase=key_passphrase,
            chain_pem=None,
            cert_data_mode="pem-b64",
            chain_data_mode="pem-b64",
            key_data_mode="pem-b64",
        )
        _debug_payload(f"cert_store POST (server {certkeypair_name})", server_payload)
        adc_ips = args.adc_ip or []
        certkey_payload = {
            "ns_ssl_certkey": {
                "certkeypair_name": certkeypair_name,
                "cert_store_id": "<cert_store_id>",
            }
        }
        if key_passphrase:
            certkey_payload["ns_ssl_certkey"]["password"] = "<key-passphrase>"
        if adc_ips:
            certkey_payload["ns_ssl_certkey"]["ns_ip_address_arr"] = adc_ips
        _debug_payload("ns_ssl_certkey POST (from cert_store)", certkey_payload)
        return 0

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

    selected_adcs: List[str] = []
    if args.list_adc_menu:
        devices = nsconsole_deploy._list_managed_devices(client, primary_only=True)
        selected_adcs = nsconsole_deploy._select_adc_menu(devices)
        if not selected_adcs:
            raise SystemExit("No ADCs selected.")
        args.adc_ip = selected_adcs
        args.list_adc_menu = False

    basicauth_changed = False
    try:
        basicauth_changed = _maybe_enable_basicauth(client)

        certkeypair_name = args.certkeypair_name or _normalize_name(args.cn)
        ca_certkey_name = None
        ca_certkey_names: List[str] = []

        if ca_file and ca_blocks:
            for ca_block in ca_blocks:
                ca_block_cn = _cert_cn_from_pem(ca_block) or ca_cn or "Root_CA"
                ca_name = _normalize_name(ca_block_cn)
                ca_store_id = _upload_ca_cert_store(
                    client,
                    ca_name=ca_name,
                    ca_pem=ca_block,
                    basic_user=args.user,
                    basic_password=password,
                )
                if not ca_store_id:
                    items = _list_cert_store(client)
                    if items:
                        print(f"[console] cert_store sample: {_summarize_cert_store(items)}")
                    raise SystemExit(f"CA cert_store entry not created for {ca_name}.")
                try:
                    _register_certkey_from_store(
                        client,
                        certkeypair_name=ca_name,
                        cert_store_id=ca_store_id,
                        passphrase=None,
                        chain_pem=None,
                        ns_ip_addresses=selected_adcs or args.adc_ip,
                    )
                except NitroError as exc:
                    raise SystemExit(f"[console] CA certkey registration failed for {ca_name}: {exc}") from exc
                ca_certkey_names.append(ca_name)
                ca_certkey_name = ca_name
                print(f"Registered CA certkey from cert_store: {ca_name}")

        print("[console] Uploading server cert/key to cert_store.")
        cert_meta = _cert_subject_serial_from_pem(leaf_pem)
        response = _upload_console_cert_store(
            client,
            certkeypair_name=certkeypair_name,
            cert_file=cert_path,
            key_file=key_path,
            passphrase=key_passphrase,
            chain_pem=None,
            basic_user=args.user,
            basic_password=password,
        )
        print(f"Uploaded cert to Console cert_store: {certkeypair_name}")
        cert_store = None
        if isinstance(response, dict):
            items = response.get("cert_store")
            if isinstance(items, list) and items:
                cert_store = items[0]
            elif isinstance(items, dict):
                cert_store = items
        if not cert_store or not cert_store.get("id"):
            cert_store = _find_cert_store_entry(
                client,
                name=certkeypair_name,
                retries=20,
                wait_seconds=5,
            )
        if not cert_store or not cert_store.get("id"):
            items = _list_cert_store(client)
            print("[console] cert_store entry not found after upload; skipping certkey registration.")
            if items:
                print(f"[console] cert_store sample: {_summarize_cert_store(items)}")
            raise SystemExit(f"cert_store entry not found for {certkeypair_name}.")
        _register_certkey_from_store(
            client,
            certkeypair_name=certkeypair_name,
            cert_store_id=str(cert_store["id"]),
            passphrase=key_passphrase,
            chain_pem=ca_pem,
            ns_ip_addresses=selected_adcs or args.adc_ip,
        )
        print(f"Registered certkeypair from cert_store: {certkeypair_name}")
        if not _find_certkeypair(client, certkeypair_name, retries=3, wait_seconds=2):
            _trigger_cert_inventory(client)
            if not _find_certkeypair(client, certkeypair_name, retries=6, wait_seconds=3):
                raise SystemExit(f"Certkeypair not found after cert_store upload: {certkeypair_name}")

        deploy_args = [
            "--console",
            args.console,
            "--user",
            args.user,
            "--certkeypair",
            certkeypair_name,
        ]
        deploy_args += ["--sync", "--sync-wait", "10"]
        if args.insecure:
            deploy_args.append("--insecure")
        if args.ca_bundle:
            deploy_args.extend(["--ca-bundle", args.ca_bundle])
        for ip in args.adc_ip or []:
            deploy_args.extend(["--adc-ip", ip])
        if args.list_adc_menu:
            deploy_args.extend(["--list-adc", "menu"])
        if args.debug:
            deploy_args.append("--debug")
        if ca_certkey_names:
            for name in ca_certkey_names:
                deploy_args.extend(["--ca-certkey", name])
        elif ca_certkey_name and ca_file:
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
    parser.add_argument("--debug", action="store_true", help="Enable debug logging and payload output")
    parser.add_argument("--dry-run", action="store_true", help="Print payloads without API calls")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
