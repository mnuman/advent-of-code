from day12 import *


def test_part1():
    assert part1("test_day12_1.txt") == 21


def test_part1a():
    assert part1a("test_day12_1.txt") == 21


def test_part2():
    assert part2("test_day12_1.txt") == 525152


def test_generate_combinations():
    assert [*generate_combinations("###")] == ["###"]
    x = [*generate_combinations("#?.")]
    assert len(x) == 2
    assert all(["#..", "##." in x])

    x = [*generate_combinations("???")]
    assert len(x) == 8
    assert all(["#..", "##.", "###" in x])
