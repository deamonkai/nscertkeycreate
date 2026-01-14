"""Verify `bin/certctl` wrapper exists and is executable."""
import os


def test_nsctl_exists_and_executable():
    path = os.path.join(os.path.dirname(__file__), "..", "bin", "certctl")
    path = os.path.abspath(path)
    assert os.path.exists(path)
    assert os.access(path, os.X_OK)
