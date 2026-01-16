#!/usr/bin/env python3
"""Poll NetScaler Console for SSL cert inventory and write a report."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import getpass
import json
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from certctl.console import NitroConsoleClient

DEFAULT_TIMEOUT = 60
MAX_CELL = 60


def _now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _to_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _clip(value: Any, width: int = MAX_CELL) -> str:
    text = "" if value is None else str(value)
    if len(text) <= width:
        return text
    return text[: max(0, width - 3)] + "..."


def _is_in_use(item: Dict[str, Any]) -> bool:
    if _to_int(item.get("no_of_bound_entities")) > 0:
        return True
    status = (item.get("certkey_status") or item.get("status") or "").upper()
    return status == "ACTIVE"


def _extract_row(item: Dict[str, Any], mapping_index: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    bindings = _normalize_bindings(item.get("entity_binding_arr"))
    entity_names = _join_unique(binding.get("entity_name") for binding in bindings)
    entity_types = _join_unique(binding.get("entity_type") for binding in bindings)
    binding_devices = _join_unique(
        binding.get("display_name") or binding.get("hostname") for binding in bindings
    )
    cert_id = item.get("cert_store_id") or ""
    mappings = mapping_index.get(str(cert_id), [])
    mapping_entities = _join_unique(mapping.get("entity_name") for mapping in mappings)
    mapping_entity_types = _join_unique(mapping.get("entity_type") for mapping in mappings)
    mapping_instances = _join_unique(
        mapping.get("instance_display_name") or mapping.get("instance_host_name") for mapping in mappings
    )
    mapping_instance_ips = _join_unique(mapping.get("instance_ip") for mapping in mappings)
    return {
        "certkeypair_name": item.get("certkeypair_name") or "",
        "device_name": item.get("device_name") or item.get("display_name") or item.get("hostname") or "",
        "ns_ip_address": item.get("ns_ip_address") or "",
        "subject": item.get("subject") or "",
        "issuer": item.get("issuer") or item.get("issuer_cn") or "",
        "valid_from": item.get("valid_from") or "",
        "valid_to": item.get("valid_to") or "",
        "days_to_expiry": item.get("days_to_expiry") or "",
        "no_of_bound_entities": item.get("no_of_bound_entities") or "",
        "certkey_status": item.get("certkey_status") or item.get("status") or "",
        "binding_count": len(bindings),
        "binding_entities": entity_names,
        "binding_types": entity_types,
        "binding_devices": binding_devices,
        "mapping_count": len(mappings),
        "mapping_entities": mapping_entities,
        "mapping_entity_types": mapping_entity_types,
        "mapping_instances": mapping_instances,
        "mapping_instance_ips": mapping_instance_ips,
    }


def _normalize_bindings(value: Any) -> List[Dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        return [value]
    return []


def _normalize_mappings(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    items = payload.get("cert_store_mapping", [])
    if isinstance(items, dict):
        return [items]
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return []


def _join_unique(values: Iterable[Optional[str]]) -> str:
    seen = []
    for value in values:
        if not value:
            continue
        if value not in seen:
            seen.append(value)
    return ", ".join(seen)


def _render_table(rows: Iterable[Dict[str, Any]], columns: List[str]) -> str:
    rows_list = list(rows)
    widths = {col: len(col) for col in columns}
    for row in rows_list:
        for col in columns:
            widths[col] = max(widths[col], len(_clip(row.get(col, ""))))

    def fmt_row(row: Dict[str, Any]) -> str:
        return "  ".join(_clip(row.get(col, "")).ljust(widths[col]) for col in columns)

    header = fmt_row({col: col for col in columns})
    sep = "  ".join("-" * widths[col] for col in columns)
    body = "\n".join(fmt_row(row) for row in rows_list)
    return "\n".join([header, sep, body]).strip()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _write_csv(path: Path, rows: List[Dict[str, Any]], columns: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row.get(col, "") for col in columns})


def _load_password(username: str, console: str, provided: Optional[str]) -> str:
    if provided:
        return provided
    env_pw = os.environ.get("CERTCTL_CONSOLE_PASSWORD")
    if env_pw:
        return env_pw
    return getpass.getpass(f"Console password for {username}@{console}: ")


def _normalize_items(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    items = payload.get("ns_ssl_certkey", [])
    if isinstance(items, dict):
        return [items]
    if isinstance(items, list):
        return items
    return []


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
    profile = args.profile or "default"
    profile_data = consoles.get(profile, {}) if isinstance(consoles.get(profile), dict) else {}

    # Merge defaults then profile, then explicit CLI values.
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
    args.timeout = pick("timeout", args.timeout, DEFAULT_TIMEOUT)
    args.format = pick("format", args.format, "table")
    args.out = pick("out", args.out)
    args.all = bool(pick("all", args.all, False))
    args.inventory = bool(pick("inventory", args.inventory, False))
    args.include_mappings = bool(pick("include_mappings", args.include_mappings, False))
    args.expires_within = pick("expires_within", args.expires_within)
    return args


def run(args: argparse.Namespace) -> int:
    args = _apply_config(args)
    if args.timeout is None:
        args.timeout = DEFAULT_TIMEOUT
    if args.format is None:
        args.format = "table"
    if args.insecure is None:
        args.insecure = False
    if args.all is None:
        args.all = False
    if args.inventory is None:
        args.inventory = False
    if args.include_mappings is None:
        args.include_mappings = False
    if args.expires_within is None:
        args.expires_within = None
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

    if args.inventory:
        client.post_json(
            "/nitro/v2/config/ns_ssl_certkey",
            {"ns_ssl_certkey": {}},
            params={"action": "inventory"},
        )

    payload = client.get_json("/nitro/v2/config/ns_ssl_certkey")
    items = _normalize_items(payload)

    mapping_index: Dict[str, List[Dict[str, Any]]] = {}
    if args.include_mappings:
        mapping_payload = client.get_json("/nitro/v2/config/cert_store_mapping")
        mappings = _normalize_mappings(mapping_payload)
        for mapping in mappings:
            cert_id = mapping.get("cert_id")
            if cert_id is None:
                continue
            mapping_index.setdefault(str(cert_id), []).append(mapping)

    if not args.all:
        items = [item for item in items if _is_in_use(item)]
    if args.expires_within is not None:
        cutoff = int(args.expires_within)
        filtered = []
        for item in items:
            raw = item.get("days_to_expiry")
            days = _to_int(raw) if raw not in (None, "") else 7
            if days <= cutoff:
                filtered.append(item)
        items = filtered

    rows = [_extract_row(item, mapping_index) for item in items]
    rows.sort(key=lambda row: (row.get("subject") or "").lower())
    columns = [
        "certkeypair_name",
        "device_name",
        "ns_ip_address",
        "certkey_status",
        "no_of_bound_entities",
        "binding_count",
        "binding_types",
        "binding_devices",
        "binding_entities",
        "mapping_count",
        "mapping_entity_types",
        "mapping_instances",
        "mapping_instance_ips",
        "mapping_entities",
        "days_to_expiry",
        "valid_to",
        "subject",
    ]

    report: Optional[Dict[str, Any]] = None
    output: Optional[str] = None
    if args.format == "json":
        report = {
            "generated_at": _now_utc().isoformat(),
            "count": len(rows),
            "items": rows,
        }
        output = json.dumps(report, indent=2, sort_keys=True)
    elif args.format == "table":
        output = _render_table(rows, columns)

    if args.out:
        out_path = Path(args.out)
        if args.format == "json":
            _write_json(out_path, report or {"generated_at": _now_utc().isoformat(), "count": 0, "items": []})
        elif args.format == "csv":
            _write_csv(out_path, rows, columns)
        else:
            _write_text(out_path, output)
    else:
        if args.format == "csv":
            writer = csv.DictWriter(os.sys.stdout, fieldnames=columns)
            writer.writeheader()
            for row in rows:
                writer.writerow({col: row.get(col, "") for col in columns})
        else:
            print(output)

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Poll NetScaler Console for SSL cert inventory and output a report."
    )
    parser.add_argument("--console", help="Console base URL, e.g. https://console")
    parser.add_argument("--user", help="Console username")
    parser.add_argument("--password", help="Console password (or set CERTCTL_CONSOLE_PASSWORD)")
    parser.add_argument("--config", help="Path to JSON/YAML config file")
    parser.add_argument("--profile", help="Config profile name (default: default)")
    parser.add_argument("--insecure", action="store_true", default=None, help="Disable TLS verification")
    parser.add_argument("--ca-bundle", help="Path to CA bundle for TLS verification")
    parser.add_argument("--timeout", type=int, default=None, help="HTTP timeout in seconds")
    parser.add_argument(
        "--format",
        choices=["table", "csv", "json"],
        default=None,
        help="Report format",
    )
    parser.add_argument("--out", help="Write report to a file instead of stdout")
    parser.add_argument(
        "--all",
        action="store_true",
        default=None,
        help="Include unbound or inactive certs (default is in-use only)",
    )
    parser.add_argument(
        "--inventory",
        action="store_true",
        default=None,
        help="Trigger inventory refresh before fetching certs",
    )
    parser.add_argument(
        "--include-mappings",
        action="store_true",
        default=None,
        help="Include cert_store_mapping data in the report",
    )
    parser.add_argument(
        "--expires-within",
        type=int,
        default=None,
        help="Only include certs expiring within N days",
    )
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
