# nscertkeycreate.py

A NetScaler Console–centric tool to generate encrypted SSL private keys and CSRs,
with optional delivery to managed ADC Primary nodes.

Features:
- RSA 4096 or ECDSA (P-256 / P-384)
- Console-only or Console-delivered-to-ADC workflows
- macOS Keychain–backed credential storage
- Interactive by default, automation-friendly when needed

## Orchestrator (certctl)

Install (editable):

```bash
pip install -e .
```

Create key+CSR (delegates to legacy for now):

```bash
certctl new -- --console https://CONSOLE --user nsroot --app-name example.com --out-dir ./out --insecure
```

Poll expiries (placeholder scaffolding):

```bash
certctl poll --console https://CONSOLE --user nsroot --days 30 --out ./reports --insecure
```
