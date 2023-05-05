from day14 import *


def test_readfile():
    start, rules = readfile("data/test-day-14.txt")
    assert start == "NNCB", "Starting point is correct"
    assert len(rules.keys()) == 16, "Correct number of rules read"
    assert rules["CH"] == "B", "Rule is present"


def test_run_part1():
    result = part1("data/test-day-14.txt")
    assert result == 1588, "1749 - 161 = 1588"
