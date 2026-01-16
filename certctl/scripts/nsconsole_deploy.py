#!/usr/bin/env python3
"""Deploy a Console certkey to ADCs and link CA certs."""

from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from certctl.console import NitroConsoleClient, NitroError


def _load_config(path: str) -> Dict[str, Any]:
    config_path = Path(path).expanduser()
    raw = config_path.read_text(encoding="utf-8")
    if config_path.suffix.lower() in (".yaml", ".yml"):
        try:
            import yaml  # type: ignore
        except Exception as exc:  # pragma: no cover - optional dependency
            raise RuntimeError("PyYAML is required for YAML config files.") from exc
        data = yaml.safe_load(raw) or {}
    else:
        data = json.loads(raw or "{}")
    if not isinstance(data, dict):
        raise RuntimeError("Config file must contain a JSON/YAML object at the root.")
    return data


def _apply_config(args: argparse.Namespace) -> argparse.Namespace:
    if not args.config:
        return args

    data = _load_config(args.config)
    defaults = data.get("defaults", {}) if isinstance(data.get("defaults"), dict) else {}
    consoles = data.get("consoles", {}) if isinstance(data.get("consoles"), dict) else {}
    profile = args.profile or data.get("default_profile") or "default"
    profile_data = consoles.get(profile, {}) if isinstance(consoles.get(profile), dict) else {}

    merged: Dict[str, Any] = {}
    merged.update(defaults)
    merged.update(profile_data)

    def pick(name: str, current: Any, fallback: Any = None) -> Any:
        if current is not None:
            return current
        return merged.get(name, fallback)

    args.console = pick("console", args.console) or merged.get("url", args.console)
    args.user = pick("user", args.user)
    args.ca_bundle = pick("ca_bundle", args.ca_bundle)
    args.insecure = bool(pick("insecure", args.insecure, False))
    args.timeout = pick("timeout", args.timeout, 60)
    return args


def _load_password(username: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {username}@{console}: ")


def _parse_cn(subject: str) -> Optional[str]:
    if not subject:
        return None
    match = re.search(r"(?:^|[,/\\s])CN=([^,/]+)", subject)
    if match:
        return match.group(1).strip()
    return None


def _list_certkeys(client: NitroConsoleClient) -> List[Dict[str, Any]]:
    payload = client.get_json("/nitro/v2/config/ns_ssl_certkey", params={"pagesize": "200"})
    items = payload.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return [items]
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return []


def _find_certkey(client: NitroConsoleClient, name: str, *, resolve_cn: bool) -> Dict[str, Any]:
    payload = client.get_json(
        "/nitro/v2/config/ns_ssl_certkey",
        params={"filter": f"certkeypair_name:{name}"},
    )
    items = payload.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return items
    if isinstance(items, list) and items:
        return items[0]
    if not resolve_cn:
        raise SystemExit(f"Certkeypair not found: {name}")

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


def _trigger_inventory(client: NitroConsoleClient) -> None:
    client.post_json(
        "/nitro/v2/config/ns_ssl_certkey",
        {"ns_ssl_certkey": {}},
        params={"action": "inventory"},
    )


def _poll_adcs(client: NitroConsoleClient, ns_ips: List[str]) -> None:
    if not ns_ips:
        return
    payload = {"ns_ssl_certkey_policy": {"ns_ip_address": ns_ips}}
    client.post_json("/nitro/v2/config/ns_ssl_certkey_policy", payload, params={"action": "do_poll"})


def _normalize_certkey_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", name or "").strip("_")


def _list_entity_certs(client: NitroConsoleClient, ns_ip: str) -> List[Dict[str, Any]]:
    payload = {"ns_ssl_certkey": {"source_ipaddress": ns_ip}}
    data = client.post_json("/nitro/v2/config/ns_ssl_certkey", payload, params={"action": "list_entity_cert"})
    items = data.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return [items]
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return []


def _try_import_with_name(
    client: NitroConsoleClient,
    target_name: str,
    *,
    ns_ip: str,
    source_name: str,
) -> Tuple[bool, Optional[str]]:
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": target_name,
            "ns_ip_address_arr": [ns_ip],
            "source_ipaddress": ns_ip,
            "source_certificate": source_name,
        }
    }
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)
    except NitroError as exc:
        return False, f"{exc.status_code} {exc.message}"
    return True, None


