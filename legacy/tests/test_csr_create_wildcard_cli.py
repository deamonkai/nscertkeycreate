"""Tests for CSR create when wildcard SANs are provided on the CLI."""
from certctl import cli


def test_cli_csr_create_cli_san_wildcard_interactive_confirm_yes(monkeypatch, tmp_path):
    from certctl import keygen, csr as csrmod
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Simulate interactive terminal and confirmation
    monkeypatch.setattr("builtins.input", lambda prompt='': "yes")
    import sys
    monkeypatch.setattr(sys.stdin, "isatty", lambda: True, raising=False)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "*.example.com", "--out", str(out)])
    assert rc == 0
    assert out.exists()
    csr_pem = out.read_text()
    assert csrmod.csr_has_san(csr_pem, "DNS:*.example.com")


def test_cli_csr_create_cli_san_wildcard_interactive_confirm_no(monkeypatch, tmp_path):
    from certctl import keygen, csr as csrmod
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Simulate interactive terminal and decline confirmation
    answers = iter(["no"])  # decline wildcard
    monkeypatch.setattr("builtins.input", lambda prompt='': next(answers))
    import sys
    monkeypatch.setattr(sys.stdin, "isatty", lambda: True, raising=False)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "*.example.com", "--out", str(out)])
    assert rc == 0
    assert out.exists()
    csr_pem = out.read_text()
    assert not csrmod.csr_has_san(csr_pem, "DNS:*.example.com")


def test_cli_csr_create_cli_san_wildcard_noninteractive_fails(monkeypatch, tmp_path):
    from certctl import keygen
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Simulate non-interactive (isatty False)
    import sys
    monkeypatch.setattr(sys.stdin, "isatty", lambda: False, raising=False)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--san", "*.example.com", "--out", str(out)])
    assert rc != 0


def test_cli_csr_create_cli_san_wildcard_allow_flag_noninteractive(monkeypatch, tmp_path):
    from certctl import keygen, csr as csrmod
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    import sys
    monkeypatch.setattr(sys.stdin, "isatty", lambda: False, raising=False)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "*.example.com", "--allow-wildcard", "--out", str(out)])
    assert rc == 0
    csr_pem = out.read_text()
    assert csrmod.csr_has_san(csr_pem, "DNS:*.example.com")
