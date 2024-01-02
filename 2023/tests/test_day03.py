from day03 import *


def test_offsets():
    # match  line above and below, also diagonal positions. exclude range on line itself
    assert offsets(2, 1, 2, 10, 10) == [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ], "Include positions on lines above and below, exclude match itself"

    assert offsets(0, 1, 2, 10, 10) == [
        (0, 0),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
    ], "Adjacent positions, no line above, exclude match itself"


def test_has_adjacent_symbol():
    lines = ["467..114..", "...*......", "..35..633."]
    assert has_adjacent_symbol(
        lines=lines, line_number=0, start=0, end=2
    ), "467 has a diagonal adjacent symbol"
    assert not has_adjacent_symbol(
        lines=lines, line_number=0, start=5, end=7
    ), "114 has no adjacent symbol"
    assert has_adjacent_symbol(
        lines=lines, line_number=2, start=2, end=3
    ), "35 has an adjacent symbol"


def test_part1():
    assert part1("test_day03_1.txt") == 4361, "Incorrect sum."


def test_parts_around_gear():
    lines = ["467..114..", "...*......", "..35..633."]
    assert (0, 0) == find_parts_around_gear(
        gear=(1, 3), parts=[PartNumber(0, 0, 2, 467)]
    )
    assert (467, 35) == find_parts_around_gear(
        gear=(1, 3), parts=[PartNumber(0, 0, 2, 467), PartNumber(2, 2, 3, 35)]
    )


def test_part2():
    assert part2("test_day03_1.txt") == 467835, "Incorrect gear product."
