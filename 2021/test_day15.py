from day15 import *


def test_readfile():
    grid = readfile("data/test-day-15.txt")
    assert len(grid) == 10, "Ten rows in test data"
    assert all([len(row) == 10 for row in grid]), "All grid rows have identical lengths."


def test_neighbours():
    assert neighbours(current_row=0, current_col=0, max_row=0,
                      max_col=0) == [], "No neighbours possible for a grid of a single point"
    origin_neighbours = neighbours(current_row=0, current_col=0, max_row=5, max_col=5)
    assert sorted(origin_neighbours) == sorted([(0, 1), (1, 0)])
    all_neighbours = neighbours(current_row=1, current_col=1, max_row=5, max_col=5)
    assert sorted(all_neighbours) == sorted([(0, 1), (1, 0), (1, 2), (2, 1)])
    edge_neighbours = neighbours(current_row=1, current_col=5, max_row=5, max_col=5)
    assert sorted(edge_neighbours) == sorted([(0, 5), (1, 4), (2, 5)])


def test_part1():
    assert part1("data/test-day-15.txt") == 40


def test_expand():
    w = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    f = 3
    nw = expand(w, factor=f)
    assert len(nw) == f * len(w), "Number of rows is correct"
    assert all([len(nw[r]) == f * len(w[r % len(w)]) for r in range(len(nw))]), "All rows have correct lengths"
    assert nw[3] == [2, 3, 4, 3, 4, 5, 4, 5, 6], "First copied row is correct"


def test_part2():
    assert part2("data/test-day-15.txt") == 315
