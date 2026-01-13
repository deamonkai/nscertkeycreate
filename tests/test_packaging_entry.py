"""Test verifying `pyproject.toml` exposes `nsctl` script entry."""


def test_pyproject_has_nsctl_entry():
    content = open("pyproject.toml").read()
    assert "nsctl" in content
    assert "nscert.cli:main" in content
