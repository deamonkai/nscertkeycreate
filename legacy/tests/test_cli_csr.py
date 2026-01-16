"""Tests for CLI CSR commands."""
import subprocess
from certctl import cli


def test_cli_csr_create_and_show(monkeypatch, tmp_path):
    # Generate a key and write to file
    from certctl import keygen
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    out = tmp_path / "req.csr"

    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/ST=CA/CN=example.com", "--san", "www.example.com", "--san", "10.0.0.1", "--out", str(out)])
    assert rc == 0
    assert out.exists()

    # Show prints text; just call show to ensure no exception
    rc2 = cli.main(["csr", "show", "--csr-file", str(out)])
    assert rc2 == 0
