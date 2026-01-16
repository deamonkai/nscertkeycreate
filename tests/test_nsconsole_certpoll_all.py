import json

import responses

from certctl.scripts.nsconsole_certpoll_all import build_arg_parser, run


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


def _add_certkey_get(resps, base, items):
    resps.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "ns_ssl_certkey": items},
        status=200,
    )


@responses.activate
def test_poll_all_from_config(tmp_path, monkeypatch):
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    config_path = tmp_path / "certctl.json"
    config_path.write_text(
        json.dumps(
            {
                "defaults": {"format": "json"},
                "consoles": {
                    "test": {"url": "https://console-test.example", "user": "nsroot", "insecure": True},
                    "prod": {"url": "https://console-prod.example", "user": "nsroot", "insecure": True},
                },
            }
        ),
        encoding="utf-8",
    )

    _add_login(responses, "https://console-test.example")
    _add_certkey_get(
        responses,
        "https://console-test.example",
        [{"certkeypair_name": "test-cert", "certkey_status": "ACTIVE"}],
    )
    _add_login(responses, "https://console-prod.example")
    _add_certkey_get(
        responses,
        "https://console-prod.example",
        [{"certkeypair_name": "prod-cert", "certkey_status": "ACTIVE"}],
    )

    out_dir = tmp_path / "reports"
    args = _args(["--config", str(config_path), "--format", "json", "--out-dir", str(out_dir)])
    assert run(args) == 0

    test_payload = json.loads((out_dir / "test.json").read_text(encoding="utf-8"))
    prod_payload = json.loads((out_dir / "prod.json").read_text(encoding="utf-8"))

    assert test_payload["count"] == 1
    assert prod_payload["count"] == 1


@responses.activate
def test_poll_all_merge_json(tmp_path, monkeypatch):
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    config_path = tmp_path / "certctl.json"
    config_path.write_text(
        json.dumps(
            {
                "defaults": {"format": "json"},
                "consoles": {
                    "test": {"url": "https://console-test.example", "user": "nsroot", "insecure": True},
                    "prod": {"url": "https://console-prod.example", "user": "nsroot", "insecure": True},
                },
            }
        ),
        encoding="utf-8",
    )

    _add_login(responses, "https://console-test.example")
    _add_certkey_get(
        responses,
        "https://console-test.example",
        [{"certkeypair_name": "test-cert", "certkey_status": "ACTIVE"}],
    )
    _add_login(responses, "https://console-prod.example")
    _add_certkey_get(
        responses,
        "https://console-prod.example",
        [{"certkeypair_name": "prod-cert", "certkey_status": "ACTIVE"}],
    )

    out_dir = tmp_path / "reports"
    args = _args(
        [
            "--config",
            str(config_path),
            "--format",
            "json",
            "--out-dir",
            str(out_dir),
            "--merge",
        ]
    )
    assert run(args) == 0

    merged = json.loads((out_dir / "all.json").read_text(encoding="utf-8"))
    assert merged["count"] == 2
    profiles = {item["profile"] for item in merged["items"]}
    assert profiles == {"test", "prod"}


@responses.activate
def test_poll_all_merge_csv(tmp_path, monkeypatch):
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    config_path = tmp_path / "certctl.json"
    config_path.write_text(
        json.dumps(
            {
                "defaults": {"format": "json"},
                "consoles": {
                    "test": {"url": "https://console-test.example", "user": "nsroot", "insecure": True},
                    "prod": {"url": "https://console-prod.example", "user": "nsroot", "insecure": True},
                },
            }
        ),
        encoding="utf-8",
    )

    _add_login(responses, "https://console-test.example")
    _add_certkey_get(
        responses,
        "https://console-test.example",
        [{"certkeypair_name": "test-cert", "certkey_status": "ACTIVE"}],
    )
    _add_login(responses, "https://console-prod.example")
    _add_certkey_get(
        responses,
        "https://console-prod.example",
        [{"certkeypair_name": "prod-cert", "certkey_status": "ACTIVE"}],
    )

    out_dir = tmp_path / "reports"
    args = _args(
        [
            "--config",
            str(config_path),
            "--format",
            "csv",
            "--out-dir",
            str(out_dir),
            "--merge",
        ]
    )
    assert run(args) == 0

    csv_path = out_dir / "all.csv"
    lines = csv_path.read_text(encoding="utf-8").strip().splitlines()
    assert lines
    assert "profile" in lines[0]
    assert any("test" in line for line in lines[1:])
    assert any("prod" in line for line in lines[1:])


@responses.activate
def test_poll_all_rollup_json(tmp_path, monkeypatch):
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    config_path = tmp_path / "certctl.json"
    config_path.write_text(
        json.dumps(
            {
                "defaults": {"format": "json"},
                "consoles": {
                    "test": {"url": "https://console-test.example", "user": "nsroot", "insecure": True},
                    "prod": {"url": "https://console-prod.example", "user": "nsroot", "insecure": True},
                },
            }
        ),
        encoding="utf-8",
    )

    _add_login(responses, "https://console-test.example")
    _add_certkey_get(
        responses,
        "https://console-test.example",
        [{"certkeypair_name": "test-cert", "certkey_status": "ACTIVE", "subject": "CN=example.com"}],
    )
    _add_login(responses, "https://console-prod.example")
    _add_certkey_get(
        responses,
        "https://console-prod.example",
        [{"certkeypair_name": "prod-cert", "certkey_status": "ACTIVE", "subject": "CN=example.com"}],
    )

    out_dir = tmp_path / "reports"
    args = _args(
        [
            "--config",
            str(config_path),
            "--format",
            "json",
            "--out-dir",
            str(out_dir),
            "--rollup",
        ]
    )
    assert run(args) == 0

    rollup = json.loads((out_dir / "rollup_subjects.json").read_text(encoding="utf-8"))
    assert rollup["count_subjects"] == 1
    subject = rollup["subjects"][0]
    assert subject["subject"] == "CN=example.com"
    assert set(subject["profiles"]) == {"test", "prod"}
