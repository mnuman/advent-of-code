import file_utils as f
import heapq

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


class Node:
    def __init__(self, position, dir_index, cost):
        self.cost = cost
        self.position = position
        self.dir_index = dir_index

    def __repr__(self):
        return f"({self.position}, {self.dir_index}), cost={self.cost}"

    # by implementing this method, we can use heapq without further ado
    # as we can now compare two objects!
    def __lt__(self, other):
        return self.cost < other.cost

    def neighbours(self):
        n1 = Node(self.position, (self.dir_index + 1) % 4, self.cost + 1000)
        n2 = Node(self.position, (self.dir_index + 3) % 4, self.cost + 1000)
        position_ = (
            self.position[0] + DIRECTIONS[self.dir_index][0],
            self.position[1] + DIRECTIONS[self.dir_index][1],
        )
        n3 = Node(position_, self.dir_index, self.cost + 1)
        return [n1, n2, n3]


def parse_data_from_file(fname: str):
    start, end, grid = None, None, set()
    for r, row in enumerate(f.read_file(fname)):
        for c, cell in enumerate(row):
            match cell:
                case "#":
                    continue  # wall - ignore
                case "S":
                    start = (r, c)
                    grid.add((r, c))
                case "E":
                    end = (r, c)
                    grid.add((r, c))
                case _:
                    grid.add((r, c))
    assert start is not None and end is not None, "Must have a start and end!"
    return start, end, grid


def dijkstra(start, end, grid):
    _MEMO = {(start, 0): 0}  # cost accounting
    _prev = {(start, 0): []}  # path accounting
    nodes_to_consider = [Node(start, 0, 0)]
    while nodes_to_consider:
        candidate = heapq.heappop(nodes_to_consider)
        if candidate.position == end:
            break
        for neighbour in candidate.neighbours():
            if neighbour.position not in grid:
                continue
            b = _MEMO.get((neighbour.position, neighbour.dir_index), float("inf"))
            if b < neighbour.cost:  # new path is more expensive
                continue
            if b > neighbour.cost:  # better new path
                heapq.heappush(nodes_to_consider, neighbour)
                _MEMO[(neighbour.position, neighbour.dir_index)] = neighbour.cost
                # If we found a better path, reset the prev
                _prev[(neighbour.position, neighbour.dir_index)] = []
            _prev[(neighbour.position, neighbour.dir_index)].append(
                (candidate.position, candidate.dir_index)
            )
    best_nodes = set([(candidate.position, candidate.dir_index)])
    while (start, 0) not in best_nodes:
        best_backtrack = set()
        for n in best_nodes:
            best_backtrack |= set(_prev[n])
        best_nodes |= best_backtrack

    unique_positions_along_path = set(position for position, direction in best_nodes)
    return candidate.cost, len(unique_positions_along_path)


if __name__ == "__main__":
    s, e, g = parse_data_from_file("day16.txt")
    min_cost, count_nodes = dijkstra(s, e, g)
    print(f"Part 1: {min_cost}")
    print(f"Part 1: {count_nodes}")