def _match_adc_cert(certs: List[Dict[str, Any]], name: str) -> Optional[Dict[str, Any]]:
    matches = []
    normalized = _normalize_certkey_name(name)
    for cert in certs:
        cert_name = str(cert.get("certkeypair_name") or "")
        if cert_name.lower() == name.lower():
            matches.append(cert)
            continue
        if normalized and _normalize_certkey_name(cert_name).lower() == normalized.lower():
            matches.append(cert)
            continue
        subject = str(cert.get("subject") or cert.get("certificate_dn") or "")
        cn = _parse_cn(subject)
        if cn and cn.lower() == name.lower():
            matches.append(cert)
    if len(matches) == 1:
        return matches[0]
    if matches:
        names = ", ".join(sorted({m.get("certkeypair_name", "unknown") for m in matches}))
        raise SystemExit(f"Multiple ADC certs match {name}: {names}")
    return None


def _import_from_adc(
    client: NitroConsoleClient,
    target_name: str,
    *,
    adc_ips: List[str],
) -> bool:
    last_error = None
    for ns_ip in adc_ips:
        try:
            certs = _list_entity_certs(client, ns_ip)
        except NitroError as exc:
            message = str(exc.message).lower()
            if exc.status_code not in (404, 405) and "not supported" not in message:
                raise
            candidates = [target_name, _normalize_certkey_name(target_name)]
            seen = set()
            for candidate in candidates:
                if not candidate or candidate in seen:
                    continue
                seen.add(candidate)
                ok, err = _try_import_with_name(client, target_name, ns_ip=ns_ip, source_name=candidate)
                if ok:
                    return True
                last_error = err
            continue
        match = _match_adc_cert(certs, target_name)
        if not match:
            continue
        source_name = match.get("certkeypair_name") or target_name
        ok, err = _try_import_with_name(client, target_name, ns_ip=ns_ip, source_name=source_name)
        if ok:
            return True
        last_error = err
    if last_error:
        raise SystemExit(f"Console import failed: {last_error}")
    return False


def _find_certkey_with_sync(
    client: NitroConsoleClient,
    name: str,
    *,
    resolve_cn: bool,
    sync: bool,
    sync_wait: int,
    import_missing: bool,
    import_wait: int,
    import_adc_ips: List[str],
) -> Dict[str, Any]:
    try:
        return _find_certkey(client, name, resolve_cn=resolve_cn)
    except SystemExit:
        pass
    if sync:
        _trigger_inventory(client)
        if sync_wait > 0:
            time.sleep(sync_wait)
        try:
            return _find_certkey(client, name, resolve_cn=resolve_cn)
        except SystemExit:
            pass
    if not import_missing:
        raise SystemExit(f"Certkeypair not found: {name}")
    if not import_adc_ips:
        raise SystemExit("Cannot import missing cert without --adc-ip or --list-adc menu selection.")
    if not _import_from_adc(client, name, adc_ips=import_adc_ips):
        raise SystemExit(f"Certkeypair not found on ADCs: {name}")
    if import_wait > 0:
        time.sleep(import_wait)
    return _find_certkey(client, name, resolve_cn=resolve_cn)


def _extract_bindings(cert: Dict[str, Any]) -> List[Dict[str, Any]]:
    bindings = cert.get("entity_binding_arr") or []
    if isinstance(bindings, dict):
        bindings = [bindings]
    if isinstance(bindings, list) and bindings:
        return [b for b in bindings if isinstance(b, dict)]
    ips = cert.get("ns_ip_address_arr") or []
    if isinstance(ips, str):
        ips = [ips]
    if isinstance(ips, list):
        return [{"ns_ip_address": ip} for ip in ips]
    return []


