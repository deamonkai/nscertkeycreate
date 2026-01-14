from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

# Placeholder: later this will call a dedicated poller module for Console + Imperva.
# For now it emits an empty report scaffolding so repo CI/tests have something deterministic.


def run_poll_report(console: str, user: str, days: int, out_dir: str, insecure: bool = False) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')

    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "console": console,
        "user": user,
        "renewal_window_days": days,
        "items": [],
        "notes": [
            "Polling implementation TODO: query NetScaler Console for cert inventory + expiry.",
            "Also query external vendors (e.g., Imperva) as configured.",
        ],
    }

    (out / f"expiry-report_{ts}.json").write_text(json.dumps(payload, indent=2), encoding='utf-8')

    with (out / f"expiry-report_{ts}.csv").open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(["source", "cn", "serial", "not_after", "days_remaining", "targets"])
        # none yet
