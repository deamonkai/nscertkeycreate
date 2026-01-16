def test_term_format_and_print(monkeypatch):
    import sys
    from certctl import term

    class Fake:
        def isatty(self):
            return False
        def write(self, s):
            Fake.written = getattr(Fake, 'written', '') + s
    fake = Fake()
    # plain
    assert term.format_warning('w', stream=fake) == 'w'
    term.print_warning('x', stream=fake)
    assert 'x' in Fake.written

    # TTY
    class FakeTTY(Fake):
        def isatty(self):
            return True
    fty = FakeTTY()
    out = term.format_warning('z', stream=fty)
    assert '\033[1;33m' in out and '\033[0m' in out
    term.print_warning('y', stream=fty)
    # ensure it wrote the ANSI code
    assert '\033[1;33m' in Fake.written or '\033[1;33m' in fty.write('')
