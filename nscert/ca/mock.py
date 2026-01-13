"""A simple mock CA adapter for tests and local runs."""
from typing import Optional
from .base import CAAdapter


class MockCA(CAAdapter):
    def __init__(self):
        self._store = {}
        self._counter = 0

    def submit_csr(self, csr_pem: str, name: str, options: Optional[dict] = None) -> str:
        self._counter += 1
        rid = f"mock-{self._counter}"
        # store and pretend it's issued immediately for simplicity
        self._store[rid] = {
            "csr": csr_pem,
            "name": name,
            "status": "issued",
            "cert": f"-----BEGIN CERTIFICATE-----\nMockCertFor:{name}\n-----END CERTIFICATE-----\n",
        }
        return rid

    def poll_status(self, request_id: str, timeout: int = 60) -> str:
        return self._store.get(request_id, {}).get("status", "unknown")

    def download_certificate(self, request_id: str) -> str:
        return self._store.get(request_id, {}).get("cert")
