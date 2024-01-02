"""
"""
import file_utils as u
import networkx as nx


def in_grid_neighbours(grid, row, col):
    return [
        (row + dr, col + dc)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if (row + dr, col + dc) in grid and grid[(row + dr, col + dc)] != "#"
    ]


def build_graph(grid):
    g = nx.DiGraph()
    for srow, scol in (k for k in grid.keys() if grid[k] != "#"):
        for trow, tcol in in_grid_neighbours(grid, srow, scol):
            src, target = grid[(srow,scol)], grid[(trow,tcol)]
            if src == ">" and target == "." and srow == trow and scol = tcol





def part1(fname: str) -> int:
    grid = {
        (row, col): char
        for row, line in enumerate(u.read_file(fname))
        for col, char in enumerate(line)
    }


def part2(fname: str) -> int:
    return 2


if __name__ == "__main__":
    print(f"Results part1: {part1('day23.txt')}")
    print(f"Results part2: {part2('day23.txt')}")
