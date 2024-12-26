import day02


def test_read_data():
    data = day02.read_data("test_day02.txt")
    assert len(data) == 6
    assert data[0] == [7, 6, 4, 2, 1]


def test_part1():
    data = day02.read_data("test_day02.txt")
    assert day02.part1(data) == 2


def test_part2():
    data = day02.read_data("test_day02.txt")
    assert day02.part2(data) == 4
