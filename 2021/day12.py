from collections import defaultdict, Counter

import utils

visited_paths = [[]]


def readfile(filename):
    data = utils.read_file(filename)
    graph = defaultdict(list)
    for line in data:
        from_vertex, to_vertex = line.split("-")
        graph[from_vertex].append(to_vertex), graph[to_vertex].append(from_vertex)
    return graph


def depth_first_search(graph, current_vertex, visited=None, vertex_validator=None):
    """Modified from https://stackoverflow.com/questions/62656477/python-get-all-paths-from-graph"""
    if visited is None:
        visited = [current_vertex]
    else:
        visited.append(current_vertex)

    for vertex in graph[current_vertex]:
        if vertex_validator(vertex, visited):
            depth_first_search(graph, vertex, visited.copy(), vertex_validator)
    visited_paths.append(visited)


def part1_vertex_validator(current_vertex, visited_vertices):
    """Validates whether the node may be visited for part 1.
       It may not have been visited yet, unless its name is in uppercase"""
    return current_vertex not in visited_vertices or current_vertex == current_vertex.upper()


def part2_vertex_validator(current_vertex, visited_vertices):
    """Validates whether the node may be visited for part 2.
       It may not have been visited yet, unless its name is in uppercase OR it is the first lowercase to be visited
       twice"""
    may_be_visited_twice = True
    if current_vertex == current_vertex.lower():
        cave_counter = Counter()
        for cave in visited_vertices:
            if cave == cave.lower():
                cave_counter[cave] += 1
        may_be_visited_twice = all([v == 1 for v in cave_counter.values()])

    return part1_vertex_validator(current_vertex, visited_vertices) or (
                current_vertex not in ("start", "end") and may_be_visited_twice)


def part1(filename):
    graph = readfile(filename)
    depth_first_search(graph, "start", vertex_validator=part1_vertex_validator)
    return len([path for path in visited_paths if len(path) > 0 and path[-1] == 'end'])


def part2(filename):
    global visited_paths
    visited_paths = [[]]
    graph = readfile(filename)
    depth_first_search(graph, "start", vertex_validator=part2_vertex_validator)
    return len([path for path in visited_paths if len(path) > 0 and path[-1] == 'end'])


if __name__ == '__main__':
    day11_1 = part1("data/day-12.txt")
    print("Day 11 - part 1", day11_1)
    day11_2 = part2("data/day-12.txt")
    print("Day 11 - part 2", day11_2)
