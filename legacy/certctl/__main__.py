"""certctl - orchestration entrypoint.

Today:
  certctl keycsr-console  ...  (create key on Console, download key, generate CSR)

This file exists so you can run `python -m certctl ...` and so `bin/certctl`
works without packaging.
"""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    p = argparse.ArgumentParser(prog="certctl", add_help=True)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("keycsr-console", help="Create key on Console, download it, then generate CSR locally")
    sub.add_parser("poll", help="(placeholder) Poll cert expiry across Console/ADCs/WAF")
    sub.add_parser("renew", help="(placeholder) Renew certs in renewal window")

    ns, rest = p.parse_known_args(argv)

    if ns.cmd == "keycsr-console":
        from certctl.scripts.keycsr_console import main as _m

        return _m(rest)

    if ns.cmd in {"poll", "renew"}:
        print(f"{ns.cmd}: not implemented yet (repo scaffold only)")
        return 2

    p.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