def _bind_cert(
    client: NitroConsoleClient,
    certkeypair: str,
    cert_id: Optional[str],
    binding: Dict[str, Any],
) -> None:
    payload = {
        "ns_ssl_certkey": {
            "certkeypair_name": certkeypair,
            "entity_binding_arr": [
                {
                    "certkeypair_name": certkeypair,
                    "ns_ip_address": binding.get("ns_ip_address"),
                    "id": binding.get("id"),
                }
            ],
        }
    }
    try:
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload, params={"action": "bind_cert"})
        return
    except NitroError as exc:
        message = str(exc.message).lower()
        if exc.status_code not in (404, 405) and "not supported" not in message:
            raise
        if not cert_id:
            raise SystemExit("Console does not support bind_cert and cert id is missing for fallback.")
        modify_payload = {
            "ns_ssl_certkey": {
                "id": cert_id,
                "certkeypair_name": certkeypair,
                "entity_binding_arr": payload["ns_ssl_certkey"]["entity_binding_arr"],
            }
        }
        client.put_json(f"/nitro/v2/config/ns_ssl_certkey/{cert_id}", modify_payload)


def _cert_exists(client: NitroConsoleClient, filename: str) -> bool:
    try:
        client.get_json(f"/nitro/v2/config/ns_ssl_cert/{filename}")
        return True
    except Exception:
        return False


def _certkey_exists(client: NitroConsoleClient, name: str) -> bool:
    try:
        _find_certkey(client, name)
        return True
    except SystemExit:
        return False


def _upload_ca_cert(
    client: NitroConsoleClient,
    ca_name: str,
    cert_path: Path,
    ns_ip_addresses: List[str],
) -> None:
    if not _cert_exists(client, cert_path.name):
        client.upload_file("/nitro/v2/upload/ns_ssl_cert", str(cert_path))
    if not _certkey_exists(client, ca_name):
        payload = {
            "ns_ssl_certkey": {
                "certkeypair_name": ca_name,
                "ns_ip_address_arr": ns_ip_addresses,
                "certificate_file_name": cert_path.name,
                "ssl_certificate": cert_path.name,
            }
        }
        client.post_json("/nitro/v2/config/ns_ssl_certkey", payload)


def _link_ca(client: NitroConsoleClient, certkeypair: str, ca_name: str, ns_ip: str) -> None:
    payload = {"ns_ssl_certlink": {"certkey": certkeypair, "linkcertkeyname": ca_name, "ns_ip_address": ns_ip}}
    client.post_json("/nitro/v2/config/ns_ssl_certlink", payload, params={"action": "link"})


def _parse_ca_inputs(args: argparse.Namespace) -> List[Tuple[str, Optional[Path]]]:
    names = args.ca_certkey or []
    files = args.ca_cert_file or []
    pairs = []
    for idx, name in enumerate(names):
        path = Path(files[idx]).expanduser() if idx < len(files) else None
        pairs.append((name, path))
    return pairs


def _extract_chain_names(cert: Dict[str, Any]) -> List[str]:
    chain = cert.get("certkeychain") or []
    if isinstance(chain, dict):
        chain = [chain]
    names = []
    for entry in chain:
        if not isinstance(entry, dict):
            continue
        name = entry.get("cert_name") or entry.get("certificate_file_name") or entry.get("linked_to")
        if name and name not in names:
            names.append(name)
    return names


def _extract_adc_ip(device: Dict[str, Any]) -> Optional[str]:
    return (
        device.get("ip_address")
        or device.get("mgmt_ip_address")
        or device.get("device_host_ip")
        or device.get("ipv4_address")
    )


