"""Minimal Netscaler Console helpers.

This module provides a thin wrapper around the extractor and a clear place to
add Console-specific parsing and upload helpers later.
"""
from typing import Optional

from .utils import extract_pem_from_json


def extract_csr_text(response_json: dict) -> Optional[str]:
    """Return CSR PEM text from a Console/device response JSON.

    Prioritize the Console `ns_ssl_csr` response shape, then fall back to a
    recursive search for the PEM block.
    """
    if not isinstance(response_json, dict):
        return extract_pem_from_json(response_json)

    # Prefer well-known ns_ssl_csr array
    ns_ssl_csr = response_json.get("ns_ssl_csr")
    if isinstance(ns_ssl_csr, list):
        for entry in ns_ssl_csr:
            if isinstance(entry, dict):
                csr = entry.get("csr")
                if csr:
                    found = extract_pem_from_json(csr)
                    if found:
                        return found

    # Fallback general search
    return extract_pem_from_json(response_json)
