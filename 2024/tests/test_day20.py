import day20
from collections import Counter


def test_read_data():
    start, end, grid, walls = day20.read_data("test_day20.txt")
    assert start == (3, 1)
    assert end == (7, 5)
    assert len(grid) + len(walls) == 15 * 15


def test_path():
    start, end, grid, walls = day20.read_data("test_day20.txt")
    path = day20.path(start, end, grid, walls)
    assert path[0] == start, "Path must start at start node"
    assert path[-1] == end, "Path must end at end node"
    assert len(path) == 85, "Path must have a total of 85 nodes - 84 steps"


def test_part1():
    start, end, grid, walls = day20.read_data("test_day20.txt")
    savings = day20.part1(start, end, grid, walls, 1)
    assert len(savings) == 44


def test_saved_distances():
    start, end, grid, walls = day20.read_data("test_day20.txt")
    cheats = day20.saved_distances(start, end, grid, walls)
    ctr = Counter(cheats.values())
    assert ctr[76] == 3
    assert ctr[74] == 4
    assert ctr[72] == 22
    assert ctr[70] == 12
    assert ctr[50] == 32


def test_part2():
    start, end, grid, walls = day20.read_data("test_day20.txt")
    savings = day20.part2(start, end, grid, walls, threshold=70)
    assert savings == 3 + 4 + 22 + 12