def _is_primary(device: Dict[str, Any]) -> bool:
    state = str(device.get("ha_master_state") or "").lower()
    if state in ("primary", "master"):
        return True
    if state in ("secondary", "slave"):
        return False
    # If HA status is unknown, default to include.
    return True


def _list_managed_devices(client: NitroConsoleClient, *, primary_only: bool) -> List[Dict[str, Any]]:
    payload = client.get_json("/nitro/v2/config/managed_device")
    items = payload.get("managed_device", [])
    if isinstance(items, dict):
        items = [items]
    if isinstance(items, list):
        devices = [item for item in items if isinstance(item, dict)]
        if primary_only:
            devices = [device for device in devices if _is_primary(device)]
        return devices
    return []


def _write_adc_list_json(path: Path, devices: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for device in devices:
        rows.append(
            {
                "id": device.get("id"),
                "name": device.get("name"),
                "display_name": device.get("display_name"),
                "hostname": device.get("hostname"),
                "device_family": device.get("device_family"),
                "ip_address": _extract_adc_ip(device),
                "version": device.get("version"),
                "status": device.get("status"),
                "ha_master_state": device.get("ha_master_state"),
                "ha_ip_address": device.get("ha_ip_address"),
                "is_ha_configured": device.get("is_ha_configured"),
                "cluster_node_ip_list": device.get("cluster_node_ip_list"),
            }
        )
    path.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")


def _select_adc_menu(devices: List[Dict[str, Any]]) -> List[str]:
    rows = []
    for idx, device in enumerate(devices, start=1):
        ip = _extract_adc_ip(device) or "unknown"
        name = device.get("display_name") or device.get("name") or device.get("hostname") or "unknown"
        state = device.get("ha_master_state") or "unknown"
        rows.append((idx, name, ip, state))

    for idx, name, ip, state in rows:
        print(f"{idx:>2}) {name} [{ip}] (HA: {state})")
    choice = input("Select ADCs (comma-separated numbers) or 'q' to cancel: ").strip()
    if not choice or choice.lower() == "q":
        return []
    indices = {int(part.strip()) for part in choice.split(",") if part.strip().isdigit()}
    selected_ips = []
    for idx, _, ip, _ in rows:
        if idx in indices and ip != "unknown":
            selected_ips.append(ip)
    return selected_ips


def run(args: argparse.Namespace) -> int:
    args = _apply_config(args)
    if not args.console or not args.user:
        raise SystemExit("Console URL and user are required (use CLI args or --config/--profile).")

    verify: Any
    if args.insecure:
        verify = False
    elif args.ca_bundle:
        verify = args.ca_bundle
    else:
        verify = True

    password = _load_password(args.user, args.console, args.password)
    client = NitroConsoleClient(base=args.console, verify=verify, timeout=args.timeout)
    client.login(args.user, password)

    if args.list_adc:
        devices = _list_managed_devices(client, primary_only=not args.all_adc)
        if args.list_adc == "json":
            out_path = Path(args.list_adc_out)
            _write_adc_list_json(out_path, devices)
            print(f"Wrote ADC list: {out_path}")
            return 0
        if args.list_adc == "menu":
            selected = _select_adc_menu(devices)
            if not selected:
                raise SystemExit("No ADCs selected.")
            args.adc_ip = selected
            if args.poll_adc:
                _poll_adcs(client, selected)
                if args.poll_wait > 0:
                    time.sleep(args.poll_wait)

    import_adc_ips = args.adc_ip or []

    source_name = args.source_certkeypair or args.certkeypair
    source_cert = _find_certkey_with_sync(
        client,
        source_name,
        resolve_cn=args.resolve_cn,
        sync=args.sync,
        sync_wait=args.sync_wait,
        import_missing=args.import_missing,
        import_wait=args.import_wait,
        import_adc_ips=import_adc_ips,
    )
    if args.certkeypair == source_name:
        target_cert = source_cert
    else:
        target_cert = _find_certkey_with_sync(
            client,
            args.certkeypair,
            resolve_cn=args.resolve_cn,
            sync=args.sync,
            sync_wait=args.sync_wait,
            import_missing=args.import_missing,
            import_wait=args.import_wait,
            import_adc_ips=import_adc_ips,
        )
    bindings = _extract_bindings(source_cert)
    if not bindings and args.adc_ip:
        bindings = [{"ns_ip_address": ip} for ip in args.adc_ip]
    if not bindings:
        raise SystemExit(f"No bindings found for certkeypair: {source_name}")

    ns_ips = [b.get("ns_ip_address") for b in bindings if b.get("ns_ip_address")]

    ca_pairs = _parse_ca_inputs(args)
    if args.link_ca and not ca_pairs:
        chain_names = _extract_chain_names(source_cert)
        ca_pairs = [(name, None) for name in chain_names]
    for ca_name, ca_path in ca_pairs:
        if ca_path:
            _upload_ca_cert(client, ca_name, ca_path, ns_ips)

    for binding in bindings:
        _bind_cert(client, args.certkeypair, target_cert.get("id"), binding)
        if args.link_ca:
            for ca_name, _ in ca_pairs:
                _link_ca(client, args.certkeypair, ca_name, binding.get("ns_ip_address"))

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deploy a Console certkey to ADCs via bindings.")
    parser.add_argument("--certkeypair", required=True, help="Target certkeypair name to deploy")
    parser.add_argument("--source-certkeypair", help="Source certkeypair name to copy bindings from")
    parser.add_argument("--adc-ip", action="append", help="Target ADC IP (repeatable)")
    parser.add_argument(
        "--list-adc",
        choices=["json", "menu"],
        help="List managed ADCs and exit or select interactively",
    )
    parser.add_argument(
        "--all-adc",
        action="store_true",
        default=False,
        help="Include non-primary HA nodes in ADC listing",
    )
    parser.add_argument(
        "--list-adc-out",
        default="./out/managed_devices.json",
        help="Output path for --list-adc json",
    )
    parser.add_argument("--link-ca", action="store_true", default=True, help="Link CA certs after deploy")
    parser.add_argument("--no-link-ca", dest="link_ca", action="store_false", help="Disable CA linking")
    parser.add_argument("--ca-certkey", action="append", help="CA certkeypair name to link (repeatable)")
    parser.add_argument("--ca-cert-file", action="append", help="CA cert PEM file to upload (repeatable)")
    parser.add_argument("--console", help="Console base URL, e.g. https://console")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--password", help="Console password (or set CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--config", help="Path to JSON/YAML config file")
    parser.add_argument("--profile", help="Config profile name (default: default)")
    parser.add_argument("--insecure", action="store_true", help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for TLS verification")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds")
    parser.add_argument(
        "--sync",
        action="store_true",
        default=False,
        help="Trigger Console inventory refresh before looking up certs",
    )
    parser.add_argument(
        "--sync-wait",
        type=int,
        default=0,
        help="Seconds to wait after inventory refresh (default: 0)",
    )
    parser.add_argument(
        "--import-missing",
        action="store_true",
        default=False,
        help="Import missing certkeypairs from ADCs via Console proxy before failing",
    )
    parser.add_argument(
        "--import-wait",
        type=int,
        default=0,
        help="Seconds to wait after importing from ADCs (default: 0)",
    )
    parser.add_argument(
        "--poll-adc",
        action="store_true",
        default=False,
        help="Poll selected ADCs via Console before lookup (requires --list-adc menu or --adc-ip)",
    )
    parser.add_argument(
        "--poll-wait",
        type=int,
        default=0,
        help="Seconds to wait after ADC poll (default: 0)",
    )
    parser.add_argument(
        "--no-resolve-cn",
        dest="resolve_cn",
        action="store_false",
        help="Disable CN lookup when certkeypair name is not found",
    )
    parser.set_defaults(resolve_cn=True)
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
