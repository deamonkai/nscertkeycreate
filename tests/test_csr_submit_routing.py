from certctl.scripts import csr_submit


def test_parse_csr_for_auto_ca(monkeypatch, tmp_path):
    csr_path = tmp_path / "req.csr"
    csr_path.write_text("dummy", encoding="utf-8")

    def fake_run(cmd, stdout, stderr, check, text):
        class Result:
            def __init__(self):
                self.stdout = (
                    "Subject: C=US, ST=AL, CN=api.rgbk.com\n"
                    "X509v3 Subject Alternative Name:\n"
                    "    DNS:api.rgbk.com, DNS:example.com\n"
                )

        return Result()

    monkeypatch.setattr(csr_submit.subprocess, "run", fake_run)
    cn, san = csr_submit._parse_csr_subject_and_sans(str(csr_path))
    assert cn == "api.rgbk.com"
    assert "DNS:api.rgbk.com" in san


def test_choose_ca_prefers_adcs_for_rgbk():
    assert csr_submit._choose_ca("svc.rgbk.com", None) == "adcs"
    assert csr_submit._choose_ca("example.com", "DNS:api.rgbk.com") == "adcs"
    assert csr_submit._choose_ca("example.com", "DNS:api.example.com") == "sectigo"
