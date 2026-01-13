"""Integration tests to verify keygen resolves passphrases from keychain."""
from nscert import keygen


def test_generate_rsa_using_keychain(monkeypatch):
    # Return a known passphrase from keychain and ensure result is encrypted
    monkeypatch.setattr(keygen, "_openssl_bin", lambda: "/usr/bin/openssl")

    def fake_keychain_get(service):
        assert service == "svc1"
        return "from-keychain"

    monkeypatch.setattr("nscert.storage.keychain_get", fake_keychain_get)

    pem = keygen.generate_rsa_key(bits=1024, passphrase=None, keychain_service="svc1")
    assert "ENCRYPTED" in pem or "ENCRYPTED PRIVATE KEY" in pem


def test_generate_ec_using_keychain(monkeypatch):
    monkeypatch.setattr(keygen, "_openssl_bin", lambda: "/usr/bin/openssl")

    def fake_keychain_get(service):
        assert service == "svc2"
        return "from-keychain"

    monkeypatch.setattr("nscert.storage.keychain_get", fake_keychain_get)

    pem = keygen.generate_ec_key(curve="prime256v1", passphrase=None, keychain_service="svc2")
    assert "ENCRYPTED" in pem or "ENCRYPTED PRIVATE KEY" in pem
