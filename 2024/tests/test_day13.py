import day13


def test_read_data():
    data = day13.read_data("test_day13.txt")
    assert len(data) == 4


def test_part1():
    data = day13.read_data("test_day13.txt")
    assert day13.part1(data) == 480


def test_part2():
    data = day13.read_data("test_day13.txt")
    assert day13.part2(data) == 875318608908
