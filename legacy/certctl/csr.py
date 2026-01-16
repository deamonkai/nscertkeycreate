"""CSR generation helpers.

We intentionally generate CSRs *locally* (OpenSSL) rather than via Console
because "ns_ssl_csr" is not supported in some Console deployments.

All outputs are PEM.
"""

from __future__ import annotations

import ipaddress
import re
import subprocess
from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class Subject:
    cn: str
    o: str = ""
    ou: str = ""
    l: str = ""
    st: str = ""
    c: str = ""

    def to_openssl_subj(self) -> str:
        # Keep ordering stable; omit empty parts.
        parts = [("CN", self.cn), ("O", self.o), ("OU", self.ou), ("L", self.l), ("ST", self.st), ("C", self.c)]
        s = ""
        for k, v in parts:
            if v:
                # OpenSSL expects slashes; escape slashes in values.
                v = v.replace("/", "\\/")
                s += f"/{k}={v}"
        return s or f"/CN={self.cn}"


_SAN_SPLIT = re.compile(r"\s*,\s*|")


def parse_san_entries(raw: str) -> List[str]:
    """Parse a SAN string into OpenSSL-compatible entries.

    Accepts input like:
      - "DNS:example.com,DNS:www.example.com,IP:10.0.0.1"
      - "example.com, www.example.com" (bare names become DNS:...)

    Returns entries like ["DNS:example.com", "DNS:www.example.com", "IP:10.0.0.1"].

    Raises ValueError if any entry is malformed.
    """
    if not raw:
        return []

    # Split on commas; tolerate accidental whitespace.
    items = [x.strip() for x in raw.split(",") if x.strip()]
    out: List[str] = []
    for item in items:
        if ":" not in item:
            # Bare value: infer DNS unless it's an IP.
            try:
                ipaddress.ip_address(item)
                out.append(f"IP:{item}")
                continue
            except ValueError:
                out.append(f"DNS:{item}")
                continue

        prefix, value = item.split(":", 1)
        prefix_u = prefix.strip().upper()
        value = value.strip()
        if prefix_u in {"DNS", "IP"}:
            if not value:
                raise ValueError(f"Empty SAN value in '{item}'")
            if prefix_u == "IP":
                try:
                    ipaddress.ip_address(value)
                except ValueError:
                    raise ValueError(f"Invalid IP SAN: '{item}'")
            out.append(f"{prefix_u}:{value}")
        else:
            raise ValueError(
                f"Unsupported SAN type '{prefix}' in '{item}'. Use DNS: or IP: (or bare hostnames)."
            )
    return out


def make_csr_openssl(
    *,
    key_pem_path: str,
    subject: Subject,
    san_entries: Iterable[str] | None = None,
    key_passphrase: Optional[str] = None,
) -> str:
    """Generate a PEM CSR using openssl.

    We prefer OpenSSL's `-addext` to avoid version-sensitive config quirks.
    """
    cmd = ["openssl", "req", "-new", "-key", key_pem_path, "-subj", subject.to_openssl_subj()]

    if key_passphrase:
        cmd += ["-passin", f"pass:{key_passphrase}"]

    san_entries = list(san_entries or [])
    if san_entries:
        san_value = ",".join(san_entries)
        cmd += ["-addext", f"subjectAltName={san_value}"]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise RuntimeError(
            "OpenSSL CSR generation failed:\n" + err.decode(errors="ignore")
        )
    return out.decode("utf-8", errors="ignore")
