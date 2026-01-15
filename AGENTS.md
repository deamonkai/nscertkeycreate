# AGENTS.md

## Setup
- Python: `>=3.9`
- Create venv + install: `python -m venv .venv && . .venv/bin/activate && python -m pip install -e .`
- Optional test deps: `python -m pip install --upgrade pytest`
- Required env vars (recommended for CI): `CERTCTL_CONSOLE_PASSWORD`, `CERTCTL_KEY_PASSPHRASE`
- Start services: none

## How to run checks
- Lint: not configured
- Tests: `python -m pytest -q`
- Build/package: `python -m pip install -e .`

## Project conventions
- Language/tooling: Python package (`certctl`) + thin CLI wrappers in `bin/`
- Formatting/linting: not configured; keep changes small and readable
- Key directories:
  - `certctl/` = library code used by scripts/CLI
  - `certctl/scripts/` = single-purpose runnable scripts
  - `nscert/` = legacy/alternate package copy
  - `legacy/` = original monolithic prototype (reference only)
  - `docs/` = development + usage notes
  - `bin/` = dev wrapper scripts
  - `reports/`, `out/` = generated outputs (avoid hand edits)

## Guardrails
- Keep certs/keys/CSRs in PEM format.
- Prefer Keychain/secret store helpers; do not hardcode secrets or commit sample keys.
- Keep scripts single-purpose and composable; avoid expanding one script into a multi-role tool.
- Don’t change CLI/public APIs without updating `docs/USAGE.md` and tests.
- If unsure, add a short note explaining assumptions.
