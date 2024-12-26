import day06


def test_part1():
    p1 = day06.Day06("test_day06.txt")
    assert len(p1.part1()) == 41


def test_part2():
    p2 = day06.Day06("test_day06.txt")
    assert p2.part2() == 6
