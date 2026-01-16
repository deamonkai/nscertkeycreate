def test_docs_mention_wildcard():
    import pathlib
    p = pathlib.Path(__file__).resolve().parents[1] / 'docs' / 'USAGE.md'
    txt = p.read_text()
    assert 'wildcard' in txt.lower()
    assert '--allow-wildcard' in txt
