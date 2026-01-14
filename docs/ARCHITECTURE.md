# Certificate automation architecture

This repository is organized around **small scripts** and a thin **orchestrator**.

## Key principles

- Never reuse private keys (rotate always)
- All artifacts are **PEM**
- Credentials are never stored in the repo
- Prefer centralized management via NetScaler Console
- Build for three environments: Test / DR / Prod

## Planned workflow

1. Poll inventory + expiry (Console + external vendors)
2. For items within renewal window (default 30d), generate new key + CSR
3. Submit CSR to selected CA (ADCS, Sectigo, ...)
4. Download certificate chain in PEM
5. Upload key+cert to Console (source of truth)
6. Deploy to ADCs via Console
7. Deploy to Imperva (optional)
8. Report + audit log

## Current state

- `legacy/nscertkeycreate.py` provides the working key+CSR flow for NetScaler Console.
- `certctl` wraps legacy behavior today; gradually replace with dedicated modules.
