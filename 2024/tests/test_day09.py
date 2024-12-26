import day09


def test_read_data():
    data, files, freespace = day09.read_data("test_day09.txt")
    assert len(data) == 42


def test_part1():
    data, files, freespace = day09.read_data("test_day09.txt")
    assert day09.part1(data) == 1928


def test_part2():
    data, files, freespace = day09.read_data("test_day09.txt")
    assert day09.part2(files, freespace) == 2858
