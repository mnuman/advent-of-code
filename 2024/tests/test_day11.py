import day11


def test_read_data():
    data = day11.read_data("test_day11.txt")
    assert len(data) == 2


def test_part1():
    data = day11.read_data("test_day11.txt")
    assert day11.part1(data) == 55312


def test_part2():
    data = day11.read_data("test_day11.txt")
    assert day11.part2(data) == 65601038650482
