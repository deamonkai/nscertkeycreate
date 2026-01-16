"""NetScaler Console NITRO API helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union

import requests
from urllib3.exceptions import InsecureRequestWarning

VerifyType = Union[bool, str]


class NitroError(RuntimeError):
    def __init__(self, status_code: int, message: str, payload: Any = None, headers: Any = None):
        super().__init__(f"NITRO error (HTTP {status_code}): {message}")
        self.status_code = status_code
        self.message = message
        self.payload = payload
        self.headers = headers


@dataclass
class NitroConsoleClient:
    base: str
    verify: VerifyType
    token: Optional[str] = None
    timeout: int = 60

    def __post_init__(self) -> None:
        if self.verify is False:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  # type: ignore[attr-defined]

    def _url(self, path: str) -> str:
        return self.base.rstrip("/") + path

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {"Accept": "*/*"}
        if self.token:
            headers["Cookie"] = f"NITRO_AUTH_TOKEN={self.token}"
        if extra:
            headers.update(extra)
        return headers

    def login(self, username: str, password: str) -> str:
        url = self._url("/nitro/v2/config/login")
        payload = {"login": {"username": username, "password": password}}
        resp = requests.post(
            url,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            json=payload,
            verify=self.verify,
            timeout=self.timeout,
        )
        data = self._parse_json(resp)
        try:
            session_id = data["login"][0]["sessionid"]
        except Exception as exc:  # pragma: no cover - defensive
            raise NitroError(resp.status_code, "Login response did not include sessionid", data) from exc
        if not session_id:
            raise NitroError(resp.status_code, "Login returned empty sessionid", data)
        self.token = session_id
        return session_id

    def _parse_json(self, resp: requests.Response) -> Dict[str, Any]:
        headers = dict(resp.headers)
        try:
            data = resp.json()
        except Exception:
            if resp.status_code >= 400:
                raise NitroError(resp.status_code, resp.text, headers=headers)
            raise NitroError(resp.status_code, "Expected JSON but got non-JSON response", headers=headers)

        if resp.status_code >= 400:
            msg = data.get("message") if isinstance(data, dict) else resp.text
            raise NitroError(resp.status_code, str(msg), data, headers=headers)

        if isinstance(data, dict):
            err = data.get("errorcode")
            if err not in (0, "0", None):
                msg = data.get("message", "Unknown NITRO error")
                raise NitroError(resp.status_code, str(msg), data, headers=headers)

        return data

    def get_json(self, path: str, *, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = self._url(path)
        resp = requests.get(
            url,
            headers=self._headers({"Accept": "application/json"}),
            params=params,
            verify=self.verify,
            timeout=self.timeout,
        )
        return self._parse_json(resp)

    def post_json(
        self,
        path: str,
        payload: Dict[str, Any],
        *,
        params: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        url = self._url(path)
        resp = requests.post(
            url,
            headers=self._headers({"Content-Type": "application/json", "Accept": "application/json"}),
            params=params,
            json=payload,
            verify=self.verify,
            timeout=self.timeout,
        )
        return self._parse_json(resp)

    def put_json(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = self._url(path)
        resp = requests.put(
            url,
            headers=self._headers({"Content-Type": "application/json", "Accept": "application/json"}),
            json=payload,
            verify=self.verify,
            timeout=self.timeout,
        )
        return self._parse_json(resp)

    def upload_file(self, path: str, file_path: str) -> Dict[str, Any]:
        url = self._url(path)
        with open(file_path, "rb") as handle:
            resp = requests.post(
                url,
                headers=self._headers(),
                files={"file": handle},
                verify=self.verify,
                timeout=self.timeout,
            )
        return self._parse_json(resp)

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
