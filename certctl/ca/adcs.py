"""ADCS adapter."""

from __future__ import annotations

import base64
import re
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from typing import Optional

import requests

from .base import CAAdapter, CertStatus, SubmitResult


@dataclass
class AdcsConfig:
    base_url: str
    username: str
    password: str
    template: Optional[str] = None
    verify: object = True


_REQ_ID_RE = re.compile(r"ReqID=([0-9]+)")
_REQ_ID_TEXT_RE = re.compile(r"Request\\s+Id\\s+is\\s+([0-9]+)", re.IGNORECASE)
_DISPOSITION_RE = re.compile(r"Disposition\\s*=\\s*([0-9]+)")


def _parse_req_id(body: str) -> str:
    match = _REQ_ID_RE.search(body) or _REQ_ID_TEXT_RE.search(body)
    if not match:
        raise RuntimeError("Unable to parse ADCS request id from response.")
    return match.group(1)


def _parse_disposition(body: str) -> Optional[str]:
    match = _DISPOSITION_RE.search(body)
    if not match:
        return None
    return match.group(1)


def _b64_to_pem(b64_data: str) -> str:
    cleaned = "".join(b64_data.strip().split())
    lines = textwrap.fill(cleaned, 64)
    return "-----BEGIN CERTIFICATE-----\n" + lines + "\n-----END CERTIFICATE-----\n"


def _require_openssl() -> str:
    path = shutil.which("openssl")
    if not path:
        raise RuntimeError("OpenSSL not found in PATH.")
    return path


def _p7b_to_pem(b64_data: str) -> str:
    _require_openssl()
    der = base64.b64decode("".join(b64_data.strip().split()))
    proc = subprocess.run(
        ["openssl", "pkcs7", "-inform", "DER", "-print_certs"],
        input=der,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return proc.stdout.decode("utf-8", errors="replace")


class AdcsAdapter(CAAdapter):
    name = "adcs"

    def __init__(self, config: AdcsConfig):
        self.config = config
        self.session = requests.Session()
        self.session.auth = (self.config.username, self.config.password)

    def submit_csr(self, csr_pem: str, **kwargs) -> SubmitResult:
        attrib = ""
        if self.config.template:
            attrib = f"CertificateTemplate:{self.config.template}"
        data = {
            "Mode": "newreq",
            "CertRequest": csr_pem,
            "CertAttrib": attrib,
            "TargetStoreFlags": "0",
            "SaveCert": "yes",
        }
        resp = self.session.post(
            f"{self.config.base_url.rstrip('/')}/certfnsh.asp",
            data=data,
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        req_id = _parse_req_id(resp.text)
        disposition = _parse_disposition(resp.text)
        if disposition == "5":
            raise RuntimeError("ADCS request was denied.")
        return SubmitResult(request_id=req_id, ca=self.name)

    def poll_status(self, request_id: str) -> CertStatus:
        resp = self.session.get(
            f"{self.config.base_url.rstrip('/')}/certnew.cer",
            params={"ReqID": request_id, "Enc": "b64"},
            verify=self.config.verify,
            timeout=60,
        )
        if resp.status_code == 200 and "<html" not in resp.text.lower():
            return CertStatus(status="Issued", raw={"request_id": request_id})
        body = resp.text.lower()
        if "pending" in body or "certsrv_e_pending" in body:
            return CertStatus(status="Pending", raw={"request_id": request_id})
        if "denied" in body or "rejected" in body:
            return CertStatus(status="Denied", raw={"request_id": request_id})
        return CertStatus(status="Unknown", raw={"request_id": request_id, "body": resp.text[:2000]})

    def collect_certificate(self, request_id: str, *, format_name=None) -> str:
        resp = self.session.get(
            f"{self.config.base_url.rstrip('/')}/certnew.cer",
            params={"ReqID": request_id, "Enc": "b64"},
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        body = resp.text.strip()
        if "BEGIN CERTIFICATE" in body:
            return body if body.endswith("\n") else body + "\n"
        if "<html" in body.lower():
            raise RuntimeError("ADCS did not return a certificate.")
        return _b64_to_pem(body)

    def collect_chain(self, request_id: str) -> str:
        resp = self.session.get(
            f"{self.config.base_url.rstrip('/')}/certnew.p7b",
            params={"ReqID": request_id, "Enc": "b64"},
            verify=self.config.verify,
            timeout=60,
        )
        resp.raise_for_status()
        body = resp.text.strip()
        if "BEGIN PKCS7" in body:
            # Convert PEM PKCS7 to PEM certificates.
            _require_openssl()
            proc = subprocess.run(
                ["openssl", "pkcs7", "-inform", "PEM", "-print_certs"],
                input=body.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return proc.stdout.decode("utf-8", errors="replace")
        if "<html" in body.lower():
            raise RuntimeError("ADCS did not return a certificate chain.")
        return _p7b_to_pem(body)
