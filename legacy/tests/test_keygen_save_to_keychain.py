"""Tests verifying passphrase save-to-keychain behavior for keygen."""
from certctl import keygen


def test_save_rsa_passphrase_to_keychain(monkeypatch):
    # stub openssl path to avoid requiring a specific binary
    monkeypatch.setattr(keygen, "_openssl_bin", lambda: "/usr/bin/openssl")

    called = {}

    def fake_set(service, password, account="certctl"):
        called['service'] = service
        called['password'] = password
        called['account'] = account
        return True

    monkeypatch.setattr("certctl.storage.keychain_set", fake_set)

    # Provide passphrase and request save to keychain
    pem = keygen.generate_rsa_key(bits=1024, passphrase="savetest", keychain_service="svc-save", save_to_keychain=True, keychain_account="acct1")

    assert called['service'] == "svc-save"
    assert called['password'] == "savetest"
    assert called['account'] == "acct1"


def test_save_ec_passphrase_to_keychain(monkeypatch):
    monkeypatch.setattr(keygen, "_openssl_bin", lambda: "/usr/bin/openssl")

    called = {}

    def fake_set(service, password, account="certctl"):
        called['service'] = service
        called['password'] = password
        called['account'] = account
        return True

    monkeypatch.setattr("certctl.storage.keychain_set", fake_set)

    pem = keygen.generate_ec_key(curve="prime256v1", passphrase="ecsave", keychain_service="svc-save-ec", save_to_keychain=True)

    assert called['service'] == "svc-save-ec"
    assert called['password'] == "ecsave"
