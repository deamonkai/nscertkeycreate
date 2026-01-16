"""CA adapter interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class SubmitResult:
    request_id: str
    ca: str


@dataclass
class CertStatus:
    status: str
    raw: dict


class CAAdapter:
    name: str

    def submit_csr(self, csr_pem: str, **kwargs) -> SubmitResult:
        raise NotImplementedError

    def poll_status(self, request_id: str) -> CertStatus:
        raise NotImplementedError

    def collect_certificate(self, request_id: str, *, format_name: Optional[str] = None) -> str:
        raise NotImplementedError
