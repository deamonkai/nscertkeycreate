Usage
=====

Installable package
-------------------

To install the package in editable (development) mode:

```bash
# from project root
python -m pip install -e .
```

Key generation (AES-encrypted)
------------------------------

Generate a new RSA 4096-bit key (AES-256 encrypted):

```bash
python -m certctl.scripts.keygen --cn example.com --kind rsa --out ./out
```

Generate an ECDSA key (secp384r1) and upload to Console:

```bash
python -m certctl.scripts.keygen --cn example.com --kind ecdsa --out ./out --upload-console --register-console --console https://console.example --user nsroot --insecure
```

If you want to match key/CSR timestamps, pass a shared `--stamp`:

```bash
python -m certctl.scripts.keygen --cn example.com --kind rsa --out ./out --stamp 20260101-120000
```

Combined key + CSR (shared stamp)
--------------------------------

Generate both a key and CSR with the same timestamp:

```bash
python -m certctl.scripts.keycsr --cn example.com --kind rsa --out ./out --san www.example.com --san 10.0.0.1
```

CSR creation from a rotated key
------------------------------

Create a CSR with SANs from an encrypted key (using the default subject fields):

```bash
python -m certctl.scripts.csr_create --key-file ./out/example.com_20260101-120000.key --cn example.com --san "DNS:www.example.com, IP:10.0.0.1" --out ./out
```

Override subject fields when needed:

```bash
python -m certctl.scripts.csr_create --key-file ./out/example.com_20260101-120000.key --cn example.com \
  --country US --state Alabama --organization "Regions Financial Corporation" --org-unit ECommerce \
  --locality Birmingham --email was@regions.com --out ./out
```

Use a matching timestamp:

```bash
python -m certctl.scripts.csr_create --key-file ./out/example.com_20260101-120000.key --cn example.com --out ./out --stamp 20260101-120000
```

CSR submission
--------------

Submit to Sectigo and wait for issuance:

```bash
python -m certctl.scripts.csr_submit --ca sectigo --csr ./out/example.com.csr --wait --out ./out/example.com.crt \
  --sectigo-org-id 1234 --sectigo-cert-type 5678 --sectigo-term 365 --sectigo-customer-uri cst123 \
  --sectigo-login your_login --sectigo-password your_password
```

Sectigo credentials can also be provided via env vars:
- `SECTIGO_BASE_URL` (default: https://cert-manager.com)
- `SECTIGO_LOGIN`
- `SECTIGO_PASSWORD`
- `SECTIGO_CUSTOMER_URI`
- `SECTIGO_ORG_ID`
- `SECTIGO_CERT_TYPE`
- `SECTIGO_TERM`

Submit to ADCS and collect the issued cert + chain:

```bash
python -m certctl.scripts.csr_submit --ca adcs --csr ./out/example.com.csr --wait --out ./out/example.com.crt \
  --adcs-base-url https://regionsissuing/certsrv --adcs-include-chain --adcs-chain-out ./out/example.com.chain.pem
```

Auto-select CA (ADCS for any CN/SAN containing `rgbk.com`, otherwise Sectigo):

```bash
python -m certctl.scripts.csr_submit --auto-ca --csr ./out/example.com.csr --wait --out ./out/example.com.crt \
  --adcs-base-url https://regionsissuing/certsrv
```

ADCS settings can be provided via JSON or env vars:
- JSON: `--adcs-config ./adcs.json` with `base_url`, `username`, `password`, optional `template`.
- Env: `ADCS_BASE_URL`, `ADCS_USERNAME`, `ADCS_PASSWORD`, optional `ADCS_TEMPLATE`.
Keychain usage (when `keyring` is installed):
- Use `--adcs-keychain-service` to set a custom keychain service name.
- Use `--adcs-save-keychain` to store prompted credentials.
- Use `--adcs-reset-keychain` to delete stored credentials.

NetScaler Console cert polling
------------------------------

Poll the Console for SSL certificate inventory (default output is a table):

```bash
python -m certctl.scripts.nsconsole_certpoll --console https://console.example --user nsroot --insecure
```

Binding details included in reports:
- `binding_count` = number of bound entities
- `binding_entities` = bound entity names (vservers/services/service-groups)
- `binding_types` = entity types (e.g., sslvserver, service)
- `binding_devices` = device display names or hostnames

Optional mapping details (via `--include-mappings`):
- `mapping_count` = number of cert_store_mapping entries for the cert
- `mapping_entities` = mapped entity names
- `mapping_entity_types` = mapped entity types
- `mapping_instances` = mapped instance display names/hostnames
- `mapping_instance_ips` = mapped instance IPs

Filter by expiry window:

```bash
python -m certctl.scripts.nsconsole_certpoll --console https://console.example --user nsroot --expires-within 30
```

Write JSON output to a file and include unbound/inactive certs:

```bash
python -m certctl.scripts.nsconsole_certpoll --console https://console.example --user nsroot --format json --out ./out/cert_inventory.json --all
```

Trigger a fresh inventory before fetching certs:

```bash
python -m certctl.scripts.nsconsole_certpoll --console https://console.example --user nsroot --inventory
```

Config file support
-------------------

You can store Console details and defaults in a JSON or YAML config and select
profiles by name. CLI flags override config values. YAML requires `PyYAML`.

Example `certctl.json`:

```json
{
  "defaults": {
    "format": "table",
    "timeout": 60,
    "inventory": false,
    "all": false
  },
  "consoles": {
    "test": {
      "url": "https://console-test.example",
      "user": "nsroot",
      "insecure": true
    },
    "prod": {
      "url": "https://console-prod.example",
      "user": "nsroot",
      "ca_bundle": "/path/to/ca.pem"
    }
  }
}
```

Run with a profile:

```bash
python -m certctl.scripts.nsconsole_certpoll --config ./certctl.json --profile test
```

Poll all consoles from config
-----------------------------

Write per-profile reports into `./reports`:

```bash
python -m certctl.scripts.nsconsole_certpoll_all --config ./certctl.json --format json --out-dir ./reports
```

Target a single profile from the same config:

```bash
python -m certctl.scripts.nsconsole_certpoll_all --config ./certctl.json --profile prod --format csv --out-dir ./reports
```

Write a merged report (JSON or CSV only):

```bash
python -m certctl.scripts.nsconsole_certpoll_all --config ./certctl.json --format json --out-dir ./reports --merge
```

Write a subject rollup (JSON or CSV only):

```bash
python -m certctl.scripts.nsconsole_certpoll_all --config ./certctl.json --format json --out-dir ./reports --rollup
```
