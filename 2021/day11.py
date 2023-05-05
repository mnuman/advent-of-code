from itertools import product
from typing import Callable, Iterable

import utils


def adjacent_cells(row: int, col: int, max_row: int, max_col: int) -> Iterable[tuple[int, int]]:
    """Return all valid adjacent cells for a cell located at row, col with *inclusive* max_row/max_col dimensions"""
    offset = (1, 0, -1)
    return [(row + rc[0], col + rc[1]) for rc in product(offset, offset) if
            ((rc[0] != 0 or rc[1] != 0) and 0 <= row + rc[0] <= max_row and 0 <= col + rc[1] <= max_col)]


def readfile(filename):
    lines = utils.read_file(filename)
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])
    return grid


def increase(grid):
    """Increase the value of the row/col in grid"""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1


def reset(grid):
    """Reset all values > 9, return 1 if cell flashed, 0 otherwise"""
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 9:
                grid[r][c] = 0
                score += 1
    return score


def flash(grid):
    """Stop iterating if no new flashers found"""
    flashers = set()
    flashed = True
    while flashed:
        before_flash_count = len(flashers)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 9 and (r, c) not in flashers:
                    neighbours = adjacent_cells(r, c, len(grid)-1, len(grid[0])-1)
                    for n_row, n_col in neighbours:
                        grid[n_row][n_col] += 1
                        flashers.add((r, c))
        flashed = len(flashers) - before_flash_count > 0


def part1(filename):
    grid = readfile(filename)
    score = 0
    for i in range(100):
        increase(grid)
        flash(grid)
        score += reset(grid)
    return score


def part2(filename):
    grid = readfile(filename)
    all_octopuses = len(grid) * len(grid[0])
    flashers = 0
    iteration = 0
    while flashers != all_octopuses:
        iteration += 1
        increase(grid)
        flash(grid)
        flashers = reset(grid)
    return iteration


if __name__ == '__main__':
    day11_1 = part1("data/day-11.txt")
    print("Day 11 - part 1", day11_1)
    day11_2 = part2("data/day-11.txt")
    print("Day 11 - part 2", day11_2)
