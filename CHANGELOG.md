# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

- Add interactive confirmation for wildcard SANs when creating CSRs; CLI now supports `--allow-wildcard` to bypass interactive confirmation in non-interactive environments. The CLI will print a clear runtime warning when `--allow-wildcard` is used to make this unsafe action visible.
