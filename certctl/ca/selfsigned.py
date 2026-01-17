"""Self-signed CA adapter for workflow testing."""

from __future__ import annotations

import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

from .base import CAAdapter, CertStatus, SubmitResult

DEFAULT_RSA_BITS = 4096
DEFAULT_EC_CURVE = "secp384r1"


@dataclass
class SelfSignedConfig:
    ca_dir: str = "./out/selfsigned"
    passphrase: str = ""
    ca_days: int = 60
    leaf_days: int = 59
    rsa_cn: str = "Molloy Root CA (RSA)"
    ecdsa_cn: str = "Molloy Root CA (ECDSA)"


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise RuntimeError("OpenSSL not found in PATH.")
    return path


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def _write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def _detect_key_type(csr_path: Path) -> str:
    _require_openssl()
    proc = subprocess.run(
        ["openssl", "req", "-in", str(csr_path), "-noout", "-text"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True,
    )
    for line in proc.stdout.splitlines():
        if "Public Key Algorithm" in line:
            lowered = line.lower()
            if "ec" in lowered:
                return "ecdsa"
            if "rsa" in lowered:
                return "rsa"
    return "rsa"


def _extract_sans(csr_path: Path) -> list[str]:
    _require_openssl()
    proc = subprocess.run(
        ["openssl", "req", "-in", str(csr_path), "-noout", "-text"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True,
    )
    sans = []
    saw_san = False
    for line in proc.stdout.splitlines():
        line = line.strip()
        if "Subject Alternative Name" in line:
            saw_san = True
            continue
        if saw_san:
            if line.startswith("DNS:") or line.startswith("IP Address:"):
                entries = [e.strip() for e in line.split(",")]
                for entry in entries:
                    if entry.startswith("DNS:"):
                        sans.append(f"DNS:{entry[4:]}")
                    elif entry.startswith("IP Address:"):
                        sans.append(f"IP:{entry.split(':', 1)[1]}")
            else:
                saw_san = False
    return sans


def _ca_paths(ca_dir: Path, kind: str) -> Tuple[Path, Path, Path]:
    key_path = ca_dir / f"molloy_root_ca_{kind}.key"
    cert_path = ca_dir / f"molloy_root_ca_{kind}.pem"
    serial_path = ca_dir / f"molloy_root_ca_{kind}.srl"
    return key_path, cert_path, serial_path


def _ensure_ca(config: SelfSignedConfig, kind: str) -> Tuple[Path, Path, Path]:
    ca_dir = Path(config.ca_dir)
    key_path, cert_path, serial_path = _ca_paths(ca_dir, kind)
    if key_path.exists() and cert_path.exists():
        _require_openssl()
        check_cmd = [
            "openssl",
            "pkey",
            "-in",
            str(key_path),
            "-passin",
            f"pass:{config.passphrase}",
            "-noout",
        ]
        try:
            _run(check_cmd)
            return key_path, cert_path, serial_path
        except subprocess.CalledProcessError:
            key_path.rename(key_path.with_suffix(key_path.suffix + ".badpass"))
            cert_path.rename(cert_path.with_suffix(cert_path.suffix + ".badpass"))

    _require_openssl()
    ca_dir.mkdir(parents=True, exist_ok=True)
    if kind == "rsa":
        key_cmd = [
            "openssl",
            "genpkey",
            "-algorithm",
            "RSA",
            "-pkeyopt",
            f"rsa_keygen_bits:{DEFAULT_RSA_BITS}",
            "-aes-256-cbc",
            "-pass",
            f"pass:{config.passphrase}",
            "-out",
            str(key_path),
        ]
        subject_cn = config.rsa_cn
    else:
        key_cmd = [
            "openssl",
            "genpkey",
            "-algorithm",
            "EC",
            "-pkeyopt",
            f"ec_paramgen_curve:{DEFAULT_EC_CURVE}",
            "-pkeyopt",
            "ec_param_enc:named_curve",
            "-aes-256-cbc",
            "-pass",
            f"pass:{config.passphrase}",
            "-out",
            str(key_path),
        ]
        subject_cn = config.ecdsa_cn
    _run(key_cmd)

    ca_cmd = [
        "openssl",
        "req",
        "-x509",
        "-new",
        "-key",
        str(key_path),
        "-passin",
        f"pass:{config.passphrase}",
        "-subj",
        f"/CN={subject_cn}",
        "-days",
        str(config.ca_days),
        "-sha256",
        "-addext",
        "basicConstraints=critical,CA:TRUE,pathlen:1",
        "-addext",
        "keyUsage=critical,keyCertSign,cRLSign",
        "-out",
        str(cert_path),
    ]
    _run(ca_cmd)
    return key_path, cert_path, serial_path


def _leaf_extfile(ca_dir: Path, sans: list[str]) -> Path:
    ext_path = ca_dir / "leaf_ext.cnf"
    content = "\n".join(
        [
            "basicConstraints=CA:FALSE",
            "keyUsage=digitalSignature,keyEncipherment",
            "extendedKeyUsage=serverAuth,clientAuth",
        ]
    )
    if sans:
        content += "\n" + "subjectAltName=" + ", ".join(sans)
    _write_text(ext_path, content + "\n")
    return ext_path


class SelfSignedAdapter(CAAdapter):
    name = "selfsigned"

    def __init__(self, config: SelfSignedConfig):
        self.config = config
        self._issued: Dict[str, str] = {}
        self._request_kind: Dict[str, str] = {}
        self._ca_paths: Dict[str, Tuple[Path, Path, Path]] = {}

    def submit_csr(self, csr_pem: str, **kwargs) -> SubmitResult:
        ca_dir = Path(self.config.ca_dir)
        ca_dir.mkdir(parents=True, exist_ok=True)
        stamp = str(time.time_ns())
        csr_path = ca_dir / f"csr_{stamp}.pem"
        _write_text(csr_path, csr_pem)

        kind = _detect_key_type(csr_path)
        key_path, cert_path, serial_path = _ensure_ca(self.config, kind)
        self._ca_paths[kind] = (key_path, cert_path, serial_path)

        leaf_path = ca_dir / f"leaf_{stamp}.pem"
        sans = _extract_sans(csr_path)
        ext_path = _leaf_extfile(ca_dir, sans)
        leaf_cmd = [
            "openssl",
            "x509",
            "-req",
            "-in",
            str(csr_path),
            "-CA",
            str(cert_path),
            "-CAkey",
            str(key_path),
            "-passin",
            f"pass:{self.config.passphrase}",
            "-CAcreateserial",
            "-CAserial",
            str(serial_path),
            "-days",
            str(self.config.leaf_days),
            "-sha256",
            "-extfile",
            str(ext_path),
            "-out",
            str(leaf_path),
        ]
        _run(leaf_cmd)
        leaf_pem = leaf_path.read_text(encoding="utf-8")
        request_id = f"selfsigned-{stamp}"
        self._issued[request_id] = leaf_pem if leaf_pem.endswith("\n") else leaf_pem + "\n"
        self._request_kind[request_id] = kind
        return SubmitResult(request_id=request_id, ca=self.name)

    def poll_status(self, request_id: str) -> CertStatus:
        return CertStatus(status="Issued", raw={"request_id": request_id})

    def collect_certificate(self, request_id: str, *, format_name: Optional[str] = None) -> str:
        if request_id not in self._issued:
            raise RuntimeError(f"Unknown request id: {request_id}")
        return self._issued[request_id]

    def collect_chain(self, request_id: str) -> str:
        if request_id not in self._issued:
            raise RuntimeError(f"Unknown request id: {request_id}")
        cert = self._issued[request_id]
        kind = self._request_kind.get(request_id, "rsa")
        _, ca_cert_path, _ = self._ca_paths[kind]
        ca_pem = ca_cert_path.read_text(encoding="utf-8")
        return cert + (ca_pem if ca_pem.endswith("\n") else ca_pem + "\n")
