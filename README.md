# nscertkeycreate.py

A NetScaler Console–centric tool to generate encrypted SSL private keys and CSRs,
with optional delivery to managed ADC Primary nodes.

Features:
- RSA 4096 or ECDSA (P-256 / P-384)
- Console-only or Console-delivered-to-ADC workflows
- macOS Keychain–backed credential storage
- Interactive by default, automation-friendly when needed