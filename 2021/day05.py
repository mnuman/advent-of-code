import re
from collections import Counter
from typing import Tuple, Callable

import utils

CoordinatePair = Tuple[int, int]
Vent = Tuple[CoordinatePair, CoordinatePair]
VentsList = list[Vent]


def read_file(filename: str) -> VentsList:
    """Read the file, consisting of coordinate pairs (x1,y1) --> (x2,y2), return list of start/end pairs"""
    data = utils.read_file(filename)
    result = []
    for line in data:
        coordinates = (re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)).groups()
        result.append(((int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3]))))
    return result


def vent_eligible(vent: Vent, filters: list[Callable]) -> bool:
    return len(filters) == 0 or any(vent_filter(vent) for vent_filter in filters)


def is_horizontal_vent(vent: Vent) -> bool:
    """Horizontal vents have the same y coordinate, only x varies"""
    return vent[0][1] == vent[1][1]


def is_vertical_vent(vent: Vent) -> bool:
    """Horizontal vents have the same x coordinate, only y varies"""
    return vent[0][0] == vent[1][0]


def is_diagonal_vent(vent: Vent) -> bool:
    """Diagonal vents have the same (absolute) difference in x and y coordinates"""
    return abs(vent[0][0] - vent[1][0]) == abs(vent[0][1] - vent[1][1])


def vent_trajectory_v1(vent: Vent) -> list[CoordinatePair]:
    """For a given vent, calculate all coordinate pairs covered. Currently, only horizontal or vertical vents
       are supported
    """
    if is_horizontal_vent(vent):
        xmin, xmax, y = min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0]), vent[0][1]
        return [(x, y) for x in range(xmin, xmax + 1)]
    elif is_vertical_vent(vent):
        ymin, ymax, x = min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1]), vent[0][0]
        return [(x, y) for y in range(ymin, ymax + 1)]
    return []


def vent_trajectory_v2(vent: Vent) -> list[CoordinatePair]:
    if is_diagonal_vent(vent):
        (x1, y1), (x2, y2) = vent
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        return [(x1 + step * step_x, y1 + step * step_y) for step in range(0, abs(x1 - x2) + 1)]
    else:
        return vent_trajectory_v1(vent)


def part1(filename: str) -> Counter:
    vents = read_file(filename)
    hits = Counter()
    for vent in vents:
        covered_coordinates = vent_trajectory_v1(vent)
        for coordinate in covered_coordinates:
            hits[coordinate] += 1
    danger_zone = [c for c in hits if hits[c] > 1]
    return len(danger_zone), danger_zone, hits


def part2(filename: str) -> Counter:
    vents = read_file(filename)
    hits = Counter()
    for vent in vents:
        covered_coordinates = vent_trajectory_v2(vent)
        for coordinate in covered_coordinates:
            hits[coordinate] += 1
    danger_zone = [c for c in hits if hits[c] > 1]
    return len(danger_zone), danger_zone, hits

if __name__ == '__main__':
    day05_1 = part1("data/day-05.txt")
    print("Day 05 - part 1", day05_1[0])
    day05_2 = part2("data/day-05.txt")
    print("Day 05 - part 2", day05_2[0])
