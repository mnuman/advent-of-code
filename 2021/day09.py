from itertools import product
from typing import Iterable, NamedTuple

import utils

"""
     x
     0 1 2 3 4 ... n
  y 0
    1
    2
    :
    n 
"""


class Point(NamedTuple):
    col: int
    row: int

    def __add__(self, other):
        return Point(self.col + other.col, self.row + other.row)


def read_file(filename: str) -> Iterable[Iterable[int]]:
    data = utils.read_file(filename)
    return [[int(c) for c in line] for line in data]


def neighbours(current: Point, bottom_right: Point) -> Iterable[Point]:
    """
    Determine the one-step neighbours for current point given coordinates of bottom right
    """
    offsets = (-1, 0, 1)
    return [current + Point(*xy) for xy in product(offsets, offsets)
            if (abs(xy[0]) + abs(xy[1])) == 1 and
            0 <= current.col + xy[0] <= bottom_right.col and
            0 <= current.row + xy[1] <= bottom_right.row]


def all_neighbours(current: Point, bottom_right: Point) -> Iterable[Point]:
    """
    Determine all neighbours for current point given coordinates of bottom right,
    may be diagonal as well, as long as we move and stay within bounds
    """
    offsets = (-1, 0, 1)
    return [current + Point(*xy) for xy in product(offsets, offsets)
            if (xy[0] != 0 or xy[1] != 0) and
            0 <= current.col + xy[0] <= bottom_right.col and
            0 <= current.row + xy[1] <= bottom_right.row]


def scan(data_lines, fn):
    col_max = len(data_lines[0])
    row_max = len(data_lines)
    bottom_right = Point(col_max - 1, row_max - 1)
    return [fn(data_lines[row][col]) for col in range(0, col_max) for row in range(0, row_max) if
            all(data_lines[row][col] < data_lines[n.row][n.col] for n in neighbours(Point(col, row), bottom_right))]


def find_sinks(data_lines):
    col_max = len(data_lines[0])
    row_max = len(data_lines)
    bottom_right = Point(col_max - 1, row_max - 1)
    return [Point(col, row) for col in range(0, col_max) for row in range(0, row_max) if
            all(data_lines[row][col] < data_lines[n.row][n.col] for n in neighbours(Point(col, row), bottom_right))]


def find_all_basins(data_lines, sinks):
    basins = []
    for sink in sinks:
        basins.append(find_basin_from_sink(data_lines, sink))
    return basins


def find_basin_from_sink(data_lines, start):
    col_max = len(data_lines[0])
    row_max = len(data_lines)
    bottom_right = Point(col=col_max - 1, row=row_max - 1)
    basin = {start}
    new_found = True
    while new_found:
        new_points = {n for p in basin for n in neighbours(p, bottom_right)
                      if data_lines[n.row][n.col] != 9 and Point(row=n.row, col=n.col) not in basin}
        new_found = len(new_points) > 0
        basin.update(new_points)
    return basin


def part1(filename):
    data = read_file(filename)
    result = sum(scan(data, lambda x: x + 1))
    return result


def part2(filename):
    data = read_file(filename)
    result = 1
    for basin in sorted(find_all_basins(data, find_sinks(data)), key=lambda b: len(b))[-3:]:
        result *= len(basin)
    return result


if __name__ == '__main__':
    day09_1 = part1("data/day-09.txt")
    print("Day 09 - part 1", day09_1)
    day09_2 = part2("data/day-09.txt")
    print("Day 09 - part 2", day09_2)
