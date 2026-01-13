"""CSR creation helpers using the OpenSSL CLI.

Provides utilities to create a CSR from a private key file or PEM content,
supporting Subject fields and SubjectAltName entries.
"""
from typing import List, Optional, Dict
import shutil
import subprocess
import tempfile
import os


class OpenSSLNotFound(Exception):
    pass


def _openssl_bin() -> str:
    path = shutil.which("openssl")
    if not path:
        raise OpenSSLNotFound("`openssl` not found in PATH")
    return path


def _build_subject_string(subject: Dict[str, str]) -> str:
    # Accepts keys like C, ST, L, O, OU, CN
    parts = []
    for k in ["C", "ST", "L", "O", "OU", "CN"]:
        v = subject.get(k)
        if v:
            parts.append(f"/{k}={v}")
    return "".join(parts)


def normalize_and_validate_san(s: str) -> str:
    """Normalize and validate a SAN entry.

    Accepts 'dns.example.com', 'IP', or prefixed 'DNS:...' / 'IP:...'.
    Returns 'DNS:...' or 'IP:...' normalized string. Raises ValueError on invalid input.
    """
    import ipaddress
    s = s.strip()
    if not s:
        raise ValueError("empty SAN")

    if s.upper().startswith("DNS:") or s.upper().startswith("IP:"):
        prefix, val = s.split(":", 1)
        val = val.strip()
    else:
        val = s
        prefix = None

    # Try IP first
    try:
        ipaddress.ip_address(val)
        return f"IP:{val}"
    except Exception:
        pass

    # Validate DNS name roughly (allow wildcard prefixes like '*.example.com')
    import re
    # simplified hostname regex (labels separated by dots)
    HOST_RE = re.compile(r"^(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)(?:\.(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?))*$")
    if val.startswith("*."):
        rest = val[2:]
        if HOST_RE.match(rest):
            return f"DNS:{val}"
    if HOST_RE.match(val):
        return f"DNS:{val}"

    raise ValueError(f"Invalid SAN value: {s}")


def create_csr_from_key(key_path: str, subject: Optional[Dict[str, str]] = None, sans: Optional[List[str]] = None, passphrase: Optional[str] = None) -> str:
    """Create a CSR using OpenSSL and return the CSR PEM text.

    - `key_path` must point to a private key file (PEM); if it is encrypted,
      supply `passphrase` which will be passed to OpenSSL via `-passin`.
    - `subject` may be provided either as a dict with fields like C, ST, L, O, OU, CN
      or as a subject string starting with a leading slash, e.g. '/C=US/ST=CA/CN=example.com'.
    - `sans` is a list of DNS names/IPs for SubjectAltName.
    """
    openssl = _openssl_bin()

    if isinstance(subject, dict):
        subj = _build_subject_string(subject)
    else:
        subj = subject

    # If sans look like ['DNS:...','IP:...'] normalize to plain names for config
    norm_sans = []
    if sans:
        for s in sans:
            # Normalize and validate; allow ValueError to bubble to caller
            ns = normalize_and_validate_san(s)
            norm_sans.append(ns)

    with tempfile.TemporaryDirectory() as td:
        conf_path = os.path.join(td, "csr.conf")
        csr_path = os.path.join(td, "req.csr")

        # Build minimal OpenSSL config with SANs if provided
        conf_lines = ["[ req ]", "distinguished_name = req_distinguished_name", "prompt = no"]
        if norm_sans:
            conf_lines.append("req_extensions = v3_req")
        conf_lines.append("")
        conf_lines.append("[ req_distinguished_name ]")
        # No need to fill DN here when using -subj, but keep the section present
        conf_lines.append("")
        if norm_sans:
            conf_lines.append("[ v3_req ]")
            conf_lines.append(f"subjectAltName = {', '.join(norm_sans)}")

        with open(conf_path, "w", encoding="utf-8") as f:
            f.write("\n".join(conf_lines))

        cmd = [openssl, "req", "-new", "-key", key_path, "-out", csr_path, "-config", conf_path]
        if subj:
            cmd += ["-subj", subj]
        if passphrase:
            cmd += ["-passin", f"pass:{passphrase}"]

        subprocess.run(cmd, check=True, capture_output=True)

        with open(csr_path, "r", encoding="utf-8") as f:
            return f.read()


