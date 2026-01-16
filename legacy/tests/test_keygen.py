"""Tests for OpenSSL-based key generation helpers."""

import re
from certctl.keygen import generate_rsa_key, generate_ec_key, generate_private_key

# We accept PKCS#1 (RSA PRIVATE KEY), PKCS#8 (PRIVATE KEY) or encrypted forms.
PEM_PRIV_RE = re.compile(r"-----BEGIN [A-Z0-9 -]*PRIVATE KEY-----")


def test_generate_rsa_unencrypted():
    pem = generate_rsa_key(bits=2048)
    assert pem.strip().startswith("-----BEGIN")
    # basic sanity checks for PEM content
    assert "PRIVATE KEY" in pem or "RSA PRIVATE KEY" in pem
    assert "BEGIN" in pem and "END" in pem


def test_generate_rsa_encrypted():
    pem = generate_rsa_key(bits=2048, passphrase="s3cr3t")
    assert "ENCRYPTED" in pem or "ENCRYPTED PRIVATE KEY" in pem or "Proc-Type: 4,ENCRYPTED" in pem


def test_generate_ec_unencrypted():
    pem = generate_ec_key(curve="prime256v1")
    assert pem.strip().startswith("-----BEGIN")
    assert "PRIVATE KEY" in pem and "BEGIN" in pem and "END" in pem


def test_generate_ec_encrypted():
    pem = generate_ec_key(curve="secp384r1", passphrase="s3cr3t")
    assert "ENCRYPTED" in pem or "ENCRYPTED PRIVATE KEY" in pem


def test_generate_private_key_helper():
    pem = generate_private_key(kind="rsa", bits=2048)
    assert PEM_PRIV_RE.search(pem)

    pem2 = generate_private_key(kind="ec", curve="prime256v1")
    assert PEM_PRIV_RE.search(pem2)
