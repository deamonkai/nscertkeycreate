"""Tests for certctl.utils.extract_pem_from_json"""

from certctl.utils import extract_pem_from_json
from certctl.netscaler import extract_csr_text


def test_extract_from_ns_ssl_csr():
    resp = {
        "ns_ssl_csr": [
            {
                "file_name": "app1.csr",
                "csr": "-----BEGIN CERTIFICATE REQUEST-----\nMIIC123...\n-----END CERTIFICATE REQUEST-----",
                "errorcode": 0,
            }
        ],
        "errorcode": 0,
    }

    pem = extract_pem_from_json(resp)
    assert pem is not None
    assert pem.startswith("-----BEGIN CERTIFICATE REQUEST-----")

    # netscaler-specific helper should prefer the ns_ssl_csr field
    pem2 = extract_csr_text(resp)
    assert pem2 == pem


def test_extract_from_ns_command_stdout():
    resp = {
        "ns_command": {
            "commands": [
                {
                    "command": "shell cat /nsconfig/ssl/app1.csr",
                    "stdout": "-----BEGIN CERTIFICATE REQUEST-----\nMIIC_STDOUT...\n-----END CERTIFICATE REQUEST-----",
                    "response": None,
                }
            ],
            "errorcode": 0,
        }
    }

    pem = extract_pem_from_json(resp)
    assert pem is not None
    assert "MIIC_STDOUT" in pem


def test_extract_from_rows_array():
    resp = {
        "ns_command": {
            "commands": [
                {"command": "cat ...", "rows": ["-----BEGIN CERTIFICATE REQUEST-----", "MIIC_ROWS...", "-----END CERTIFICATE REQUEST-----"]}
            ]
        }
    }

    pem = extract_pem_from_json(resp)
    assert pem is not None
    assert "MIIC_ROWS" in pem


def test_no_pem_returns_none():
    resp = {"foo": "bar", "nested": {"x": [1, 2, {"y": "nothing here"}]}}
    assert extract_pem_from_json(resp) is None
