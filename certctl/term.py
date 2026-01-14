"""Terminal/TTY helpers for CLI formatting and safe output.

Provides small helpers to format and print warnings with optional ANSI styling
when the target stream is a TTY.
"""
from typing import Optional, TextIO
import sys


def format_warning(msg: str, stream: Optional[TextIO] = None) -> str:
    """Return a formatted warning string.

    If ``stream`` is a tty (supports ``.isatty()``) the message will be wrapped
    with ANSI bold yellow codes for prominence; otherwise the plain message is
    returned.
    """
    if stream is None:
        stream = sys.stderr
    try:
        is_tty = stream.isatty()
    except Exception:
        is_tty = False
    if is_tty:
        return f"\033[1;33m{msg}\033[0m"
    return msg


def print_warning(msg: str, stream: Optional[TextIO] = None) -> None:
    """Write a warning message followed by a newline to ``stream`` (defaults to stderr)."""
    if stream is None:
        stream = sys.stderr
    stream.write(format_warning(msg, stream) + "\n")


# Additional semantic helpers
def format_error(msg: str, stream: Optional[TextIO] = None) -> str:
    """Return a formatted error string (bold red on TTY)."""
    if stream is None:
        stream = sys.stderr
    try:
        is_tty = stream.isatty()
    except Exception:
        is_tty = False
    if is_tty:
        return f"\033[1;31m{msg}\033[0m"
    return msg


def print_error(msg: str, stream: Optional[TextIO] = None) -> None:
    """Write an error message followed by a newline to ``stream`` (defaults to stderr)."""
    if stream is None:
        stream = sys.stderr
    stream.write(format_error(msg, stream) + "\n")


def format_info(msg: str, stream: Optional[TextIO] = None) -> str:
    """Return a formatted info string (bold green on TTY)."""
    if stream is None:
        stream = sys.stderr
    try:
        is_tty = stream.isatty()
    except Exception:
        is_tty = False
    if is_tty:
        return f"\033[1;32m{msg}\033[0m"
    return msg


def print_info(msg: str, stream: Optional[TextIO] = None) -> None:
    """Write an info message followed by a newline to ``stream`` (defaults to stderr)."""
    if stream is None:
        stream = sys.stderr
    stream.write(format_info(msg, stream) + "\n")
