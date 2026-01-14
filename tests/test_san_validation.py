"""Tests for SAN validation and CLI rejection of invalid SANs."""
import pytest
from certctl.csr import normalize_and_validate_san


def test_normalize_dns():
    assert normalize_and_validate_san("www.example.com") == "DNS:www.example.com"
    assert normalize_and_validate_san("DNS:www.example.com") == "DNS:www.example.com"


def test_normalize_ip():
    assert normalize_and_validate_san("10.2.3.4") == "IP:10.2.3.4"
    assert normalize_and_validate_san("IP:10.2.3.4") == "IP:10.2.3.4"


def test_invalid_san_raises():
    with pytest.raises(ValueError):
        normalize_and_validate_san("*invalid_hostname*")


def test_cli_rejects_bad_san(tmp_path):
    # Generate a key
    from certctl import keygen, cli
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "bad@@@", "--out", str(out)])
    assert rc != 0
    assert not out.exists()
