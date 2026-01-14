"""Test verifying `pyproject.toml` exposes `certctl` script entry."""


def test_pyproject_has_nsctl_entry():
    content = open("pyproject.toml").read()
    assert "certctl" in content
    assert "certctl.cli:main" in content
