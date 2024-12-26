import day08


def test_read_data():
    data, rows, cols = day08.read_data("test_day08.txt")
    assert rows == 12
    assert cols == 12
    assert len(data.keys()) == 2
    assert len(data["0"]) == 4
    assert len(data["A"]) == 3


def test_part1():
    data, rows, cols = day08.read_data("test_day08.txt")
    nodes = day08.part1(data, rows, cols)
    assert len(nodes) == 14


def test_part2():
    data, rows, cols = day08.read_data("test_day08.txt")
    nodes = day08.part2(data, rows, cols)
    assert len(nodes) == 34
