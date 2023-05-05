import day07


def test_read_file():
    crabs = day07.read_file("data/test-day-07.txt")
    assert len(crabs) == 10, "Ten positions read"
    assert crabs == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_best_position():
    assert day07.best_pos([0, 0]) == 0
    assert day07.best_pos([1, 7]) == 4


def test_fuel_cost():
    assert day07.fuel_cost([0, 0, 0], 0) == 0, "No movement doesn't cost fuel"
    assert day07.fuel_cost([0, 1, 2], 1) == 2, "Two units"


def test_part1():
    assert day07.part1("data/test-day-07.txt") == (2, 37)


def test_part2():
    assert day07.part2("data/test-day-07.txt") == (5, 168)
