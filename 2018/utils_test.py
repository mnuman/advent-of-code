import utils


def test_read_file():
    f = utils.read_file('data/utils-single-line.txt')
    assert len(f) == 6
    assert f[0] == '+1'
    assert f[1] == '-2'


def test_read_file_with_convert():
    def toint(s):
        """Inline conversion function from string to integer"""
        return int(s)

    f = utils.read_file('data/utils-single-line.txt', convert=toint)
    assert len(f) == 6
    assert f[0] == 1
    assert f[1] == -2
