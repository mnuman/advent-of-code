import day07


def test_part1():
    data = day07.read_data("test_day07.txt")
    assert day07.part1(data) == 3749


def test_part2():
    data = day07.read_data("test_day07.txt")
    assert day07.part2(data) == 11387


def test_can_produce_part1():
    assert day07.can_produce(day07.operators_part1, [1, 2, 4], 8)
    assert day07.can_produce(day07.operators_part1, [1, 2, 4], 7)
    assert day07.can_produce(day07.operators_part1, [1, 2, 4], 6)
    assert not day07.can_produce(day07.operators_part1, [1, 2, 4], 5)
    assert day07.can_produce(day07.operators_part1, [11, 6, 16, 20], 292)


def test_can_produce_part2():
    assert day07.can_produce(day07.operators_part2, [15, 6], 156)
    assert day07.can_produce(day07.operators_part2, [6, 8, 6, 15], 7290)
