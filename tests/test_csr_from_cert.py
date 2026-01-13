"""Tests for creating CSR from an existing certificate's metadata."""
from nscert import keygen, csr


def test_create_csr_from_cert(tmp_path):
    # Generate a key
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Create a certificate from the key with SANs using a temp OpenSSL config
    conf = tmp_path / "conf.cnf"
    conf.write_text("""[ req ]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no
[ req_distinguished_name ]
[ v3_req ]
subjectAltName = DNS:www.example.com, IP:10.0.0.1
""")

    cert_file = tmp_path / "cert.pem"
    import subprocess
    subj = "/C=US/ST=CA/CN=example.com"
    subprocess.run(["openssl", "req", "-new", "-x509", "-key", str(key_file), "-out", str(cert_file), "-days", "1", "-config", str(conf), "-extensions", "v3_req", "-subj", subj], check=True)

    csr_pem = csr.create_csr_from_cert(str(cert_file), str(key_file))
    assert csr_pem.startswith("-----BEGIN CERTIFICATE REQUEST-----")
    # Ensure SANs and CN are preserved
    assert csr.csr_has_san(csr_pem, "DNS:www.example.com")
    assert csr.csr_has_san(csr_pem, "IP:10.0.0.1")

    # Check the CN shows up in the CSR subject
    import subprocess
    p = subprocess.run(["openssl", "req", "-in", "/dev/stdin", "-noout", "-subject"], input=csr_pem.encode("utf-8"), capture_output=True, check=True)
    out = p.stdout.decode("utf-8")
    import re
    assert re.search(r"CN\s*=\s*example\.com", out)
