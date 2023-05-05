from copy import deepcopy
from itertools import product

from dijkstar import Graph, find_path

import utils


def readfile(filename):
    lines = utils.read_file(filename)
    return [list(map(int, [c for c in row])) for row in lines]


def neighbours(current_row, current_col, max_row, max_col, offsets=(-1, 0, 1)):
    """
    Determine all neighbours (row,col) for point at (current_row,current_col) where we:
    - do not move diagonally
    - not identical to current point and
    - stay within bounds
    """
    return [(current_row + rc[0], current_col + rc[1]) for rc in product(offsets, offsets)
            if (rc[0] != 0 or rc[1] != 0) and
            0 <= current_col + rc[1] <= max_col and
            0 <= current_row + rc[0] <= max_row and
            rc[0] ** 2 + rc[1] ** 2 == 1
            ]


def convert_weights_to_graph(entry_weights):
    number_rows, number_cols = len(entry_weights), len(entry_weights[0])
    g = Graph()
    for r in range(number_rows):
        for c in range(number_cols):
            for n_row, n_col in neighbours(r, c, number_rows - 1, number_cols - 1):
                g.add_edge(r * number_cols + c, n_row * number_cols + n_col, entry_weights[n_row][n_col])
    return g


def part1(filename):
    weights = readfile(filename)
    graph = convert_weights_to_graph(weights)
    path_info = find_path(graph, 0, len(weights) * len(weights[0]) - 1)
    return path_info.total_cost


def expand(weights, factor=5):
    new_weights = deepcopy(weights)  # copy the original weights
    num_items = len(weights[0])
    w = lambda v: v + 1 if v + 1 < 10 else 1
    for f in range(1, factor):
        for r in range(len(weights)):
            new_weights[r] += [w(c) for c in new_weights[r][-num_items:]]
    for f in range(1, factor):
        for row_idx in range(len(weights)):
            # f = 2, row_idx 0:10=num_items; rows 0-19 are already present
            new_weights.append([w(c) for c in new_weights[(f-1)*num_items+row_idx]])
    return new_weights


def part2(filename):
    weights = readfile(filename)
    expanded_weights = expand(weights)
    graph = convert_weights_to_graph(expanded_weights)
    path_info = find_path(graph, 0, len(expanded_weights) * len(expanded_weights[0]) - 1)
    return path_info.total_cost


if __name__ == '__main__':
    day15_1 = part1("data/day-15.txt")
    print("Day 15 - part 1", day15_1)
    day15_2 = part2("data/day-15.txt")
    print("Day 15 - part 2", day15_2)
