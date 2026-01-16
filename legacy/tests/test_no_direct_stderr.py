import pathlib


def test_no_direct_stderr_writes():
    root = pathlib.Path(__file__).resolve().parents[1]
    # Only check package sources and the top-level script(s); ignore virtualenv and tests
    py_files = list((root / 'certctl').rglob('*.py'))
    main_script = root / 'nscertkeycreate.py'
    if main_script.exists():
        py_files.append(main_script)
    offending = []
    for p in py_files:
        txt = p.read_text()
        if 'sys.stderr.write' in txt or 'file=sys.stderr' in txt:
            offending.append(str(p))
    assert not offending, f"Found direct stderr writes in: {offending}"
