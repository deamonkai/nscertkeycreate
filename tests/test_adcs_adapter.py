import base64

import pytest
import responses

from certctl.ca.adcs import AdcsAdapter, AdcsConfig, _b64_to_pem, _parse_req_id


def test_parse_req_id_from_html():
    body = "some html certnew.cer?ReqID=123&amp;something"
    assert _parse_req_id(body) == "123"


def test_b64_to_pem_wraps():
    raw = base64.b64encode(b"dummy").decode("ascii")
    pem = _b64_to_pem(raw)
    assert "BEGIN CERTIFICATE" in pem
    assert "END CERTIFICATE" in pem


@responses.activate
def test_adcs_submit_and_collect():
    config = AdcsConfig(
        base_url="https://adcs.example/certsrv",
        username="user",
        password="pass",
        verify=False,
    )
    adapter = AdcsAdapter(config)

    responses.add(
        responses.POST,
        "https://adcs.example/certsrv/certfnsh.asp",
        body="certnew.cer?ReqID=456&amp;Enc=b64",
        status=200,
    )
    cert_b64 = base64.b64encode(b"fakecert").decode("ascii")
    responses.add(
        responses.GET,
        "https://adcs.example/certsrv/certnew.cer",
        body=cert_b64,
        status=200,
    )

    submit = adapter.submit_csr("CSRDATA")
    assert submit.request_id == "456"

    cert = adapter.collect_certificate("456")
    assert "BEGIN CERTIFICATE" in cert
