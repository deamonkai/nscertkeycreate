"""NetScaler Console (ADM/Console) NITRO helpers.

Design goals:
- Log in ONCE to obtain a session token ("sessionid" in the login response).
- Use that token on subsequent requests (Cookie: NITRO_AUTH_TOKEN=...).
- Keep credentials out of git: caller can provide password via keychain/env.

Notes:
- In some Console builds, download endpoints authorize *only* via the cookie,
  even if Basic auth / X-NITRO headers are supplied.
- Requests' cookie jar can contain multiple cookies with the same name but
  different paths, leading to CookieConflictError. To avoid that entire class
  of issues, we do not rely on the cookie jar; we store the token ourselves
  and set the Cookie header explicitly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


class NitroError(RuntimeError):
    def __init__(self, status: int, message: str, payload: Any | None = None, headers: Dict[str, str] | None = None):
        super().__init__(f"NITRO error (HTTP {status}): {message}")
        self.status = status
        self.message = message
        self.payload = payload
        self.headers = headers or {}


@dataclass
class ConsoleSession:
    base_url: str
    username: str
    password: str
    insecure: bool = False
    timeout: int = 30

    _token: Optional[str] = None
    _http: Optional[requests.Session] = None

    def _sess(self) -> requests.Session:
        if self._http is None:
            self._http = requests.Session()
        return self._http

    @property
    def token(self) -> str:
        if not self._token:
            raise RuntimeError("Not logged in yet")
        return self._token

    def login(self) -> str:
        """Login and return the session token (NITRO_AUTH_TOKEN value)."""
        url = f"{self.base_url.rstrip('/')}/nitro/v2/config/login"
        payload = {"login": {"username": self.username, "password": self.password}}

        r = requests.post(
            url,
            json=payload,
            auth=(self.username, self.password),
            verify=not self.insecure,
            timeout=self.timeout,
        )

        try:
            j = r.json()
        except Exception:
            raise NitroError(r.status_code, r.text)

        if r.status_code >= 400 or (isinstance(j, dict) and j.get("errorcode") not in (None, 0)):
            msg = j.get("message") if isinstance(j, dict) else str(j)
            raise NitroError(r.status_code, msg or "Login failed", j)

        try:
            token = j["login"][0]["sessionid"]
        except Exception:
            raise NitroError(r.status_code, "Login response missing sessionid", j)

        self._token = token
        return token

    # ---------------------- low-level HTTP helpers ----------------------

    def _headers(self, extra: Optional[Dict[str, str]] = None, include_auth_headers: bool = True) -> Dict[str, str]:
        h: Dict[str, str] = {}
        if self._token:
            h["Cookie"] = f"NITRO_AUTH_TOKEN={self._token}"
        if include_auth_headers:
            h["X-NITRO-USER"] = self.username
            h["X-NITRO-PASS"] = self.password
        if extra:
            h.update(extra)
        return h

    def request(self, method: str, path: str, *, params: Dict[str, str] | None = None,
                json_body: Any | None = None, data: Any | None = None,
                headers: Dict[str, str] | None = None,
                include_auth_headers: bool = True,
                stream: bool = False) -> requests.Response:
        if not self._token:
            self.login()

        url = f"{self.base_url.rstrip('/')}{path}"
        r = self._sess().request(
            method,
            url,
            params=params,
            json=json_body,
            data=data,
            headers=self._headers(headers, include_auth_headers=include_auth_headers),
            verify=not self.insecure,
            timeout=self.timeout,
            stream=stream,
        )
        return r

    def _raise_for_nitro(self, r: requests.Response) -> None:
        if r.status_code < 400:
            return
        # try to decode JSON error payload
        msg = r.text
        payload: Any = None
        try:
            payload = r.json()
            if isinstance(payload, dict) and "message" in payload:
                msg = payload.get("message") or msg
        except Exception:
            payload = None
        raise NitroError(r.status_code, msg, payload, headers=dict(r.headers))

    # ---------------------- Console operations we need ----------------------

    def create_ssl_key(self, *, file_name: str, algo: str, keysize: int | None = None,
                       ec_curve: str | None = None, keyform: str = "PEM",
                       encrypt: bool = False, passphrase: str | None = None,
                       des_type: str = "AES256") -> Dict[str, Any]:
        """Create a private key file stored on Console.

        This maps to the ns_ssl_key resource in Console NITRO v2.
        We send form-urlencoded with an `object=` payload because Console
        rejects raw JSON for some POSTs.
        """
        obj: Dict[str, Any] = {
            "file_name": file_name,
            "keyform": keyform,
            "algo": algo,
        }
        if keysize is not None:
            obj["keysize"] = str(keysize)
        if ec_curve:
            obj["ec_curve"] = ec_curve
        if encrypt:
            # Console uses des_type naming even for AES in some builds
            obj["des_type"] = des_type
            if passphrase:
                obj["passphrase"] = passphrase

        payload = {"ns_ssl_key": obj}
        data = {"object": json.dumps(payload)}

        r = self.request(
            "POST",
            "/nitro/v2/config/ns_ssl_key",
            params={"action": "create"},
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        self._raise_for_nitro(r)
        return r.json()

    def download_file(self, resource: str, file_name: str) -> bytes:
        """Download a stored file via /nitro/v2/download/<resource>/<file_name>."""
        # For download endpoints, some builds want ONLY the cookie.
        r = self.request(
            "GET",
            f"/nitro/v2/download/{resource}/{file_name}",
            include_auth_headers=False,
            stream=True,
        )
        self._raise_for_nitro(r)
        return r.content

    def list_ssl_certkeys(self, *, attrs: str | None = None) -> Dict[str, Any]:
        """List certificate-key objects stored on Console.

        This uses the Console NITRO resource `ns_ssl_certkey`.
        The response includes expiry-related fields such as `valid_to`
        and `days_to_expiry` (stringified).
        """
        params: Dict[str, str] = {}
        if attrs:
            params["attrs"] = attrs
        r = self.request("GET", "/nitro/v2/config/ns_ssl_certkey", params=params)
        self._raise_for_nitro(r)
        return r.json()
