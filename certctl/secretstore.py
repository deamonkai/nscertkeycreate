"""Optional keychain helper using keyring when available."""

from __future__ import annotations

from typing import Optional

try:  # pragma: no cover - exercised when keyring is installed
    import keyring  # type: ignore
except Exception:  # pragma: no cover - keyring optional
    keyring = None  # type: ignore


def is_available() -> bool:
    return keyring is not None


def get_secret(service: str, username: str) -> Optional[str]:
    if keyring is None:
        return None
    try:
        return keyring.get_password(service, username)  # type: ignore
    except Exception:
        return None


def set_secret(service: str, username: str, value: str) -> None:
    if keyring is None:
        raise RuntimeError("keyring is not available (pip install keyring).")
    keyring.set_password(service, username, value)  # type: ignore


def delete_secret(service: str, username: str) -> None:
    if keyring is None:
        return
    try:
        keyring.delete_password(service, username)  # type: ignore
    except Exception:
        return
