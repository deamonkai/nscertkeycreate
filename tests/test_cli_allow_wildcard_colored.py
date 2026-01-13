def test_allow_wildcard_warning_colored_when_tty(monkeypatch, tmp_path, capsys):
    from nscert import cli
    from nscert import keygen
    import sys

    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Simulate stderr being a TTY so colored output should be used
    monkeypatch.setattr(sys.stderr, "isatty", lambda: True, raising=False)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--subject", "/C=US/CN=example.com", "--san", "*.example.com", "--allow-wildcard", "--out", str(out)])
    captured = capsys.readouterr()
    assert rc == 0
    # ANSI bold yellow prefix
    assert "\033[1;33mWARNING: --allow-wildcard used" in captured.err
    # ANSI reset present
    assert "\033[0m" in captured.err
