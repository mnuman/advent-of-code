from day15 import *


def test_part1():
    assert part1("test_day15_1.txt") == 1320


def test_part2():
    assert part2("test_day15_1.txt") == 145


def test_token_value():
    assert token_value("rn=1") == 30
    assert token_value("HASH") == 52
    assert token_value("rn") == 0
    assert token_value("cm") == 0
