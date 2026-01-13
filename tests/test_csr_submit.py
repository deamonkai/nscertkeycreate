"""Tests for CSR submit flow using the Mock CA adapter."""
from nscert import cli
from nscert.ca.mock import MockCA


def test_csr_submit_mock(tmp_path):
    # Create a key and a CSR
    from nscert import keygen, csr
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    csr_pem = csr.create_csr_from_key(str(key_file), subject={"C": "US", "CN": "test.local"}, sans=["www.test.local"])
    csr_file = tmp_path / "r.csr"
    csr_file.write_text(csr_pem)

    # Submit via CLI using mock adapter
    rc = cli.main(["csr", "submit", "--csr-file", str(csr_file), "--ca", "mock", "--name", "testreq", "--wait"]) 
    assert rc == 0


def test_csr_submit_reject_wildcard(tmp_path):
    from nscert import keygen, csr
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    csr_pem = csr.create_csr_from_key(str(key_file), subject={"C": "US", "CN": "test.local"}, sans=["*.example.com"])
    csr_file = tmp_path / "r.csr"
    csr_file.write_text(csr_pem)

    rc = cli.main(["csr", "submit", "--csr-file", str(csr_file), "--ca", "mock", "--name", "testreq"]) 
    assert rc != 0

    # Allow wildcard
    rc2 = cli.main(["csr", "submit", "--csr-file", str(csr_file), "--ca", "mock", "--name", "testreq", "--allow-wildcard", "--wait"]) 
    assert rc2 == 0
