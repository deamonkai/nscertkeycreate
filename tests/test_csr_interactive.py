"""Tests for interactive CSR prompting."""
from nscert import csr


def test_prompt_for_subject_and_sans(monkeypatch):
    answers = iter([
        "US",    # C
        "CA",    # ST
        "",      # L
        "Example Org", # O
        "",      # OU
        "example.com", # CN
        "www.example.com", # SAN 1
        "10.0.0.1",       # SAN 2
        ""                # finish
    ])

    monkeypatch.setattr("builtins.input", lambda prompt='': next(answers))

    subj, sans = csr.prompt_for_subject_and_sans()
    assert subj["C"] == "US"
    assert subj["ST"] == "CA"
    assert subj["O"] == "Example Org"
    assert subj["CN"] == "example.com"
    # prompt now returns normalized SANs like DNS:... or IP:...
    assert "DNS:www.example.com" in sans
    assert "IP:10.0.0.1" in sans


def test_cli_csr_create_interactive(monkeypatch, tmp_path):
    # Generate a key
    from nscert import keygen, cli
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Simulate interactive inputs (subject fields + SANs)
    answers = iter([
        "US",    # C
        "CA",    # ST
        "",      # L
        "Example Org", # O
        "",      # OU
        "example.com", # CN
        "www.example.com", # SAN 1
        "10.0.0.1",       # SAN 2
        ""                # finish
    ])
    monkeypatch.setattr("builtins.input", lambda prompt='': next(answers))

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--out", str(out)])
    assert rc == 0
    assert out.exists()

    # Target SAN should be present
    from nscert import csr as csrmod
    csr_pem = out.read_text()
    assert csrmod.csr_has_san(csr_pem, "DNS:www.example.com")
    assert csrmod.csr_has_san(csr_pem, "IP:10.0.0.1")


def test_prompt_for_subject_and_sans_wildcard_confirm_yes(monkeypatch):
    answers = iter([
        "US",    # C
        "CA",    # ST
        "",      # L
        "Example Org", # O
        "",      # OU
        "example.com", # CN
        "*.example.com", # SAN 1 (wildcard)
        "yes",  # confirm wildcard
        "",     # finish
    ])

    monkeypatch.setattr("builtins.input", lambda prompt='': next(answers))

    subj, sans = csr.prompt_for_subject_and_sans()
    assert subj["C"] == "US"
    assert any(s.startswith("DNS:*.example.com") for s in sans)


def test_prompt_for_subject_and_sans_wildcard_confirm_no(monkeypatch):
    answers = iter([
        "US",    # C
        "CA",    # ST
        "",      # L
        "Example Org", # O
        "",      # OU
        "example.com", # CN
        "*.example.com", # SAN 1 (wildcard)
        "no",   # do not confirm
        "www.example.com", # SAN 2
        "",     # finish
    ])

    monkeypatch.setattr("builtins.input", lambda prompt='': next(answers))

    subj, sans = csr.prompt_for_subject_and_sans()
    assert subj["C"] == "US"
    assert not any(s.startswith("DNS:*.example.com") for s in sans)
    assert any(s.startswith("DNS:www.example.com") for s in sans)