def csr_has_san(csr_pem: str, san: str) -> bool:
    """Return True if the CSR PEM contains the provided SAN entry.

    This uses `openssl req -in - -noout -text` to parse the CSR contents.
    """
    openssl = _openssl_bin()
    p = subprocess.run([openssl, "req", "-in", "/dev/stdin", "-noout", "-text"], input=csr_pem.encode("utf-8"), check=True, capture_output=True)
    out = p.stdout.decode("utf-8")
    # Accept a few representations: 'DNS:...' or 'IP:...' -> just look for the name/value
    if san.startswith("DNS:"):
        return san[4:] in out
    if san.startswith("IP:"):
        return san[3:] in out
    return san in out



def extract_subject_and_sans_from_cert(cert_pem: str) -> (Dict[str, str], List[str]):
    """Extract subject fields and SANs from a certificate PEM using openssl.

    Returns (subject_dict, san_list)
    """
    openssl = _openssl_bin()

    # Get subject in RFC2253 style for easier parsing
    p = subprocess.run([openssl, "x509", "-in", "/dev/stdin", "-noout", "-subject", "-nameopt", "RFC2253"], input=cert_pem.encode("utf-8"), check=True, capture_output=True)
    subj_out = p.stdout.decode("utf-8").strip()
    # subj_out is like: "subject=CN=example.com,O=Example,C=US"
    subj = subj_out.split("=", 1)[1] if "=" in subj_out else ""
    subject_parts = {}
    for part in subj.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            subject_parts[k.strip()] = v.strip()

    # Get SANs from the text representation
    p2 = subprocess.run([openssl, "x509", "-in", "/dev/stdin", "-noout", "-text"], input=cert_pem.encode("utf-8"), check=True, capture_output=True)
    txt = p2.stdout.decode("utf-8")
    sans = []
    import re
    for m in re.finditer(r"DNS:([^,\s]+)", txt):
        sans.append(f"DNS:{m.group(1)}")
    # OpenSSL sometimes prints IPs as 'IP:' or 'IP Address: '
    for m in re.finditer(r"IP:?\s*Address:?\s*([^,\s]+)", txt, flags=re.IGNORECASE):
        sans.append(f"IP:{m.group(1)}")
    for m in re.finditer(r"IP:([^,\s]+)", txt):
        sans.append(f"IP:{m.group(1)}")

    return subject_parts, sans


def create_csr_from_cert(cert_path: str, key_path: str, passphrase: Optional[str] = None) -> str:
    """Create a CSR based on an existing certificate's subject and SANs, signing with `key_path`."""
    with open(cert_path, "r", encoding="utf-8") as f:
        cert_pem = f.read()

    subject, sans = extract_subject_and_sans_from_cert(cert_pem)
    # convert subject dict into subject string
    subj_str = _build_subject_string(subject) if subject else None
    return create_csr_from_key(key_path, subj_str, sans=sans, passphrase=passphrase)


def prompt_for_subject_and_sans() -> (Dict[str, str], List[str]):
    """Interactively prompt the user for subject fields and SANs.

    Returns a (subject_dict, san_list) tuple.
    """
    fields = ["C", "ST", "L", "O", "OU", "CN"]
    subject: Dict[str, str] = {}
    from .term import print_info
    print_info("Enter subject fields (press Enter to skip a field)")
    for f in fields:
        try:
            val = input(f"{f}: ").strip()
        except EOFError:
            val = ""
        if val:
            subject[f] = val

    print_info("Enter SANs (one per line). Examples: 'www.example.com' or '10.0.0.1'. Leave blank to finish.")
    sans: List[str] = []
    while True:
        try:
            s = input("SAN: ").strip()
        except EOFError:
            break
        if not s:
            break
        try:
            norm = normalize_and_validate_san(s)
        except ValueError as e:
            from .term import print_error
            print_error(f"Invalid SAN: {e}. Try again.")
            continue
        # If this is a wildcard SAN, ask for explicit confirmation
        if norm.startswith("DNS:*."):
            ans = input(
                f"Wildcard SAN detected: {norm}. Wildcard SANs (e.g., *.example.com) broaden certificate scope and can be risky. Type 'yes' to include it, or anything else to exclude: "
            ).strip().lower()
            if ans != "yes":
                from .term import print_info
                print_info(f"Excluded {norm}")
                continue
            else:
                from .term import print_info
                print_info(f"Included {norm}")
        # store the normalized SAN
        sans.append(norm)

    return subject, sans
