from day13 import *


def test_transpose():
    lines = ["AAAA", "BBBB", "CCCC"]
    lines_transposed = transpose(lines)
    assert len(lines) == len(lines_transposed[0])
    assert len(lines[0]) == len(lines_transposed)
    assert lines_transposed == ["ABC"] * 4


def test_part1():
    assert part1("test_day13_1.txt") == 405

def test_part2():
    assert part2("test_day13_1.txt") == 400
