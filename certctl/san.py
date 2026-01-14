"""SAN parsing/normalization.

Accepts inputs like:
- "DNS:example.com,DNS:www.example.com"
- "example.com, www.example.com"  (bare hostnames treated as DNS)
- "IP:10.0.0.1, 10.0.0.2"        (bare IPs treated as IP)

Returns a list suitable for OpenSSL: ["DNS:...", "IP:...", ...].
"""

from __future__ import annotations

import ipaddress
from typing import List


def normalize_san_list(san_raw: str) -> List[str]:
    if not san_raw:
        return []

    items = [x.strip() for x in san_raw.split(",") if x.strip()]
    out: List[str] = []

    for item in items:
        if ":" in item:
            k, v = item.split(":", 1)
            k = k.strip().upper()
            v = v.strip()
            if not v:
                continue
            if k in {"DNS", "IP", "URI", "EMAIL", "RID"}:
                out.append(f"{k}:{v}")
                continue
            # Unknown prefix: treat whole thing as DNS if it isn't an IP
            item = v

        # Bare value: detect IP vs DNS
        try:
            ipaddress.ip_address(item)
            out.append(f"IP:{item}")
        except ValueError:
            out.append(f"DNS:{item}")

    # de-dupe but preserve order
    seen = set()
    deduped: List[str] = []
    for x in out:
        k = x.upper()
        if k not in seen:
            seen.add(k)
            deduped.append(x)
    return deduped
