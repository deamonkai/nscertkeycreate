"""Sectigo (Cert Manager) adapter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

from .base import CAAdapter, CertStatus, SubmitResult


@dataclass
class SectigoConfig:
    base_url: str
    login: str
    password: str
    customer_uri: str
    org_id: int
    cert_type: int
    term_days: int
    verify: object = True


class SectigoAdapter(CAAdapter):
    name = "sectigo"

    def __init__(self, config: SectigoConfig):
        self.config = config

    def _headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json;charset=UTF-8",
            "login": self.config.login,
            "password": self.config.password,
            "customerUri": self.config.customer_uri,
        }

    def submit_csr(self, csr_pem: str, **kwargs: Any) -> SubmitResult:
        payload: Dict[str, Any] = {
            "orgId": self.config.org_id,
            "csr": csr_pem,
            "certType": self.config.cert_type,
            "term": self.config.term_days,
        }
        subj_alt_names = kwargs.get("subj_alt_names")
        if subj_alt_names:
            payload["subjAltNames"] = subj_alt_names
        resp = requests.post(
            f"{self.config.base_url.rstrip('/')}/api/ssl/v1/enroll",
            headers=self._headers(),
            json=payload,
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        ssl_id = data.get("sslId")
        if ssl_id is None:
            raise RuntimeError(f"Sectigo response missing sslId: {data}")
        return SubmitResult(request_id=str(ssl_id), ca=self.name)

    def poll_status(self, request_id: str) -> CertStatus:
        resp = requests.get(
            f"{self.config.base_url.rstrip('/')}/api/ssl/v1/{request_id}",
            headers=self._headers(),
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status", "Unknown")
        return CertStatus(status=status, raw=data)

    def collect_certificate(self, request_id: str, *, format_name: Optional[str] = None) -> str:
        fmt = format_name or "pem"
        resp = requests.get(
            f"{self.config.base_url.rstrip('/')}/api/ssl/v1/collect/{request_id}",
            headers=self._headers(),
            params={"format": fmt},
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.text
