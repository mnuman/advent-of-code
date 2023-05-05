from day09 import *


def test_read_file():
    data = read_file("data/test-day-09.txt")
    assert len(data) == 5, "Test file contains 5 lines"
    assert all([len(line) == 10 for line in data]), "All lines must contain 10 elements"


def test_neighbours():
    bottom_right = Point(10, 10)
    assert sorted(neighbours(Point(0, 0), bottom_right)) == sorted(
        [Point(0, 1), Point(1, 0)]), "Origin has only two neighbours"
    assert sorted(neighbours(Point(1, 1), bottom_right)) == sorted(
        [Point(0, 1), Point(1, 0), Point(1, 2), Point(2, 1)]), "Non-edge point has four neighbours"
    assert sorted(neighbours(Point(0, 1), bottom_right)) == sorted(
        [Point(0, 2), Point(0, 0), Point(1, 1)]), "Boundary point has three neighbours"
    assert sorted(neighbours(Point(1, 0), bottom_right)) == sorted(
        [Point(2, 0), Point(0, 0), Point(1, 1)]), "Boundary point has three neighbours"
    assert sorted(neighbours(Point(10, 10), bottom_right)) == sorted(
        [Point(10, 9), Point(9, 10)]), "Boundary point has two neighbours"
    assert sorted(neighbours(Point(10, 8), bottom_right)) == sorted(
        [Point(10, 9), Point(9, 8), Point(10, 7)]), "Boundary point has three neighbours"


def test_all_neighbours():
    bottom_right = Point(10, 10)
    direct_neighbours = all_neighbours(Point(row=5, col=5), bottom_right)
    assert len(direct_neighbours) == 8
    assert sorted(direct_neighbours) == sorted(
        [Point(4, 6), Point(5, 6), Point(6, 6), Point(4, 5), Point(6, 5), Point(4, 4), Point(5, 4), Point(6, 4)])


def test_scan():
    datalines = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0]]
    assert scan(datalines, lambda x: x) == [1, 0]


def test_find_sinks():
    data = read_file("data/test-day-09.txt")
    sinks = sorted(find_sinks(data))
    assert sinks == sorted([Point(1, 0), Point(9, 0), Point(2, 2), Point(6, 4)])


def test_part1():
    assert part1("data/test-day-09.txt") == 15, "Test data yields correct result"


def test_part2():
    assert part2("data/test-day-09.txt") == 1134, "Test data yields correct result"


def test_find_basin_from_sink():
    data = read_file("data/test-day-09.txt")
    basin = find_basin_from_sink(data, Point(row=0, col=1))
    assert sorted(basin) == sorted({Point(row=0, col=0), Point(row=0, col=1), Point(row=1, col=0)})
