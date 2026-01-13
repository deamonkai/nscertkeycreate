def test_format_warning_colored_and_plain(monkeypatch, capsys):
    import sys
    from nscert import utils

    # Non-tty stream -> plain
    class Fake:
        def isatty(self):
            return False
        def write(self, s):
            pass
    fake = Fake()
    out_plain = utils.format_warning("test", stream=fake)
    assert out_plain == "test"

    # TTY stream -> colored
    class FakeTTY(Fake):
        def isatty(self):
            return True
    fty = FakeTTY()
    out_colored = utils.format_warning("test", stream=fty)
    assert "\033[1;33mtest\033[0m" == out_colored


def test_print_warning_writes(monkeypatch, capsys):
    import sys
    from nscert import utils

    class FakeTTY:
        def isatty(self):
            return True
        written = ""
        def write(self, s):
            # accumulate
            FakeTTY.written += s
    f = FakeTTY()
    utils.print_warning("hello", stream=f)
    assert "hello" in FakeTTY.written
    assert "\033[1;33m" in FakeTTY.written
