from __future__ import annotations

import os
import time
from pathlib import Path


class FileLock:
    """Cross-platform-ish lock using atomic create.

    Good enough for single-machine runs (macOS/Windows/Linux).
    """

    def __init__(self, path: str, timeout: float = 0.0):
        self.path = Path(path)
        self.timeout = timeout
        self._fd: int | None = None

    def acquire(self) -> None:
        start = time.time()
        while True:
            try:
                self._fd = os.open(str(self.path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                os.write(self._fd, str(os.getpid()).encode())
                return
            except FileExistsError:
                if self.timeout and (time.time() - start) < self.timeout:
                    time.sleep(0.2)
                    continue
                raise RuntimeError(f"Lock held: {self.path}")

    def release(self) -> None:
        try:
            if self._fd is not None:
                os.close(self._fd)
        finally:
            self._fd = None
            try:
                self.path.unlink(missing_ok=True)  # py3.8+: missing_ok
            except TypeError:
                if self.path.exists():
                    self.path.unlink()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.release()
        return False
