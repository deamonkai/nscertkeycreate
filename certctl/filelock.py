from __future__ import annotations

import os
import time
from dataclasses import dataclass


@dataclass
class FileLock:
    """Cross-platform advisory file lock.

    - POSIX: fcntl.flock
    - Windows: msvcrt.locking

    Best-effort: intended for a single machine on a local filesystem.
    """

    path: str
    timeout_seconds: float = 0.0
    poll_interval_seconds: float = 0.1

    def __post_init__(self) -> None:
        self._fh = None

    def acquire(self) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(self.path)) or '.', exist_ok=True)
        fh = open(self.path, 'a+b')
        start = time.time()

        while True:
            try:
                if os.name == 'nt':
                    import msvcrt
                    # lock 1 byte; non-blocking attempt
                    msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                self._fh = fh
                return
            except Exception:
                if self.timeout_seconds and (time.time() - start) >= self.timeout_seconds:
                    fh.close()
                    raise TimeoutError(f"Timed out waiting for lock: {self.path}")
                time.sleep(self.poll_interval_seconds)

    def release(self) -> None:
        if not self._fh:
            return
        try:
            if os.name == 'nt':
                import msvcrt
                self._fh.seek(0)
                msvcrt.locking(self._fh.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self._fh.fileno(), fcntl.LOCK_UN)
        finally:
            self._fh.close()
            self._fh = None

    def __enter__(self) -> "FileLock":
        self.acquire()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.release()
