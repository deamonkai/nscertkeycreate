"""Utility helpers for certctl package.

Includes a robust PEM extractor that searches arbitrary Console JSON payloads
for a PEM CSR block (-----BEGIN CERTIFICATE REQUEST----- ...
-----END CERTIFICATE REQUEST-----).
"""

from typing import Optional, Any, TextIO
import re
import sys

PEM_RE = re.compile(r"-----BEGIN CERTIFICATE REQUEST-----(?:.|\n)+?-----END CERTIFICATE REQUEST-----", re.DOTALL)


# Compatibility exports: delegate terminal formatting to certctl.term
from .term import format_warning, print_warning, format_error, print_error, format_info, print_info  # re-exported for backwards compatibility



def extract_pem_from_json(obj: Any) -> Optional[str]:
    """Recursively search `obj` (dict/list/str) for the first PEM CSR block.

    Returns the matched PEM string or None if not found.
    """
    if isinstance(obj, str):
        m = PEM_RE.search(obj)
        if m:
            return m.group(0)
        return None

    if isinstance(obj, dict):
        # check common CSR locations quickly
        # e.g., {"ns_ssl_csr": [{"csr": "-----BEGIN..."}]}
        if "ns_ssl_csr" in obj:
            val = obj.get("ns_ssl_csr")
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, dict):
                        csr = item.get("csr")
                        if csr:
                            m = PEM_RE.search(csr)
                            if m:
                                return m.group(0)
        # generic recursive walk
        for v in obj.values():
            res = extract_pem_from_json(v)
            if res:
                return res

    if isinstance(obj, list):
        # If it's a list of strings (rows), join them and search the whole block
        if all(isinstance(i, str) for i in obj):
            joined = "\n".join(obj)
            m = PEM_RE.search(joined)
            if m:
                return m.group(0)
        for item in obj:
            res = extract_pem_from_json(item)
            if res:
                return res

    return None
