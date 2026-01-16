import json
from pathlib import Path

import responses

from certctl.scripts.nsconsole_certpoll import build_arg_parser, run


def _args(args):
    parser = build_arg_parser()
    return parser.parse_args(args)


def _add_login(resps, base):
    resps.add(
        responses.POST,
        f"{base}/nitro/v2/config/login",
        json={"login": [{"sessionid": "token"}]},
        status=200,
    )


def _add_inventory(resps, base):
    resps.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"action": "inventory"})],
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )


def _add_certkey_get(resps, base, items):
    resps.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "ns_ssl_certkey": items},
        status=200,
    )


@responses.activate
def test_certpoll_filters_in_use(monkeypatch, tmp_path):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_certkey_get(
        responses,
        base,
        [
            {
                "certkeypair_name": "active-bound",
                "no_of_bound_entities": 2,
                "days_to_expiry": 10,
                "entity_binding_arr": [
                    {"entity_name": "lb1", "entity_type": "sslvserver", "display_name": "adc-1"}
                ],
            },
            {"certkeypair_name": "active-unbound", "certkey_status": "ACTIVE", "days_to_expiry": 15},
            {"certkeypair_name": "inactive", "certkey_status": "INACTIVE", "days_to_expiry": 20},
        ],
    )

    out_path = tmp_path / "report.json"
    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--format",
            "json",
            "--out",
            str(out_path),
        ]
    )
    assert run(args) == 0

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload["count"] == 2
    names = {item["certkeypair_name"] for item in payload["items"]}
    assert names == {"active-bound", "active-unbound"}
    bound = next(item for item in payload["items"] if item["certkeypair_name"] == "active-bound")
    assert bound["binding_count"] == 1
    assert bound["binding_entities"] == "lb1"
    assert bound["binding_types"] == "sslvserver"
    assert bound["binding_devices"] == "adc-1"


@responses.activate
def test_certpoll_includes_cert_store_mapping(monkeypatch, tmp_path):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_certkey_get(
        responses,
        base,
        [
            {
                "certkeypair_name": "mapped",
                "certkey_status": "ACTIVE",
                "cert_store_id": "cert-1",
            }
        ],
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/cert_store_mapping",
        json={
            "errorcode": 0,
            "cert_store_mapping": [
                {
                    "cert_id": "cert-1",
                    "entity_name": "svc-1",
                    "entity_type": "service",
                    "instance_display_name": "adc-2",
                    "instance_ip": "10.0.0.1",
                }
            ],
        },
        status=200,
    )

    out_path = tmp_path / "report.json"
    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--format",
            "json",
            "--out",
            str(out_path),
            "--include-mappings",
        ]
    )
    assert run(args) == 0

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    item = payload["items"][0]
    assert item["mapping_count"] == 1
    assert item["mapping_entities"] == "svc-1"
    assert item["mapping_entity_types"] == "service"
    assert item["mapping_instances"] == "adc-2"
    assert item["mapping_instance_ips"] == "10.0.0.1"


@responses.activate
def test_certpoll_filters_by_expiry(monkeypatch, tmp_path):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_certkey_get(
        responses,
        base,
        [
            {"certkeypair_name": "soon", "certkey_status": "ACTIVE", "days_to_expiry": 10},
            {"certkeypair_name": "later", "certkey_status": "ACTIVE", "days_to_expiry": 45},
        ],
    )

    out_path = tmp_path / "report.json"
    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--format",
            "json",
            "--out",
            str(out_path),
            "--expires-within",
            "30",
        ]
    )
    assert run(args) == 0

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    names = {item["certkeypair_name"] for item in payload["items"]}
    assert names == {"soon"}


@responses.activate
def test_certpoll_inventory_and_all(monkeypatch, capsys):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_inventory(responses, base)
    _add_certkey_get(
        responses,
        base,
        [
            {"certkeypair_name": "active", "certkey_status": "ACTIVE", "days_to_expiry": 10},
            {"certkeypair_name": "inactive", "certkey_status": "INACTIVE", "days_to_expiry": 20},
        ],
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--inventory",
            "--all",
        ]
    )
    assert run(args) == 0

    stdout = capsys.readouterr().out
    assert "certkeypair_name" in stdout
    assert "active" in stdout
    assert "inactive" in stdout
    assert any("action=inventory" in call.request.url for call in responses.calls)


@responses.activate
def test_certpoll_uses_config_profile(monkeypatch, tmp_path):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    config_path = tmp_path / "certctl.json"
    config_path.write_text(
        json.dumps(
            {
                "defaults": {"format": "json", "inventory": True},
                "consoles": {
                    "test": {
                        "url": base,
                        "user": "nsroot",
                        "insecure": True,
                    }
                },
            }
        ),
        encoding="utf-8",
    )

    _add_login(responses, base)
    _add_inventory(responses, base)
    _add_certkey_get(
        responses,
        base,
        [{"certkeypair_name": "active", "certkey_status": "ACTIVE", "days_to_expiry": 10}],
    )

    out_path = tmp_path / "report.json"
    args = _args(["--config", str(config_path), "--profile", "test", "--out", str(out_path)])
    assert run(args) == 0

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload["count"] == 1
    assert payload["items"][0]["certkeypair_name"] == "active"
