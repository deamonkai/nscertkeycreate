"""Sectigo CA adapter skeleton.

This file provides a class with the expected interface. Implementing a full
Sectigo integration requires API credentials and network access; this is a
skeleton with TODOs and a clear place to add HTTP calls.
"""
from typing import Optional
from .base import CAAdapter


class SectigoCA(CAAdapter):
    def __init__(self, api_base: str = "https://api.sectigo.com", api_key: Optional[str] = None):
        self.api_base = api_base
        self.api_key = api_key

    def submit_csr(self, csr_pem: str, name: str, options: Optional[dict] = None) -> str:
        """Submit CSR to Sectigo and return request id.

        TODO: Implement actual HTTP POSTs with authentication and error handling.
        """
        raise NotImplementedError("Sectigo submission not implemented yet")

    def poll_status(self, request_id: str, timeout: int = 60) -> str:
        """Poll Sectigo for request status.

        TODO: implement polling logic using Sectigo APIs.
        """
        raise NotImplementedError("Sectigo polling not implemented yet")

    def download_certificate(self, request_id: str) -> str:
        """Download issued certificate PEM.

        TODO: fetch the issued certificate from Sectigo.
        """
        raise NotImplementedError("Sectigo download not implemented yet")
