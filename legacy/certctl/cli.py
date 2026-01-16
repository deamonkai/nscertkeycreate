"""Minimal CLI for certctl tooling.

Provides a `keygen` subcommand which wraps `certctl.keygen.generate_private_key`.
This is intentionally small and testable: `main(argv)` accepts an argv list.
"""
from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from . import keygen


def _build_subj_from_dict(subject: dict) -> str:
    parts = []
    for k in ["C", "ST", "L", "O", "OU", "CN"]:
        v = subject.get(k)
        if v:
            parts.append(f"/{k}={v}")
    return "".join(parts)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="certctl", description="certctl control utility")
    sub = p.add_subparsers(dest="command")

    keygen_p = sub.add_parser("keygen", help="Generate a private key")
    keygen_p.add_argument("--kind", choices=["rsa", "ec"], default="rsa")
    keygen_p.add_argument("--bits", type=int, default=4096, help="RSA key bits")
    keygen_p.add_argument("--curve", default="prime256v1", help="EC curve")
    keygen_p.add_argument("--passphrase", help="Passphrase to encrypt key (insecure on CLI)")
    keygen_p.add_argument("--keychain-service", help="Keychain service name to read/write passphrase")
    keygen_p.add_argument("--save-passphrase", action="store_true", help="Save provided passphrase into Keychain")
    keygen_p.add_argument("--keychain-account", default="certctl", help="Keychain account name when saving passphrase")
    keygen_p.add_argument("--out", help="Write key to file instead of stdout")

    # csr subcommands
    csr_p = sub.add_parser("csr", help="Create and inspect CSRs")
    csr_sub = csr_p.add_subparsers(dest="csr_cmd")

    csr_create = csr_sub.add_parser("create", help="Create a CSR from a private key file")
    csr_create.add_argument("--key-file", required=True, help="Path to the private key PEM")
    csr_create.add_argument("--subject", help="Subject string in /C=.../ST=.../CN=... format or as key=value pairs like C=US,ST=CA,CN=example.com")
    csr_create.add_argument("--san", action="append", help="SubjectAltName entry (DNS or IP); can be given multiple times")
    csr_create.add_argument("--allow-wildcard", action="store_true", help="Allow wildcard SANs without interactive confirmation. Use with caution: wildcards broaden certificate scope; in non-interactive contexts this flag bypasses interactive confirmation.")
    csr_create.add_argument("--from-cert", help="Path to an existing certificate to populate subject and SANs from")
    csr_create.add_argument("--passphrase", help="Passphrase for encrypted key (insecure on CLI)")
    csr_create.add_argument("--out", help="Write CSR to file instead of stdout")

    csr_show = csr_sub.add_parser("show", help="Show CSR details (like SANs)")
    csr_show.add_argument("--csr-file", required=True, help="Path to CSR PEM file")

    csr_submit = csr_sub.add_parser("submit", help="Submit a CSR to a CA adapter")
    csr_submit.add_argument("--csr-file", required=True, help="CSR PEM file to submit")
    csr_submit.add_argument("--ca", choices=["mock", "sectigo"], default="mock", help="CA adapter to use")
    csr_submit.add_argument("--name", required=True, help="Name for the cert request")
    csr_submit.add_argument("--wait", action="store_true", help="Wait for issuance and download cert")
    csr_submit.add_argument("--out", help="Write downloaded cert to file")
    csr_submit.add_argument("--allow-wildcard", action="store_true", help="Allow submission of CSRs containing wildcard SANs. Use with caution: wildcards broaden certificate scope and may be unsafe.")

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "keygen":
        if args.kind == "rsa":
            pem = keygen.generate_rsa_key(bits=args.bits, passphrase=args.passphrase, keychain_service=args.keychain_service, save_to_keychain=args.save_passphrase, keychain_account=args.keychain_account)
        else:
            pem = keygen.generate_ec_key(curve=args.curve, passphrase=args.passphrase, keychain_service=args.keychain_service, save_to_keychain=args.save_passphrase, keychain_account=args.keychain_account)

        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(pem)
        else:
            sys.stdout.write(pem)
        return 0

    if args.command == "csr":
        if args.csr_cmd == "create":
            # Parse subject: accept both /C=... style or comma separated key=value
            subject = {}
            subj = args.subject or ""
            if subj.startswith("/"):
                # convert /C=US/ST=... into dict
                for part in subj.split("/"):
                    if not part:
                        continue
                    if "=" in part:
                        k, v = part.split("=", 1)
                        subject[k] = v
            elif subj:
                for part in subj.split(","):
                    if "=" in part:
                        k, v = part.split("=", 1)
                        subject[k.strip()] = v.strip()

            csr_pem = None
            from . import csr as csrmod
            if args.from_cert:
                # Populate subject and SANs from an existing cert
                csr_pem = csrmod.create_csr_from_cert(args.from_cert, args.key_file, passphrase=args.passphrase)
            else:
                subj_str = subj if subj and subj.startswith("/") else _build_subj_from_dict(subject) if subject else None

                # If no subject and no SANs provided, prompt interactively
                if not subj_str and not args.san:
                    subj_dict, san_list = csrmod.prompt_for_subject_and_sans()
                    subj_str = _build_subj_from_dict(subj_dict) if subj_dict else None
                    csr_pem = csrmod.create_csr_from_key(args.key_file, subj_str, sans=san_list, passphrase=args.passphrase)
                else:
                    # Validate SANs supplied on CLI
                    norm_sans = []
                    if args.san:
                        wildcard_sans = []
                        try:
                            for s in args.san:
                                ns = csrmod.normalize_and_validate_san(s)
                                norm_sans.append(ns)
                                if ns.startswith("DNS:*.") or "*" in ns:
                                    wildcard_sans.append(ns)
                        except ValueError as e:
                                from .term import print_error
                                print_error(f"Invalid SAN provided: {e}")
                                return 1

                        # Handle wildcard SANs: interactive confirmation or explicit allow
                        if wildcard_sans:
                            if args.allow_wildcard:
                                # Use formatted warning helper for reusable behavior
                                from .term import print_warning
                                print_warning("WARNING: --allow-wildcard used. Wildcard SANs broaden certificate scope and can be risky.")
                            else:
                                # If interactive terminal, confirm each wildcard SAN
                                try:
                                    is_tty = sys.stdin.isatty()
                                except Exception:
                                    is_tty = False
                                if not is_tty:
                                    from .term import print_error
                                    print_error("Wildcard SAN detected in CLI arguments; rerun with --allow-wildcard to allow it in non-interactive mode.")
                                    return 1
                                # interactive confirm
                                for w in list(wildcard_sans):
                                    ans = input(f"Wildcard SAN detected: {w}. Type 'yes' to include it, or anything else to exclude: ").strip().lower()
                                    if ans != "yes":
                                        # remove from normalized list
                                        norm_sans = [x for x in norm_sans if x != w]
                                        from .term import print_info
                                        print_info(f"Excluded {w}")
                    # it as None so OpenSSL will not add subjectAltName.
                    san_to_use = norm_sans if args.san else None
                    csr_pem = csrmod.create_csr_from_key(args.key_file, subj_str, sans=san_to_use, passphrase=args.passphrase)

            if args.out:
                with open(args.out, "w", encoding="utf-8") as f:
                    f.write(csr_pem)
            else:
                sys.stdout.write(csr_pem)
            return 0

        if args.csr_cmd == "show":
            with open(args.csr_file, "r", encoding="utf-8") as f:
                csr_pem = f.read()
            from . import csr as csrmod
            # Rudimentary output: show the CSR text parsed by openssl
            import subprocess
            openssl = csrmod._openssl_bin()
            p = subprocess.run([openssl, "req", "-in", "/dev/stdin", "-noout", "-text"], input=csr_pem.encode("utf-8"), check=True, capture_output=True)
            sys.stdout.write(p.stdout.decode("utf-8"))
            return 0

        if args.csr_cmd == "submit":
            with open(args.csr_file, "r", encoding="utf-8") as f:
                csr_pem = f.read()

            # validate SANs if present and wildcard rules
            from . import csr as csrmod
            # parse SANs in the CSR via openssl text
            import subprocess
            openssl = csrmod._openssl_bin()
            p = subprocess.run([openssl, "req", "-in", "/dev/stdin", "-noout", "-text"], input=csr_pem.encode("utf-8"), check=True, capture_output=True)
            txt = p.stdout.decode("utf-8")
            import re
            sans = [f"DNS:{m.group(1)}" for m in re.finditer(r"DNS:([^,\s]+)", txt)]
            for m in re.finditer(r"IP:?\s*Address:?\s*([^,\s]+)", txt, flags=re.IGNORECASE):
                sans.append(f"IP:{m.group(1)}")

            # wildcard checks
            if any(s.startswith("DNS:*." ) or "*" in s for s in sans) and not args.allow_wildcard:
                from .term import print_error
                print_error("Wildcard SAN detected in CSR; pass --allow-wildcard to confirm you want to submit it.")
                return 1

            # dispatch to adapter
            from .ca.mock import MockCA
            from .ca.sectigo import SectigoCA
            if args.ca == "mock":
                adapter = MockCA()
            else:
                adapter = SectigoCA()

            req_id = adapter.submit_csr(csr_pem, args.name)
            from .term import print_info
            print_info(f"Submitted CSR, request id: {req_id}")

            if args.wait:
                status = adapter.poll_status(req_id, timeout=300)
                from .term import print_info
                print_info(f"Final status: {status}")
                if status == "issued":
                    cert = adapter.download_certificate(req_id)
                    if args.out:
                        with open(args.out, "w", encoding="utf-8") as f:
                            f.write(cert)
                    else:
                        sys.stdout.write(cert)
                else:
                    from .term import print_error
                    print_error(f"Request ended with status: {status}")
            return 0

    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
