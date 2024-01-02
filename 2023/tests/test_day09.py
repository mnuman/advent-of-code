from day09 import *


def test_part1():
    assert part1("test_day09_1.txt") == 114


def test_part2():
    assert part2("test_day09_1.txt") == 2


def test_line_diffs():
    assert line_diffs([3, 3]) == [0]
    assert line_diffs([1, 2, 3, 4, 2]) == [1, 1, 1, -2]


def test_reduce_and_extend():
    assert reduce_and_extend([0, 3, 6, 9, 12, 15]) == 18
    assert reduce_and_extend([1, 3, 6, 10, 15, 21]) == 28
    
    # simply reversing the input ensures the previous algorithm works
    l = [10, 13, 16, 21, 30, 45]
    l.reverse()
    assert reduce_and_extend(l) == 5
