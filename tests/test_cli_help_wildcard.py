import pytest


def test_csr_create_help_contains_wildcard(capsys):
    from nscert import cli
    p = cli.build_parser()
    with pytest.raises(SystemExit):
        p.parse_args(["csr", "create", "--help"])
    captured = capsys.readouterr()
    out = captured.out + captured.err
    assert '--allow-wildcard' in out
    assert 'wildcard' in out.lower()
