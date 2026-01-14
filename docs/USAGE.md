Usage
=====

A thin wrapper script `bin/certctl` is included for development; it forwards
arguments to the `certctl` CLI. You can also run the CLI directly with the
project environment's Python:

Run keygen via the package CLI (using the project's venv python):

```bash
/Users/michaelmolloy/tools/nscertkeycreate/.venv/bin/python -m certctl.cli keygen --kind rsa --passphrase "fromcli" --keychain-service svc1 --save-passphrase
```

Or make the wrapper executable and use it directly:

```bash
chmod +x bin/certctl
./bin/certctl keygen --kind rsa --passphrase "fromcli" --keychain-service svc1 --save-passphrase
```

Installable package
-------------------

To install the package editable (development) mode so `certctl` is available on your PATH:

```bash
# from project root
python -m pip install -e .
# now `certctl` should be on your PATH (provided your venv is active)
certctl keygen --kind rsa --keychain-service svc1 --save-passphrase
```

CSR commands
------------

Create a CSR from a private key:

```bash
certctl csr create --key-file /path/to/key.pem --subject "/C=US/ST=CA/CN=example.com" --san www.example.com --san 10.0.0.1 --out /tmp/example.csr
```

Create a CSR interactively (prompts for subject fields and SANs if none supplied):

```bash
certctl csr create --key-file /path/to/key.pem --out /tmp/example.csr
# prompts for C, ST, L, O, OU, CN and then SANs (one per line)
```

Note about wildcard SANs: Wildcard SANs (for example, `*.example.com`) broaden the scope of a certificate and can be risky. When a wildcard SAN is entered interactively `certctl` will prompt you to explicitly confirm by typing `yes`. If you pass wildcard SANs on the CLI, `certctl` will prompt for confirmation in interactive terminals; in non-interactive runs (CI or scripts) you must pass `--allow-wildcard` to proceed. The `--allow-wildcard` flag exists on both `csr create` and `csr submit` — use it with care.

SAN validation
--------------

SAN entries are validated and normalized. Acceptable inputs:
- Hostnames (e.g., `www.example.com`) — normalized to `DNS:...`
- IPv4/IPv6 addresses (e.g., `10.0.0.1`) — normalized to `IP:...`
- You may also provide `DNS:...` or `IP:...` explicitly

Invalid SANs will be rejected interactively (you'll be prompted again) or will cause the CLI to exit with an error when provided as `--san` arguments.

Show CSR details (parsed by openssl):

```bash
certctl csr show --csr-file /tmp/example.csr
```

Notes:
- Prefer reading/writing passphrases using `--keychain-service` and `--save-passphrase` instead of placing passphrases directly on the command line in production.
- The wrapper is intentionally minimal for development; packaging adds the `certctl` entry point for convenience.
