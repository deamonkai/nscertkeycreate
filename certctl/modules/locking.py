"""Cross-platform, single-host file lock.

Goal: keep it simple; allow running on macOS/Linux/Windows without extra services.
"""

from __future__ import annotations

import os
import time
from contextlib import contextmanager


@contextmanager
def file_lock(lock_path: str, timeout_s: int = 30, poll_s: float = 0.2):
    """Acquire an exclusive lock using an atomic create.

    This is intentionally minimal. It protects against concurrent runs on a single host.
    """
    start = time.time()
    fd = None
    while True:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            os.write(fd, str(os.getpid()).encode())
            break
        except FileExistsError:
            if time.time() - start > timeout_s:
                raise TimeoutError(f"Could not acquire lock within {timeout_s}s: {lock_path}")
            time.sleep(poll_s)

    try:
        yield
    finally:
        try:
            if fd is not None:
                os.close(fd)
            os.unlink(lock_path)
        except Exception:
            pass
