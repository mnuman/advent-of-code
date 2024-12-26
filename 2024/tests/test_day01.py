import day01


def test_part1():
    locs_1, locs_2 = day01.read_data("data/test_day01.txt")
    assert day01.part1(locs_1, locs_2) == 11


def test_part2():
    locs_1, locs_2 = day01.read_data("data/test_day01.txt")
    assert day01.part2(locs_1, locs_2) == 31
