"""certctl: orchestration layer for certificate lifecycle tasks.

This repository is intentionally decomposed into small, purpose-built scripts.
`certctl` is the top-level CLI that coordinates those scripts.

Nothing in `certctl` should talk directly to a specific vendor/CA/device.
Those integrations live in dedicated modules (e.g., NetScaler Console NITRO).
"""

__all__ = ["cli"]
