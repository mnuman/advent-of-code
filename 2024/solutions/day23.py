import file_utils as f
from collections import defaultdict
from itertools import combinations


def read_data(fname: str):
    return [tuple(line.split("-")) for line in f.read_file(fname)]


def parse_data(data):
    connections = defaultdict(set)
    for c1, c2 in data:
        connections[c1].add(c2)  # other machine
        connections[c2].add(c1)
    return connections


def t_gen(computers):
    """
    Return the nodes where at least one of the nodes **STARTS** with the letter "t" - hence the [::2] slice.
    """
    return (
        (c1, c2, c3)
        for c1, c2, c3 in combinations(computers, 3)
        if "t" in (c1 + c2 + c3)[::2]
    )


"""
In graph theory, a clique is a subset of vertices of an undirected graph such
that every two distinct vertices in the clique are adjacent.
"""


def is_clique(connections, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[j] not in connections[nodes[i]]:
                return False
    return True


"""
https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
"""


def find_max_clique(connections):
    max_clique = []
    nodes = list(connections.keys())

    def backtrack(clique, start):
        nonlocal max_clique
        if len(clique) > len(max_clique):
            max_clique = clique[:]
        for i in range(start, len(nodes)):
            if all(nodes[i] in connections[node] for node in clique):
                clique.append(nodes[i])
                backtrack(clique, i + 1)
                clique.pop()

    backtrack([], 0)
    return max_clique


def part1(data):
    connections = parse_data(data)
    return len(
        {
            (c1, c2, c3)
            for c1, c2, c3 in t_gen(connections.keys())
            if c1 in connections[c2] and c2 in connections[c3] and c3 in connections[c1]
        }
    )


def part2(data):
    connections = parse_data(data)
    max_clique = find_max_clique(connections)
    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    data = read_data("day23.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
