"""CLI tests for creating CSR from an existing certificate."""
from nscert import cli, keygen


def test_cli_csr_create_from_cert(tmp_path):
    # Generate key
    key_pem = keygen.generate_private_key(kind="rsa", bits=1024)
    key_file = tmp_path / "k.pem"
    key_file.write_text(key_pem)

    # Create a cert with SANs
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
    subj = "/C=US/ST=CA/CN=example.com"
    import subprocess
    subprocess.run(["openssl", "req", "-new", "-x509", "-key", str(key_file), "-out", str(cert_file), "-days", "1", "-config", str(conf), "-extensions", "v3_req", "-subj", subj], check=True)

    out = tmp_path / "req.csr"
    rc = cli.main(["csr", "create", "--key-file", str(key_file), "--from-cert", str(cert_file), "--out", str(out)])
    assert rc == 0
    assert out.exists()

    # Show the CSR to ensure content
    rc2 = cli.main(["csr", "show", "--csr-file", str(out)])
    assert rc2 == 0
