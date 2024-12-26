import day03


def test_read_data():
    data = day03.read_data("test_day03.txt")
    assert len(data) == 1


def test_part1():
    data = day03.read_data("test_day03.txt")
    assert day03.part1(data) == 161


def test_part2():
    data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    assert day03.part2(data) == 48
