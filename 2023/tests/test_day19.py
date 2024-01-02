from day19 import *


def test_part1():
    assert part1("test_day19_1.txt") == 19114


def test_part2():
    assert part2("test_day19_1.txt") == 167409079868000


def test_calc_ranges():
    assert calc_ranges((1, 40), "x<40") == ((1, 39), (40, 40))
    assert calc_ranges((40, 100), "x<40") == (None, (40, 100))
    assert calc_ranges((1, 40), "x>40") == (None, (1, 40))
    assert calc_ranges((1, 40), "True") == ((1, 40), None)
    assert calc_ranges((1351, 4000), "s<537") == (None, None)
