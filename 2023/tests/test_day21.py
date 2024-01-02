from day21 import *


def test_part1():
    assert part1("test_day21_1.txt", 6) == 16


def test_part2():
    assert part2("test_day21_1.txt", 6) == 16
    assert part2("test_day21_1.txt", 10) == 50
    assert part2("test_day21_1.txt", 50) == 1594
    assert part2("test_day21_1.txt", 100) == 6536
    assert part2("test_day21_1.txt", 500) == 167004  # largest feasible for brute force


def test_part2b():
    assert part2("test_day21_2.txt", 6) == 2


def test_sample_part2():
    sample_part2("test_day21_1.txt", 50)
