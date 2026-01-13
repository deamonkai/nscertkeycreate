Development
===========

This repository is being refactored into a small package with modular components.

To run unit tests (requires `pytest`):

Install pytest (recommend using a virtualenv):

```bash
python -m pip install --upgrade pytest
```

Then run the tests:

```bash
python -m pytest -q
```

Current work: scaffolded `nscert` package and implemented `extract_pem_from_json` utility with tests.
