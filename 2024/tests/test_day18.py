import day18


def test_read_data():
    data = day18.read_data("test_day18.txt")
    assert len(data) == 25


def test_part1():
    data = day18.read_data("test_day18.txt")
    assert day18.part1(data, max_coord=6, bytes=12) == 22


def test_part2():
    data = day18.read_data("test_day18.txt")
    assert day18.part2(data, max_coord=6, bytes=12) == (6, 1)
