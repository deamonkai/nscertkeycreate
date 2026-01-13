def test_term_error_and_info_format(monkeypatch):
    from nscert import term

    class Fake:
        def isatty(self):
            return True
        written = ''
        def write(self, s):
            Fake.written += s

    fake = Fake()
    # error
    e = term.format_error('danger', stream=fake)
    assert '\033[1;31m' in e and '\033[0m' in e
    term.print_error('err', stream=fake)
    assert '\033[1;31m' in Fake.written

    # info
    i = term.format_info('ok', stream=fake)
    assert '\033[1;32m' in i and '\033[0m' in i
    term.print_info('info', stream=fake)
    assert '\033[1;32m' in Fake.written
