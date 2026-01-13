"""Key generation helpers using the OpenSSL CLI.

This module intentionally uses the system `openssl` command for portability on
macOS systems where the `cryptography` library may not be available by
default.

Functions return the PEM text of the generated private key.
"""
from typing import Optional
import shutil
import subprocess


class OpenSSLNotFound(Exception):
    pass


def _openssl_bin() -> str:
    path = shutil.which("openssl")
    if not path:
        raise OpenSSLNotFound("`openssl` not found in PATH")
    return path


def generate_rsa_key(bits: int = 4096, passphrase: Optional[str] = None, cipher: Optional[str] = "des3", keychain_service: Optional[str] = None, save_to_keychain: bool = False, keychain_account: str = "nscert") -> str:
    """Generate an RSA private key in PEM format.

    If `passphrase` is provided or available in `keychain_service`, the PEM
    will be encrypted with the provided `cipher` (defaults to 3DES via
    OpenSSL's `des3` v2 option).

    If `save_to_keychain` is True and `keychain_service` is provided and a
    passphrase was supplied by the caller, the passphrase will be saved into
    the macOS Keychain using `nscert.storage.keychain_set`.

    Returns PEM text.
    """
    # Optionally save provided passphrase to keychain
    if passphrase and keychain_service and save_to_keychain:
        try:
            from . import storage
            storage.keychain_set(keychain_service, passphrase, account=keychain_account)
        except Exception:
            # Best-effort only; do not fail the key generation on keychain errors
            pass

    # Resolve passphrase via keychain if requested and not provided
    if not passphrase and keychain_service:
        try:
            from . import storage
            passphrase = storage.keychain_get(keychain_service)
        except Exception:
            pass

    openssl = _openssl_bin()

    # Generate an unencrypted private key into stdout using genpkey
    gen_cmd = [openssl, "genpkey", "-algorithm", "RSA", "-pkeyopt", f"rsa_keygen_bits:{bits}", "-outform", "PEM"]

    gen = subprocess.run(gen_cmd, check=True, capture_output=True)
    private_pem = gen.stdout

    if passphrase:
        # Convert to PKCS#8 and encrypt
        # Use -v2 <cipher> for modern encryption (des3 corresponds to 3DES)
        topk8_cmd = [openssl, "pkcs8", "-topk8", "-v2", cipher, "-passout", f"pass:{passphrase}", "-outform", "PEM"]
        topk8 = subprocess.run(topk8_cmd, input=private_pem, check=True, capture_output=True)
        return topk8.stdout.decode("utf-8")

    return private_pem.decode("utf-8")


def generate_ec_key(curve: str = "prime256v1", passphrase: Optional[str] = None, cipher: Optional[str] = "des3", keychain_service: Optional[str] = None, save_to_keychain: bool = False, keychain_account: str = "nscert") -> str:
    """Generate an EC private key (PEM) for given curve name (e.g., prime256v1 / secp384r1).

    If `passphrase` is provided or available in `keychain_service`, the PEM
    will be encrypted using PKCS#8 v2.

    If `save_to_keychain` is True and `keychain_service` is provided and a
    passphrase was supplied by the caller, the passphrase will be saved into
    the macOS Keychain using `nscert.storage.keychain_set`.
    """
    # Optionally save provided passphrase to keychain
    if passphrase and keychain_service and save_to_keychain:
        try:
            from . import storage
            storage.keychain_set(keychain_service, passphrase, account=keychain_account)
        except Exception:
            pass

    # Resolve passphrase via keychain if requested and not provided
    if not passphrase and keychain_service:
        try:
            from . import storage
            passphrase = storage.keychain_get(keychain_service)
        except Exception:
            pass

    openssl = _openssl_bin()

    gen_cmd = [openssl, "ecparam", "-name", curve, "-genkey", "-noout", "-outform", "PEM"]
    gen = subprocess.run(gen_cmd, check=True, capture_output=True)
    private_pem = gen.stdout

    if passphrase:
        topk8_cmd = [openssl, "pkcs8", "-topk8", "-v2", cipher, "-passout", f"pass:{passphrase}", "-outform", "PEM"]
        topk8 = subprocess.run(topk8_cmd, input=private_pem, check=True, capture_output=True)
        return topk8.stdout.decode("utf-8")

    return private_pem.decode("utf-8")


def generate_private_key(kind: str = "rsa", **kwargs) -> str:
    """Generic helper to generate a private key of a given `kind` ('rsa' or 'ec')."""
    kind = kind.lower()
    if kind == "rsa":
        return generate_rsa_key(**kwargs)
    if kind == "ec":
        return generate_ec_key(**kwargs)
    raise ValueError("Unsupported key kind: use 'rsa' or 'ec'")
