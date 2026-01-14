"""Bridge to legacy prototype script.

We keep the legacy workflow runnable while we migrate functionality into
small, purpose-built modules.

This module shells out to `legacy/nscertkeycreate.py` within the repo.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def run_legacy_nscertkeycreate(*, console: str, user: str, app_name: str, out_dir: str, insecure: bool, ca_bundle: str | None) -> int:
    repo_root = Path(__file__).resolve().parents[2]
    legacy = repo_root / "legacy" / "nscertkeycreate.py"

    cmd = [sys.executable, str(legacy), "--console", console, "--user", user, "--app-name", app_name, "--out-dir", out_dir]
    if insecure:
        cmd.append("--insecure")
    if ca_bundle:
        cmd += ["--ca-bundle", ca_bundle]

    # inherit environment; users may set keyring backend vars, proxy vars, etc.
    env = os.environ.copy()
    return subprocess.call(cmd, env=env)
