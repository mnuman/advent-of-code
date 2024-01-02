"""
"""
import file_utils as u
from heapq import heappush, heappop


def dijkstra(g, min_steps, max_steps):
    assert len(g) == len(g[0]), "Non-square grid!"
    pq = []
    dim = len(g)
    visited = set()
    # push starting point to priority queue
    heappush(pq, (0, 0, 0, 0, 0, 0))

    while len(pq) > 0:
        cost, row, col, drow, dcol, steps = heappop(pq)
        if (row, col, drow, dcol, steps) not in visited:
            if row == dim - 1 and col == dim - 1 and steps >= min_steps:
                return cost  # arrived!

            visited.add((row, col, drow, dcol, steps))

            # consider all possible steps from current position
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if dr + drow == 0 and dc + dcol == 0:
                    continue  # reverse last not allowed

                # ultra crucible: at start, all moves allowed
                # then all moves allowed if in same direction or more than min_steps
                if (
                    (row, col) == (0, 0)
                    or steps >= min_steps
                    or (dr, dc) == (drow, dcol)
                ):
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < dim and 0 <= new_col < dim:
                        new_cost = cost + g[new_row][new_col]
                        if dr == drow and dc == dcol:
                            if steps < max_steps:
                                heappush(
                                    pq,
                                    (new_cost, new_row, new_col, dr, dc, steps + 1),
                                )
                        else:
                            heappush(pq, (new_cost, new_row, new_col, dr, dc, 1))


def part1(fname: str):
    grid = [[int(c) for c in line] for line in u.read_file(fname)]
    result = dijkstra(grid, 0, 3)
    return result


def part2(fname: str):
    grid = [[int(c) for c in line] for line in u.read_file(fname)]
    result = dijkstra(grid, 4, 10)
    return result


if __name__ == "__main__":
    print(f"Result for part1 : {part1('day17.txt')}")
    print(f"Result for part2 : {part2('day17.txt')}")
