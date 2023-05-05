from day11 import *


def test_read_file():
    grid_data = readfile("data/test-day-11.txt")
    assert len(grid_data) == 10, "Data grid for test file is ten lines"
    assert all([len(line) == 10 for line in grid_data]), "All lines have length 10"


def test_adjacent_cells():
    assert adjacent_cells(0, 0, 0, 0) == [], "No grid - no cells"
    assert sorted(adjacent_cells(1, 1, 2, 2)) == sorted(
        [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)])


def test_part1():
    flashes = part1("data/test-day-11.txt")
    assert flashes == 1656


def test_part2():
    flashes = part2("data/test-day-11.txt")
    assert flashes == 195

