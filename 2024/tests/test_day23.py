import day23


def test_read_data():
    data = day23.read_data("test_day23.txt")
    assert len(data) == 32


def test_part1():
    data = day23.read_data("test_day23.txt")
    assert day23.part1(data) == 7


def test_part2():
    data = day23.read_data("test_day23.txt")
    assert day23.part2(data) == "co,de,ka,ta"
