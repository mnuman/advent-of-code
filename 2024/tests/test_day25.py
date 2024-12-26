import day25


def test_read_data():
    locks, keys = day25.read_data("test_day25.txt")
    assert len(locks) == 2
    assert len(keys) == 3


def test_part1():
    locks, keys = day25.read_data("test_day25.txt")
    assert day25.part1(locks, keys) == 3
