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

Submit to the self-signed workflow CA (local testing):

```bash
python -m certctl.scripts.csr_submit --ca selfsigned --csr ./out/example.com.csr --wait --out ./out/example.com.crt \
  --selfsign-ca-dir ./out/selfsigned --selfsign-include-chain --selfsign-chain-out ./out/example.com.chain.pem
```

Self-signed passphrase can be provided via `CERTCTL_SELFSIGN_PASSPHRASE` (or `CERTCTL_KEY_PASSPHRASE`).

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

Imperva deploy
--------------

Deploy a cert stored in NetScaler Console to Imperva (combined PEM built automatically):

```bash
python -m certctl.scripts.imperva_deploy --certkeypair example.com --site-id 123456 \
  --console https://console.example --user nsroot --insecure
```

Imperva API credentials:
- Env: `IMPERVA_API_ID`, `IMPERVA_API_KEY` (otherwise you will be prompted).

Notes:
- Uses `PUT /api/prov/v2/sites/{siteId}/customCertificate` with base64-encoded PEM and key.
- The combined PEM is only created for Imperva; Console/ADC keep certs and CA files separate.

Self-signed Console + ADC deploy
--------------------------------

Generate a self-signed cert, upload it to Console, and deploy to ADCs:

```bash
python -m certctl.scripts.selfsigned_console_deploy --cn www.molloytest.net --kind rsa --out ./out \
  --console https://192.168.113.2 --user nsroot --insecure --list-adc-menu
```

Console cert_store probe (minimal payloads)
-------------------------------------------

Probe minimal cert_store payloads for server + CA certs:

```bash
python -m certctl.scripts.console_cert_store_probe \
  --console https://192.168.113.2 --user nsroot --insecure \
  --ca-name Molloy_Root_CA_RSA --ca-cert ./out/www.molloytest.net-20260121-165010.ca.pem \
  --name www_molloytest_net --cert ./out/www.molloytest.net-20260121-165010.crt \
  --key ./out/www.molloytest.net-20260121-165010.key --domain www.molloytest.net
```

Use `--dry-run` to print payload sizes without sending requests.

Optional flags for alternate payloads:
- `--include-key-file` adds `key_file` to the server payload.
- `--cert-type server_cert` and `--ca-cert-type root_cert` add cert_type values.
- `--cert-file-name` / `--ca-cert-file-name` override file_name fields.
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

Filter by substring (name, subject, issuer, device, or IP):

```bash
python -m certctl.scripts.nsconsole_certpoll --console https://console.example --user nsroot --filter test.molloyhome.net
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

Deploy cert to ADCs via Console
-------------------------------

Deploy a certkey to the ADCs it is already bound to (from Console bindings):

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101
```

If the cert is on the ADC but not yet visible in Console, trigger an inventory refresh:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101 --sync
```

If the cert is only on the ADC, import it via the Console proxy using a selected ADC:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101 \
  --list-adc menu --import-missing
```

When the Console does not support `list_entity_cert`, the import step will try the ADC certkey name using the CN and a normalized underscore variant.

If the cert is only on the ADC, you can also poll the selected ADCs before lookup:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101 --list-adc menu --poll-adc --poll-wait 5
```

List managed ADCs to JSON for later use:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --list-adc json --list-adc-out ./out/managed_devices.json
```

Include non-primary HA nodes in the listing:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --list-adc json --all-adc --list-adc-out ./out/managed_devices.json
```

Interactive ADC selection:

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --list-adc menu --certkeypair example.com_20260101
```

Deploy using bindings from another certkeypair (for rotation):

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101 \
  --source-certkeypair example.com_20240101
```

Link CA certs (upload if missing, then link):

```bash
python -m certctl.scripts.nsconsole_deploy --config ./certctl.json --profile prod --certkeypair example.com_20260101 \
  --ca-certkey myroot_ca --ca-cert-file ./out/root.pem --ca-certkey myintermediate_ca --ca-cert-file ./out/intermediate.pem
```

If no `--ca-certkey` values are provided, the script will attempt to link any CA certs found in the source cert's chain metadata.
