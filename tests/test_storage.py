"""Tests for macOS Keychain helpers in `certctl.storage`.

These tests stub out `subprocess.run` and `getpass.getpass` to simulate
macOS behavior.
"""
import subprocess
from certctl import storage


class DummyCompleted:
    def __init__(self, out=b""):
        self.stdout = out


def test_keychain_get_found(monkeypatch):
    def fake_run(args, check, capture_output):
        return DummyCompleted(out=b"s3cr3t\n")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert storage.keychain_get("svc-1") == "s3cr3t"


def test_keychain_get_not_found(monkeypatch):
    def fake_run(args, check, capture_output):
        raise subprocess.CalledProcessError(1, args)

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert storage.keychain_get("svc-missing") is None


def test_get_or_prompt_passphrase_stores(monkeypatch):
    # Simulate nothing in keychain, then interactive prompt, then store called
    def fake_run_find(args, check, capture_output):
        raise subprocess.CalledProcessError(1, args)

    stored = {}

    def fake_set(service, password, account="certctl"):
        stored[service] = password
        return True

    monkeypatch.setattr(subprocess, "run", fake_run_find)
    monkeypatch.setattr(storage, "keychain_set", fake_set)
    monkeypatch.setattr("getpass.getpass", lambda prompt: "typed-pass")

    val = storage.get_or_prompt_passphrase("myservice", prompt="enter:")
    assert val == "typed-pass"
    assert stored.get("myservice") == "typed-pass"
