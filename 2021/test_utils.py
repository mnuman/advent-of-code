import utils


def test_read_file():
    f = utils.read_file('data/utils-single-line.txt')
    assert len(f) == 6
    assert f[0] == '+1'
    assert f[1] == '-2'


def test_read_file_with_convert():
    f = utils.read_file('data/utils-single-line.txt', convert=utils.toint)
    assert len(f) == 6
    assert f[0] == 1
    assert f[1] == -2


def test_binary_to_int():
    assert utils.binary_to_int("0") == 0
    assert utils.binary_to_int("00000") == 0
    assert utils.binary_to_int("1111") == 15
