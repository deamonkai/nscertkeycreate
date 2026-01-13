"""Tests for the CLI wiring of keygen --save-passphrase flag."""
from nscert import cli


def test_cli_keygen_save_passphrase(monkeypatch, capsys):
    called = {}

    def fake_gen_rsa(**kwargs):
        called.update(kwargs)
        return "PEM-KEY"

    monkeypatch.setattr("nscert.keygen.generate_rsa_key", fake_gen_rsa)

    # Simulate cli args
    rc = cli.main(["keygen", "--kind", "rsa", "--bits", "1024", "--passphrase", "fromcli", "--keychain-service", "svc-cli", "--save-passphrase"]) 

    assert rc == 0
    assert called["passphrase"] == "fromcli"
    assert called["keychain_service"] == "svc-cli"
    assert called["save_to_keychain"] is True


def test_cli_keygen_write_file(monkeypatch, tmp_path):
    def fake_gen_ec(**kwargs):
        return "PEM-EC"

    monkeypatch.setattr("nscert.keygen.generate_ec_key", fake_gen_ec)

    out = tmp_path / "key.pem"

    rc = cli.main(["keygen", "--kind", "ec", "--curve", "prime256v1", "--out", str(out)])
    assert rc == 0

    assert out.exists()
    assert out.read_text() == "PEM-EC"
