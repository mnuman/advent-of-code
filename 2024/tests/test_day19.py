import day19


def test_read_data():
    data = day19.read_data("test_day19.txt")
    assert len(data[0]) == 8
    assert len(data[1]) == 8


def test_part1():
    data = day19.read_data("test_day19.txt")
    assert day19.part1(data) == 6


def test_part2():
    data = day19.read_data("test_day19.txt")
    assert day19.part2(data) == 16
