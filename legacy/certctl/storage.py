"""Credential storage abstraction for macOS Keychain.

Provides small helpers to get/set generic passwords using the `security`
command on macOS. Functions are intentionally simple and easily testable via
stubbing subprocess calls.
"""
from typing import Optional
import subprocess
import shlex
import getpass


def keychain_get(service: str) -> Optional[str]:
    """Return the password for `service` from macOS Keychain, or None if not found."""
    try:
        # 'security find-generic-password -s <service> -w' prints the password
        completed = subprocess.run(["security", "find-generic-password", "-s", service, "-w"], check=True, capture_output=True)
        return completed.stdout.decode("utf-8").rstrip("\n")
    except subprocess.CalledProcessError:
        return None


def keychain_set(service: str, password: str, account: str = "certctl") -> bool:
    """Set a generic password in the Keychain for the given service."""
    # Use -U to update if exists
    try:
        subprocess.run(["security", "add-generic-password", "-a", account, "-s", service, "-w", password, "-U"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def keychain_delete(service: str) -> bool:
    try:
        subprocess.run(["security", "delete-generic-password", "-s", service], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def get_or_prompt_passphrase(service: Optional[str], prompt: Optional[str] = None) -> str:
    """Get passphrase from keychain or prompt the user interactively.

    If `service` is provided, on a user-entered passphrase we attempt to store
    it back into the Keychain for future use.
    """
    if service:
        existing = keychain_get(service)
        if existing:
            return existing

    # Fallback to interactive prompt
    text = getpass.getpass(prompt or "Enter passphrase for private key: ")

    if service and text:
        # best effort: set into keychain but ignore failures
        try:
            keychain_set(service, text)
        except Exception:
            pass

    return text
