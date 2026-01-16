Development
===========

This repository is a small package with modular components.

To run unit tests (requires `pytest`, `responses`):

Install test dependencies (recommend using a virtualenv):

```bash
python -m pip install --upgrade pytest responses
```

Then run the tests:

```bash
python -m pytest -q
```

Current work: NetScaler Console polling + key/CSR scripts with tests.

Note: The NetScaler Console Device API proxy (`authorize_deviceapiproxy` and
`enable_apiproxy_credentials`) is disabled by default. We enabled it on the
lab Console to support future Console-proxy import workflows.
