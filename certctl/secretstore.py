"""Small secret storage abstraction.

For now:
- macOS: uses the built-in Keychain via the `security` CLI.
- other OSes: prompts only (no persistent storage) unless CERTCTL_* env vars used.

This keeps dependencies minimal and avoids coupling to a specific enterprise vault.
"""

from __future__ import annotations

import os
import platform
import subprocess
from typing import Optional


def _is_macos() -> bool:
    return platform.system().lower() == "darwin"


def get_from_keychain(service: str, account: str) -> Optional[str]:
    if not _is_macos():
        return None
    try:
        # -w prints password only
        out = subprocess.check_output(
            ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return None


def set_in_keychain(service: str, account: str, secret: str) -> None:
    if not _is_macos():
        return
    # Add or update
    subprocess.check_call(
        [
            "security",
            "add-generic-password",
            "-U",
            "-s",
            service,
            "-a",
            account,
            "-w",
            secret,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def env_or_keychain(env_var: str, service: str, account: str) -> Optional[str]:
    v = os.environ.get(env_var)
    if v:
        return v
    return get_from_keychain(service, account)
