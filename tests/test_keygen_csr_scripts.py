from pathlib import Path

import pytest

from certctl.scripts import csr_create, keygen
from certctl.scripts import keycsr


def test_keygen_rsa_builds_openssl_command(monkeypatch, tmp_path):
    captured = {}

    def fake_run(cmd, env=None):
        captured["cmd"] = cmd
        if "-out" in cmd:
            out_path = Path(cmd[cmd.index("-out") + 1])
            out_path.write_text("dummy", encoding="utf-8")

    monkeypatch.setattr(keygen, "_run", fake_run)
    monkeypatch.setattr(keygen, "_require_openssl", lambda: "/usr/bin/openssl")

    args = keygen.build_arg_parser().parse_args(
        [
            "--cn",
            "example.com",
            "--kind",
            "rsa",
            "--out",
            str(tmp_path),
            "--stamp",
            "20260101-120000",
            "--passphrase",
            "secret",
        ]
    )
    keygen.run(args)

    cmd = captured["cmd"]
    assert "genpkey" in cmd
    assert "RSA" in cmd
    assert f"rsa_keygen_bits:{keygen.DEFAULT_RSA_BITS}" in cmd
    assert "-aes-256-cbc" in cmd


def test_keygen_ecdsa_builds_openssl_command(monkeypatch, tmp_path):
    captured = {}

    def fake_run(cmd, env=None):
        captured["cmd"] = cmd
        if "-out" in cmd:
            out_path = Path(cmd[cmd.index("-out") + 1])
            out_path.write_text("dummy", encoding="utf-8")

    monkeypatch.setattr(keygen, "_run", fake_run)
    monkeypatch.setattr(keygen, "_require_openssl", lambda: "/usr/bin/openssl")

    args = keygen.build_arg_parser().parse_args(
        [
            "--cn",
            "example.com",
            "--kind",
            "ecdsa",
            "--out",
            str(tmp_path),
            "--passphrase",
            "secret",
        ]
    )
    keygen.run(args)

    cmd = captured["cmd"]
    assert "genpkey" in cmd
    assert "EC" in cmd
    assert f"ec_paramgen_curve:{keygen.DEFAULT_EC_CURVE}" in cmd
    assert "-aes-256-cbc" in cmd


def test_csr_create_runs_openssl_with_config(monkeypatch, tmp_path):
    captured = {}
    config_path = tmp_path / "openssl.cnf"
    config_path.write_text("[req]\n", encoding="utf-8")

    def fake_run(cmd, env=None):
        captured["cmd"] = cmd

    def fake_write_config(subject, sans):
        return str(config_path)

    monkeypatch.setattr(csr_create, "_run", fake_run)
    monkeypatch.setattr(csr_create, "_require_openssl", lambda: "/usr/bin/openssl")
    monkeypatch.setattr(csr_create, "_write_openssl_config", fake_write_config)

    key_path = tmp_path / "key.pem"
    key_path.write_text("dummy", encoding="utf-8")
    out_path = tmp_path / "req.csr"

    args = csr_create.build_arg_parser().parse_args(
        [
            "--key-file",
            str(key_path),
            "--cn",
            "example.com",
            "--out",
            str(tmp_path),
            "--stamp",
            "20260101-120000",
            "--passphrase",
            "secret",
            "--san",
            "DNS:www.example.com, IP:192.168.0.1",
        ]
    )
    csr_create.run(args)

    cmd = captured["cmd"]
    assert cmd[0] == "openssl"
    assert "req" in cmd
    out_arg = cmd[cmd.index("-out") + 1]
    assert out_arg.startswith(str(tmp_path))
    assert str(config_path) in cmd

    assert not config_path.exists()


def test_keycsr_uses_shared_stamp(monkeypatch, tmp_path):
    calls = {"key": None, "csr": None}

    def fake_generate(kind, path, passphrase):
        calls["key"] = path

    def fake_csr_run(args):
        calls["csr"] = args
        return 0

    monkeypatch.setattr(keygen, "_generate_key", fake_generate)
    monkeypatch.setattr(csr_create, "run", fake_csr_run)
    monkeypatch.setattr(keygen, "_get_passphrase", lambda args: "secret")

    args = keycsr.build_arg_parser().parse_args(
        [
            "--cn",
            "example.com",
            "--kind",
            "rsa",
            "--out",
            str(tmp_path),
            "--stamp",
            "20260101-120000",
        ]
    )
    keycsr.run(args)

    assert calls["key"].name == "example.com-20260101-120000.key"
    assert calls["csr"].stamp == "20260101-120000"
