from day05 import *


def test_part1():
    assert part1("test_day05_1.txt") == 35


def test_part2():
    assert part2("test_day05_1.txt") == 46


def test_project_range() -> None:
    r = Range(10, 10, 100)
    assert (100, 109) == r.project_range(10, 19)
    assert (100, 100) == r.project_range(10, 10)
    assert (109, 109) == r.project_range(19, 19)


def test_transform():
    mappings = [Range(30, 10, 300), Range(50, 10, 500), Range(10, 10, 100)]
    assert transform(ValueRange(10, 20), mappings) == [ValueRange(start=100, end=109)]
    assert transform(ValueRange(5, 25), mappings) == [
        ValueRange(5, 9),  # identity mapping for 5 - 9
        ValueRange(20, 25),  # identity mapping for 20 - 25
        ValueRange(100, 109),  # maps from           10 - 19
    ]
