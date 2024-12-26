from collections import defaultdict
from itertools import combinations
import file_utils as f


def read_data(fname: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    """
    Build a dictionary of positions row,col by key is frequency (character) as only
    the same signal needs to be considered.
    Return dictionary, number of rows and number of columns.
    """
    data = defaultdict(list)
    raw_data = f.read_file(fname)
    for r, row in enumerate(raw_data):
        for c, cell in enumerate(row):
            if cell != ".":
                data[cell].append((r, c))
    return data, len(raw_data), len(raw_data[0])


def nodes(
    signals: dict[str, list[tuple[int, int]]], rows: int, cols: int
) -> set[tuple[int, int]]:
    """
    Find the nodes in the grid. Process each two combinations of the same signal
    and calculate the position of the node. If the node is within the grid, add it
    to the result set.
    The position must be along the line connecting s1 to s2. It can either be twice
    as far from s1 as from s2, or it can be twice as far from s2 as from s1 (that
    is the factor)
    """
    result = set()
    for freq in signals.keys():
        for s1, s2 in combinations(signals[freq], 2):
            for factor in (-1, 2):
                p = s1[0] + factor * (s2[0] - s1[0]), s1[1] + factor * (s2[1] - s1[1])
                if 0 <= p[0] < rows and 0 <= p[1] < cols:
                    result.add(p)
    return result


def resonant_harmonic_nodes(
    signals: dict[str, list[tuple[int, int]]], rows: int, cols: int
) -> set[tuple[int, int]]:
    """
    Find the nodes in the grid. Process each two combinations of the same signal
    and calculate the position of the node. If the node is within the grid, add it
    to the result set.
    Qualifying positions are along the line connecting s1 to s2.
    """
    result = set()
    for freq in signals.keys():
        for s1, s2 in combinations(signals[freq], 2):
            factor = 1
            candidate_in_grid = True
            while candidate_in_grid:
                candidate_in_grid = False
                dr = s2[0] - s1[0]
                dc = s2[1] - s1[1]
                candidate_1 = s1[0] + factor * dr, s1[1] + factor * dc
                candidate_2 = s2[0] - factor * dr, s2[1] - factor * dc
                if 0 <= candidate_1[0] < rows and 0 <= candidate_1[1] < cols:
                    candidate_in_grid = True
                    result.add(candidate_1)
                if 0 <= candidate_2[0] < rows and 0 <= candidate_2[1] < cols:
                    candidate_in_grid = True
                    result.add(candidate_2)
                factor += 1
    return result


def part1(signals, rows, cols):
    return nodes(signals, rows, cols)


def part2(signals, rows, cols):
    return resonant_harmonic_nodes(signals, rows, cols)


if __name__ == "__main__":
    signals, rows, cols = read_data("day08.txt")
    print(f"Part 1: {len(part1(signals, rows, cols))}")
    print(f"Part 2: {len(part2(signals, rows, cols))}")
