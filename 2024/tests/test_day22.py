from collections import defaultdict
import day22


def test_generate_secret():
    secret = 123
    result = []
    for i in range(10):
        secret = day22.generate_secret(secret)
        result.append(secret)
    assert result == [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]


def test_read_data():
    data = day22.read_data("test_day22.txt")
    assert len(data) == 4


def test_part1():
    data = day22.read_data("test_day22.txt")
    assert day22.part1(data) == 37327623


def test_part2():
    # using the global becomes messy with the testcases - damn!
    day22.buyers_prices = defaultdict(list)
    data = [1, 2, 3, 2024]  # this is different from the test_day22.txt!
    day22.part1(data)
    assert day22.part2(data) == 23
