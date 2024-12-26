import file_utils as f
import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_data(fname: str):
    return list(tuple(map(int, e.split(","))) for e in f.read_file(fname))


class Node:
    def __init__(self, position, cost):
        self.cost = cost
        self.position = position

    def __repr__(self):
        return f"({self.position}, cost={self.cost}"

    # by implementing this method, we can use heapq without further ado
    # as we can now compare two objects!
    def __lt__(self, other):
        return self.cost < other.cost

    def neighbours(self):
        for dr, dc in DIRECTIONS:
            r, c = self.position
            r += dr
            c += dc
            yield Node((r, c), self.cost + 1)


def part1(data, bytes=1024, max_coord=70):
    start = (0, 0)
    end = (max_coord, max_coord)
    blocked = set(data[:bytes])
    grid = set(
        (r, c)
        for r in range(max_coord + 1)
        for c in range(max_coord + 1)
        if (r, c) not in blocked
    )
    return dijkstra(start, end, grid)


def dijkstra(start, end, grid):
    _MEMO = {(start, 0): 0}  # cost accounting
    _prev = {(start, 0): []}  # path accounting
    nodes_to_consider = [Node(start, 0)]
    while nodes_to_consider:
        candidate = heapq.heappop(nodes_to_consider)
        if candidate.position == end:
            break
        for neighbour in candidate.neighbours():
            if neighbour.position not in grid:
                continue
            b = _MEMO.get(neighbour.position, float("inf"))
            if b < neighbour.cost:  # new path is more expensive
                continue
            if b > neighbour.cost:  # better new path
                heapq.heappush(nodes_to_consider, neighbour)
                _MEMO[neighbour.position] = neighbour.cost
                # If we found a better path, reset the prev
                _prev[neighbour.position] = []
            _prev[neighbour.position].append(candidate.position)
    return candidate.cost if candidate.position == end else -1


def part2(data, bytes=2048, max_coord=70):
    start = (0, 0)
    end = (max_coord, max_coord)
    i = bytes
    while i < len(data):
        grid = set(
            (r, c)
            for r in range(max_coord + 1)
            for c in range(max_coord + 1)
            if (r, c) not in set(data[: i + 1])
        )
        if dijkstra(start, end, grid) == -1:
            return data[i]
        i += 1
    return -1


if __name__ == "__main__":
    data = read_data("day18.txt")
    print(f"Part 1: {part1(data)}")
    # print(f"Part 2: {part2(data)}")
    # determined iteratively using binary search from i = 1024 - len(data) that
    # bytes=2990 is the first value to block the path. Hence, the answer is data[2990-1]
    print(f"Part 2: {part1(data, bytes=2990)}")
    print(f"Part 2: {data[2989]}")
