#!/usr/bin/env python3
"""
nscertkeycreate.py

NetScaler Console key + CSR workflow:
- Create key on Console (RSA 4096 or ECDSA prime256v1 by default)
- Download key locally
- Generate CSR locally with OpenSSL (supports SAN)
- Optionally upload CSR back to Console

Fixes included:
- Login once to /nitro/v2/config/login; store sessionid token
- Use Cookie: NITRO_AUTH_TOKEN=<token> for subsequent requests (avoid CookieConflictError)
- Correct OpenSSL SAN config generation:
    [alt_names]
    DNS.1 = example.com
    DNS.2 = www.example.com
    IP.1  = 10.0.0.1
- Optional: --insecure disables TLS verification (curl -k equivalent)
- Optional: --ca-bundle for proper TLS verification with internal CA
- Keychain storage (Console password + key passphrase) via keyring (optional)
"""

import argparse
import datetime as _dt
import getpass
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import warnings
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

try:
    import requests
except ImportError:
    print("ERROR: This script requires 'requests'. Install with: pip install requests", file=sys.stderr)
    raise

try:
    import keyring  # type: ignore
except Exception:
    keyring = None  # type: ignore

APP = "nscertkeycreate"
DEFAULT_EC_CURVE = "prime256v1"
DEFAULT_RSA_BITS = 4096


class NitroError(RuntimeError):
    def __init__(self, status_code: int, message: str, payload: Any = None, headers: Any = None):
        super().__init__(f"NITRO error (HTTP {status_code}): {message}")
        self.status_code = status_code
        self.message = message
        self.payload = payload
        self.headers = headers


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def _safe_filename(name: str) -> str:
    name = name.strip().replace("/", "_").replace("\\", "_")
    return name


def _prompt_yes_no(prompt: str, default_yes: bool = True) -> bool:
    suffix = " [Y/n] " if default_yes else " [y/N] "
    while True:
        ans = input(prompt + suffix).strip().lower()
        if not ans:
            return default_yes
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise RuntimeError("OpenSSL not found in PATH. Install it (or ensure 'openssl' is available).")
    return path


def _run(cmd: list, *, input_bytes: Optional[bytes] = None, env: Optional[Dict[str, str]] = None) -> Tuple[int, bytes, bytes]:
    p = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE if input_bytes is not None else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    out, err = p.communicate(input=input_bytes)
    return p.returncode, out, err


def _keyring_available() -> bool:
    return keyring is not None


def _kr_service(console_url: str) -> str:
    return f"{APP}:{console_url.rstrip('/')}"


def keyring_get(console_url: str, username: str, which: str) -> Optional[str]:
    if not _keyring_available():
        return None
    try:
        return keyring.get_password(_kr_service(console_url), f"{username}:{which}")  # type: ignore
    except Exception:
        return None


def keyring_set(console_url: str, username: str, which: str, value: str) -> None:
    if not _keyring_available():
        raise RuntimeError("keyring is not available (pip install keyring).")
    keyring.set_password(_kr_service(console_url), f"{username}:{which}", value)  # type: ignore


def keyring_delete(console_url: str, username: str, which: str) -> None:
    if not _keyring_available():
        return
    try:
        keyring.delete_password(_kr_service(console_url), f"{username}:{which}")  # type: ignore
    except Exception:
        pass


VerifyType = Union[bool, str]


