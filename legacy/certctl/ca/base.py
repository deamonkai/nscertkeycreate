"""Base CA adapter interface."""
from typing import Protocol, Optional


class CAAdapter(Protocol):
    def submit_csr(self, csr_pem: str, name: str, options: Optional[dict] = None) -> str:
        """Submit a CSR and return a request id or token."""

    def poll_status(self, request_id: str, timeout: int = 60) -> str:
        """Poll request status and return a final state string (e.g., 'issued' / 'pending' / 'failed')."""

    def download_certificate(self, request_id: str) -> str:
        """Return the issued certificate PEM for the request_id."""
