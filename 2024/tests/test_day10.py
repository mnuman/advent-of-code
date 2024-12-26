import day10


def test_read_data():
    data = day10.read_data("test_day10.txt")
    assert len(data) == 8
    assert all(len(line) == 8 for line in data)


def test_part1():
    data = day10.read_data("test_day10.txt")
    assert day10.part1(data) == 36


def test_part2():
    data = day10.read_data("test_day10.txt")
    assert day10.part2(data) == 81