@dataclass
class NitroConsoleClient:
    base: str
    verify: VerifyType
    token: Optional[str] = None
    timeout: int = 60

    def _url(self, path: str) -> str:
        return self.base.rstrip("/") + path

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        h: Dict[str, str] = {"Accept": "*/*"}
        if self.token:
            h["Cookie"] = f"NITRO_AUTH_TOKEN={self.token}"
        if extra:
            h.update(extra)
        return h

    def login(self, username: str, password: str) -> str:
        url = self._url("/nitro/v2/config/login")
        payload = {"login": {"username": username, "password": password}}

        r = requests.post(
            url,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            json=payload,
            verify=self.verify,
            timeout=self.timeout,
        )

        try:
            j = r.json()
        except Exception:
            raise NitroError(r.status_code, r.text)

        if r.status_code >= 400:
            msg = j.get("message") if isinstance(j, dict) else r.text
            raise NitroError(r.status_code, str(msg), j)

        try:
            sess = j["login"][0]["sessionid"]
        except Exception:
            raise NitroError(r.status_code, "Login response did not include sessionid", j)

        if not isinstance(sess, str) or not sess:
            raise NitroError(r.status_code, "Login returned empty sessionid", j)

        self.token = sess
        return sess

    def _parse_json(self, r: requests.Response) -> Dict[str, Any]:
        headers = dict(r.headers)
        try:
            j = r.json()
        except Exception:
            if r.status_code >= 400:
                raise NitroError(r.status_code, r.text, headers=headers)
            raise NitroError(r.status_code, "Expected JSON but got non-JSON response", headers=headers)

        if r.status_code >= 400:
            msg = j.get("message") if isinstance(j, dict) else r.text
            raise NitroError(r.status_code, str(msg), j, headers=headers)

        if isinstance(j, dict) and "errorcode" in j and j.get("errorcode") not in (0, "0", None):
            msg = j.get("message", "Unknown NITRO error")
            raise NitroError(r.status_code, str(msg), j, headers=headers)

        return j

    def post_json(self, path: str, payload: Dict[str, Any], *, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = self._url(path)
        r = requests.post(
            url,
            headers=self._headers({"Content-Type": "application/json", "Accept": "application/json"}),
            params=params,
            json=payload,
            verify=self.verify,
            timeout=self.timeout,
        )
        return self._parse_json(r)

    def get_json(self, path: str, *, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = self._url(path)
        r = requests.get(
            url,
            headers=self._headers({"Accept": "application/json"}),
            params=params,
            verify=self.verify,
            timeout=self.timeout,
        )
        return self._parse_json(r)

    def download_bytes(self, path: str) -> bytes:
        url = self._url(path)
        r = requests.get(url, headers=self._headers(), verify=self.verify, timeout=self.timeout)
        if r.status_code >= 400:
            try:
                j = r.json()
                msg = j.get("message") or r.text
                raise NitroError(r.status_code, str(msg), j, headers=dict(r.headers))
            except ValueError:
                raise NitroError(r.status_code, r.text, headers=dict(r.headers))
        return r.content

    # High-level operations
    def create_key(
        self,
        key_name: str,
        *,
        algo: str,
        keyform: str = "PEM",
        keysize: Optional[int] = None,
        ec_curve: Optional[str] = None,
        password: Optional[str] = None,
        file_location_path: str = "",
    ) -> Dict[str, Any]:
        obj: Dict[str, Any] = {
            "file_name": key_name,
            "keyform": keyform,
            "algo": algo,
            "file_location_path": file_location_path,
        }
        if keysize is not None:
            obj["keysize"] = int(keysize)
        if ec_curve:
            obj["ec_curve"] = ec_curve
        if password:
            obj["password"] = password

        return self.post_json("/nitro/v2/config/ns_ssl_key", {"ns_ssl_key": obj}, params={"action": "create"})

    def download_key(self, key_name: str) -> bytes:
        return self.download_bytes(f"/nitro/v2/download/ns_ssl_key/{key_name}")


def _pick_key_type_interactive() -> Dict[str, Any]:
    print("Select key type:")
    print(f"  1) RSA {DEFAULT_RSA_BITS} (common/compatible)")
    print("  2) ECDSA (best-practice default curve) (default)")
    while True:
        sel = input("Select [1-2]: ").strip() or "2"
        if sel == "1":
            return {"algo": "RSA", "keysize": DEFAULT_RSA_BITS}
        if sel == "2":
            return {"algo": "ECDSA", "ec_curve": DEFAULT_EC_CURVE}
        print("Invalid selection. Choose 1 or 2.")


def _parse_san_string(san: str) -> Dict[str, list]:
    """
    Input: "DNS:example.com,DNS:www.example.com,IP:10.0.0.1"
    Output: {"DNS": ["example.com","www.example.com"], "IP": ["10.0.0.1"]}
    """
    out: Dict[str, list] = {}
    if not san.strip():
        return out

    items = [x.strip() for x in san.split(",") if x.strip()]
    for it in items:
        if ":" not in it:
            raise RuntimeError("SAN entry must be like DNS:example.com or IP:10.0.0.1 (comma-separated).")
        k, v = it.split(":", 1)
        k = k.strip().upper()
        v = v.strip()
        if k not in ("DNS", "IP", "EMAIL", "URI"):
            raise RuntimeError(f"Unsupported SAN type '{k}'. Use DNS, IP, EMAIL, or URI.")
        if not v:
            raise RuntimeError("SAN value cannot be empty.")
        out.setdefault(k, []).append(v)
    return out


def _openssl_make_csr(
    key_file: pathlib.Path,
    csr_file: pathlib.Path,
    *,
    cn: str,
    o: str = "",
    ou: str = "",
    l: str = "",
    st: str = "",
    c: str = "",
    san: str = "",
    passphrase: Optional[str] = None,
) -> None:
    openssl = _require_openssl()

    subj_parts = []
    if c:
        subj_parts.append(f"/C={c}")
    if st:
        subj_parts.append(f"/ST={st}")
    if l:
        subj_parts.append(f"/L={l}")
    if o:
        subj_parts.append(f"/O={o}")
    if ou:
        subj_parts.append(f"/OU={ou}")
    subj_parts.append(f"/CN={cn}")
    subj = "".join(subj_parts)

    extra_args = []
    with tempfile.TemporaryDirectory() as td:
        tdpath = pathlib.Path(td)

        san_map = _parse_san_string(san)

        cfg_path = None
        if san_map:
            cfg_path = tdpath / "openssl.cnf"
            lines = []
            lines += [
                "[ req ]",
                "default_md = sha256",
                "prompt = no",
                "distinguished_name = dn",
                "req_extensions = req_ext",
                "",
                "[ dn ]",
                f"CN = {cn}",
                "",
                "[ req_ext ]",
                "subjectAltName = @alt_names",
                "",
                "[ alt_names ]",
            ]

            # Correct OpenSSL alt_names syntax: DNS.1=, IP.1=, etc.
            for typ in ("DNS", "IP", "EMAIL", "URI"):
                vals = san_map.get(typ, [])
                for idx, v in enumerate(vals, start=1):
                    lines.append(f"{typ}.{idx} = {v}")

            cfg_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            extra_args = ["-config", str(cfg_path), "-reqexts", "req_ext"]

        cmd = [
            openssl, "req", "-new", "-sha256",
            "-key", str(key_file),
            "-out", str(csr_file),
            "-subj", subj,
        ] + extra_args

        if passphrase:
            env = os.environ.copy()
            env["NSCERTKEY_PASSPHRASE"] = passphrase
            cmd += ["-passin", "env:NSCERTKEY_PASSPHRASE"]
            rc, out, err = _run(cmd, env=env)
        else:
            rc, out, err = _run(cmd)

        if rc != 0:
            raise RuntimeError(f"OpenSSL CSR generation failed:\n{err.decode(errors='ignore')}")


def _write_file(path: pathlib.Path, data: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    try:
        os.chmod(path, mode)
    except Exception:
        pass


def _copy_latest(target: pathlib.Path, latest_name: str) -> None:
    latest = target.parent / latest_name
    try:
        if latest.exists():
            latest.unlink()
    except Exception:
        pass
    shutil.copy2(target, latest)


def _console_password_flow(console_url: str, username: str, reset: bool) -> str:
    if reset:
        keyring_delete(console_url, username, "console_password")

    pw = keyring_get(console_url, username, "console_password")
    if pw:
        return pw

    pw = getpass.getpass(f"Console password for {username}@{console_url}: ")
    if _keyring_available():
        if _prompt_yes_no("Store Console password in keychain?", default_yes=True):
            try:
                keyring_set(console_url, username, "console_password", pw)
            except Exception as e:
                print(f"[warn] Could not store Console password in keychain: {e}", file=sys.stderr)
    return pw


def _key_passphrase_flow(console_url: str, username: str, reset: bool, encrypt: bool) -> Optional[str]:
    if not encrypt:
        return None
    if reset:
        keyring_delete(console_url, username, "key_passphrase")

    pp = keyring_get(console_url, username, "key_passphrase")
    if pp:
        return pp

    pp = getpass.getpass("Key passphrase (will be stored in keychain if you choose): ")
    if _keyring_available():
        if _prompt_yes_no("Store key passphrase in keychain?", default_yes=True):
            try:
                keyring_set(console_url, username, "key_passphrase", pp)
            except Exception as e:
                print(f"[warn] Could not store key passphrase in keychain: {e}", file=sys.stderr)
    return pp


def _prompt_subject() -> Dict[str, str]:
    cn = input("CSR Common Name (CN): ").strip()
    if not cn:
        raise RuntimeError("CN is required.")
    o = input("Organization (O) [optional]: ").strip()
    ou = input("Org Unit (OU) [optional]: ").strip()
    l = input("City/Locality (L) [optional]: ").strip()
    st = input("State/Province (ST) [optional, spell out like 'Alabama' (not 'AL')]: ").strip()
    c = input("Country (C) 2-letter [optional]: ").strip()
    san = input("SubjectAltName string (e.g. DNS:example.com,DNS:www.example.com) [optional]: ").strip()
    return {"cn": cn, "o": o, "ou": ou, "l": l, "st": st, "c": c, "san": san}


def build_names(app_name: str, *, rotate: bool) -> Tuple[str, str]:
    app_name = _safe_filename(app_name)
    if rotate:
        stamp = _now_stamp()
        return f"{app_name}_{stamp}.key", f"{app_name}_{stamp}.csr"
    return f"{app_name}.key", f"{app_name}.csr"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--console", required=True)
    ap.add_argument("--user", required=True)
    ap.add_argument("--app-name", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--no-rotate", action="store_true")
    ap.add_argument("--no-latest", action="store_true")
    ap.add_argument("--insecure", action="store_true", help="Disable TLS verification (curl -k)")
    ap.add_argument("--ca-bundle", help="Path to CA bundle PEM file to trust Console's issuing CA")
    ap.add_argument("--reset-password", action="store_true")
    ap.add_argument("--reset-passphrase", action="store_true")
    args = ap.parse_args()

    console = args.console.rstrip("/")
    username = args.user
    out_dir = pathlib.Path(args.out_dir).expanduser().resolve()

    rotate = not args.no_rotate
    write_latest = not args.no_latest

    # TLS verification selection
    if args.ca_bundle:
        ca_path = str(pathlib.Path(args.ca_bundle).expanduser().resolve())
        verify: VerifyType = ca_path
    elif args.insecure:
        verify = False
        # avoid noisy urllib3 warnings if user explicitly requested insecure
        try:
            from urllib3.exceptions import InsecureRequestWarning  # type: ignore
            warnings.simplefilter("ignore", InsecureRequestWarning)
        except Exception:
            pass
    else:
        verify = True

    password = _console_password_flow(console, username, reset=args.reset_password)
    client = NitroConsoleClient(base=console, verify=verify)

    print("[console] Logging in to establish session (for download/upload authorization)...")
    client.login(username, password)
    print("[console] Login OK (session established).")

    key_name, csr_name = build_names(args.app_name, rotate=rotate)
    print("\n[info] Derived names:")
    print(f"       Key: {key_name}")
    print(f"       CSR: {csr_name}")
    print(f"       Rotate: {'ON' if rotate else 'OFF'}")
    print(f"       Write latest: {'ON' if write_latest else 'OFF'}")
    if not _prompt_yes_no("Proceed with these names?", default_yes=True):
        print("Aborted.")
        return 2

    kcfg = _pick_key_type_interactive()
    encrypt_key = _prompt_yes_no("Encrypt the private key with a passphrase?", default_yes=True)
    passphrase = _key_passphrase_flow(console, username, reset=args.reset_passphrase, encrypt=encrypt_key)
    subj = _prompt_subject()

    print("\n[console] Creating key on Console (never reuse keys)...")
    client.create_key(
        key_name,
        algo=kcfg.get("algo", ""),
        keyform="PEM",
        keysize=kcfg.get("keysize"),
        ec_curve=kcfg.get("ec_curve"),
        password=passphrase if encrypt_key else None,
    )
    print(f"[console] Key create accepted: {key_name}")

    print("\n[console] Downloading KEY via /nitro/v2/download ...")
    key_bytes = client.download_key(key_name)
    key_out = out_dir / key_name
    _write_file(key_out, key_bytes, 0o600)
    print(f"[local] Wrote key: {key_out}")
    if write_latest:
        _copy_latest(key_out, "latest.key")
        print(f"[local] Wrote latest.key -> {key_out.name}")

    print("\n[local] Generating CSR with OpenSSL...")
    csr_out = out_dir / csr_name
    _openssl_make_csr(
        key_out, csr_out,
        cn=subj["cn"], o=subj["o"], ou=subj["ou"], l=subj["l"], st=subj["st"], c=subj["c"],
        san=subj["san"],
        passphrase=passphrase if encrypt_key else None,
    )
    try:
        os.chmod(csr_out, 0o644)
    except Exception:
        pass
    print(f"[local] Wrote CSR: {csr_out}")
    if write_latest:
        _copy_latest(csr_out, "latest.csr")
        print(f"[local] Wrote latest.csr -> {csr_out.name}")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())