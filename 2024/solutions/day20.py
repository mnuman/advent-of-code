import file_utils as f
from itertools import combinations
from aoc_utils import manhattan_distance
from collections import Counter

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_data(fname: str):
    grid = set()
    start, end = None, None
    walls = set()
    for r, line in enumerate(f.read_file(fname)):
        for c, char in enumerate(line):
            match char:
                case ".":
                    grid.add((r, c))
                case "#":
                    walls.add((r, c))
                case "S":
                    start = (r, c)
                    grid.add((r, c))
                case "E":
                    end = (r, c)
                    grid.add((r, c))
    return start, end, grid, walls


def path(start, end, grid, walls):
    path = [start]
    while path[-1] != end:
        # only a single path exists ...
        c, r = path[-1]
        n = [
            (c + dr, r + dc)
            for dr, dc in DIRECTIONS
            if (c + dr, r + dc) in grid and (c + dr, r + dc) not in path
        ]
        assert len(n) == 1, f"Multiple paths from {path[-1]}: {n}"
        path.append(n[0])
    return path


def find_shortcuts(path, walls):
    traversed = set(path)
    shortcuts = {}
    for r, c in walls:
        neighbours = (
            (r + dr, c + dc) for dr, dc in DIRECTIONS if (r + dr, c + dc) in traversed
        )
        for n1, n2 in combinations(neighbours, 2):
            if abs(n1[0] - n2[0]) == 2 or abs(n1[1] - n2[1]) == 2:
                shortcuts[(r, c)] = (n1, n2)
    return shortcuts


def part1(start, end, grid, walls, threshold=100):
    p = path(start, end, grid, walls)
    shortcuts = find_shortcuts(p, walls)
    savings = [abs(p.index(s1) - p.index(s2)) - 2 for s1, s2 in shortcuts.values()]
    return [s for s in savings if s >= threshold]


def offsets(max_dist=20):
    """Generate a set of offsets for points to consider, within a maximum manhattan distance"""
    dist_gen = (
        (r, c)
        for r in range(0, max_dist + 1)
        for c in range(0, max_dist + 1)
        if 0 < (r + c) <= max_dist
    )
    return {
        (s1 * r, s2 * c)
        for r, c in dist_gen
        for s1, s2 in [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    }


def saved_distances(start, end, grid, walls):
    race_path = path(start, end, grid, walls)
    idx = {p: i for i, p in enumerate(race_path)}  # quick lookup for path index
    o = offsets()  # all offsets within a manhattan distance of 20
    # effective savings: distance saved from (p2 - p) - (cost of moving from p to p2)
    return {
        (p, p2): (idx[p2] - idx[p]) - manhattan_distance(p, p2)
        for i, p in enumerate(race_path)
        for p2 in (
            (p[0] + dr, p[1] + dc)
            for dr, dc in o
            if (p[0] + dr, p[1] + dc) in grid and idx[(p[0] + dr, p[1] + dc)] > i
        )
    }


def part2(start, end, grid, walls, threshold=100):
    """
    Now, we're allowed up to 20 ps of cheat time - all walls disappear.
    So the question is what the largest shortcut will be from a given node along the path
    in 20 ps, e.g. the manhattan distance between the nodes can be at most 20.
    """
    savings = Counter(saved_distances(start, end, grid, walls).values())
    return sum(v for k, v in savings.items() if k >= threshold)


if __name__ == "__main__":
    start, end, grid, walls = read_data("day20.txt")
    print(f"Part 1: {len(part1(start, end, grid, walls))}")
    print(f"Part 2: {part2(start, end, grid, walls)}")
