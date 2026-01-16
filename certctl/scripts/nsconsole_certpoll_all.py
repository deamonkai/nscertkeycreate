#!/usr/bin/env python3
"""Poll all configured NetScaler Consoles and write per-profile reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from certctl.scripts import nsconsole_certpoll


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


def _ext_for_format(fmt: str) -> str:
    return {"json": "json", "csv": "csv"}.get(fmt, "txt")


def _collect_items(format_name: str, inputs: Dict[str, Path]) -> list[Dict[str, Any]]:
    items: list[Dict[str, Any]] = []
    if format_name == "csv":
        import csv

        for profile, path in inputs.items():
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    row = dict(row)
                    row["profile"] = profile
                    items.append(row)
    else:
        for profile, path in inputs.items():
            payload = json.loads(path.read_text(encoding="utf-8"))
            rows = payload.get("items", [])
            if isinstance(rows, list):
                for row in rows:
                    if isinstance(row, dict):
                        row = dict(row)
                        row["profile"] = profile
                        items.append(row)
    return items


def _merge_reports(format_name: str, inputs: Dict[str, Path], output: Path) -> None:
    merged: Dict[str, Any] = {
        "generated_at": None,
        "profiles": {},
        "count": 0,
        "items": [],
    }

    if format_name == "csv":
        for profile, path in inputs.items():
            rows = _collect_items("csv", {profile: path})
            merged["profiles"][profile] = {"generated_at": None, "count": len(rows)}
            merged["items"].extend(rows)
            merged["count"] += len(rows)
    else:
        for profile, path in inputs.items():
            payload = json.loads(path.read_text(encoding="utf-8"))
            merged["profiles"][profile] = {
                "generated_at": payload.get("generated_at"),
                "count": payload.get("count", 0),
            }
            if merged["generated_at"] is None:
                merged["generated_at"] = payload.get("generated_at")
            rows = _collect_items("json", {profile: path})
            merged["items"].extend(rows)
            merged["count"] += payload.get("count", 0)

    output.parent.mkdir(parents=True, exist_ok=True)
    if format_name == "csv":
        # Build a union of keys to ensure CSV columns cover all profiles.
        keys = []
        for item in merged["items"]:
            for key in item.keys():
                if key not in keys:
                    keys.append(key)
        if "profile" not in keys:
            keys.insert(0, "profile")
        with output.open("w", newline="", encoding="utf-8") as handle:
            import csv

            writer = csv.DictWriter(handle, fieldnames=keys)
            writer.writeheader()
            for item in merged["items"]:
                writer.writerow({k: item.get(k, "") for k in keys})
    else:
        output.write_text(json.dumps(merged, indent=2, sort_keys=True), encoding="utf-8")


def _write_rollup(format_name: str, items: list[Dict[str, Any]], output: Path) -> None:
    groups: Dict[str, Dict[str, Any]] = {}
    for item in items:
        subject = (item.get("subject") or "").strip() or "(unknown)"
        entry = groups.setdefault(
            subject,
            {
                "subject": subject,
                "count": 0,
                "profiles": [],
                "certkeypair_names": [],
            },
        )
        entry["count"] += 1
        profile = item.get("profile")
        if profile and profile not in entry["profiles"]:
            entry["profiles"].append(profile)
        name = item.get("certkeypair_name")
        if name and name not in entry["certkeypair_names"]:
            entry["certkeypair_names"].append(name)

    rollup = {
        "count_subjects": len(groups),
        "subjects": sorted(groups.values(), key=lambda x: x["subject"].lower()),
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    if format_name == "csv":
        import csv

        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["subject", "count", "profiles", "certkeypair_names"],
            )
            writer.writeheader()
            for entry in rollup["subjects"]:
                writer.writerow(
                    {
                        "subject": entry["subject"],
                        "count": entry["count"],
                        "profiles": ", ".join(entry["profiles"]),
                        "certkeypair_names": ", ".join(entry["certkeypair_names"]),
                    }
                )
    else:
        output.write_text(json.dumps(rollup, indent=2, sort_keys=True), encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    data = _load_config(args.config)
    consoles = data.get("consoles", {})
    if not isinstance(consoles, dict) or not consoles:
        raise SystemExit("Config must include a non-empty 'consoles' mapping.")

    out_dir = Path(args.out_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    profiles = [args.profile] if args.profile else list(consoles.keys())
    report_paths: Dict[str, Path] = {}
    for profile in profiles:
        if profile not in consoles:
            raise SystemExit(f"Profile '{profile}' not found in config.")
        ext = _ext_for_format(args.format)
        out_path = out_dir / f"{profile}.{ext}"

        poll_args = argparse.Namespace(
            console=None,
            user=None,
            password=None,
            config=args.config,
            profile=profile,
            insecure=None,
            ca_bundle=None,
            timeout=None,
            format=args.format,
            out=str(out_path),
            all=args.all,
            inventory=args.inventory,
            include_mappings=args.include_mappings,
            expires_within=args.expires_within,
        )
        nsconsole_certpoll.run(poll_args)
        report_paths[profile] = out_path
        print(f"[{profile}] wrote {args.format} report to {out_path}")

    if args.merge:
        if args.format not in ("json", "csv"):
            raise SystemExit("--merge is only supported with --format json or csv.")
        merged_path = out_dir / f"all.{_ext_for_format(args.format)}"
        _merge_reports(args.format, report_paths, merged_path)
        print(f"[all] wrote merged {args.format} report to {merged_path}")

    if args.rollup:
        if args.format not in ("json", "csv"):
            raise SystemExit("--rollup is only supported with --format json or csv.")
        items = _collect_items(args.format, report_paths)
        rollup_path = out_dir / f"rollup_subjects.{_ext_for_format(args.format)}"
        _write_rollup(args.format, items, rollup_path)
        print(f"[rollup] wrote subject rollup to {rollup_path}")

    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Poll all configured NetScaler Consoles and write per-profile reports."
    )
    parser.add_argument("--config", required=True, help="Path to JSON/YAML config file")
    parser.add_argument("--out-dir", default="./reports", help="Output directory for reports")
    parser.add_argument(
        "--format",
        choices=["table", "csv", "json"],
        default="json",
        help="Report format",
    )
    parser.add_argument("--profile", help="Only run a single profile")
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
        "--merge",
        action="store_true",
        default=False,
        help="Write a combined report across all profiles (json/csv only)",
    )
    parser.add_argument(
        "--rollup",
        action="store_true",
        default=False,
        help="Write a subject rollup across all profiles (json/csv only)",
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
