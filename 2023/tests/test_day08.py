from day08 import *


def test_part1():
    assert part1("test_day08_1.txt") == 2
    assert part1("test_day08_2.txt") == 6


def test_part2():
    assert part2("test_day08_3.txt") == 6


def test_parse_lines():
    lines = ["RL", "", "AAA = (BBB, CCC)", "BBB = (DDD, EEE)", "CCC = (ZZZ, GGG)"]
    ins, conn = parse_lines(lines)
    assert ins == "RL"
    assert len(conn) == 3
    for k in ("AAA", "BBB", "CCC"):
        assert k in conn.keys()
