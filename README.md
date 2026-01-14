# certctl

A set of small, composable Python scripts for certificate lifecycle automation across:

- **NetScaler Console** (test / DR / prod consoles)
- **NetScaler ADCs** (via Console as the central management plane)
- **External services** (e.g., Imperva WAF)

This repo is intentionally modular: each script does **one job well**, so you can
chain them in CI/CD, change-management workflows, or a future orchestrator.

## Current status

Implemented (working end-to-end in lab):
- **Create private key on NetScaler Console**, download it, and generate a **PEM CSR locally**.

Planned / scaffolding:
- Polling/reporting of certificate expiry across Console + external vendors
- CA submission adapters (ADCS, Sectigo, etc.)
- Upload key/cert to Console and deployment to ADCs (with automatic CA chain linking)
- External WAF deployment (Imperva)

## Directory layout

- `certctl/` - library code used by scripts
- `certctl/scripts/` - runnable scripts (single-purpose)

### Included scripts

- `certctl/scripts/nsconsole_certpoll.py` - poll a NetScaler Console for stored certificate expiry data and write a table / CSV / JSON report.
- `legacy/` - the original monolithic prototype script kept for reference

## Quick start (lab)

Create a key on Console, download it, and create a CSR:

```bash
python3 -m certctl keycsr-console \
  --console https://192.168.113.2 \
  --user nsroot \
  --app-name example.com \
  --out-dir ./out \
  --insecure
```

Notes:
- `--app-name` is the CN base; with `--rotate` (default ON) we timestamp the filenames and **never reuse keys**.
- The CSR is created locally with OpenSSL because `ns_ssl_csr` is not supported in some Console deployments.

## Security

- Secrets can be provided via env vars (recommended for CI):
  - `CERTCTL_CONSOLE_PASSWORD`
  - `CERTCTL_KEY_PASSPHRASE`
- On **macOS**, you can optionally store these in Keychain via prompts.
- Enterprise vault integration (AWS Secrets Manager / Azure Key Vault / etc.) will be added as a separate module.

