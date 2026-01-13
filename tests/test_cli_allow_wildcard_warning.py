def test_allow_wildcard_warning_prints(monkeypatch, tmp_path, capsys):
    from nscert import cli
    from nscert import keygen

    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "*.example.com", "--allow-wildcard", "--out", str(out)])
    captured = capsys.readouterr()
    assert rc == 0
    assert "WARNING: --allow-wildcard used" in captured.err
