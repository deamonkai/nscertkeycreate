"""Tests for CSR creation using OpenSSL CLI."""
import tempfile
from nscert import keygen
from nscert import csr


def test_create_csr_with_san(tmp_path):
    # Generate a temporary key
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "test.key"
    key_file.write_text(key_pem)

    subject = {"C": "US", "ST": "CA", "CN": "example.com"}
    sans = ["www.example.com", "10.0.0.1"]

    csr_pem = csr.create_csr_from_key(str(key_file), subject=subject, sans=sans)
    assert csr_pem.startswith("-----BEGIN CERTIFICATE REQUEST-----")

    # Ensure SANs are present in the CSR
    assert csr.csr_has_san(csr_pem, "DNS:www.example.com")
    assert csr.csr_has_san(csr_pem, "IP:10.0.0.1")
