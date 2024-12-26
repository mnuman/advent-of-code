import file_utils as f
from queue import Queue

DIRECTION_OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_data(fname: str):
    data = [[int(c) for c in line] for line in f.read_file(fname)]
    return data


def get_neighbours(row, col, grid):
    neighbours = []
    for dr, dc in DIRECTION_OFFSETS:
        new_row, new_col = row + dr, col + dc
        if (
            0 <= new_row < len(grid)
            and 0 <= new_col < len(grid[0])
            and grid[new_row][new_col] == grid[row][col] + 1
        ):
            neighbours.append((new_row, new_col))
    return neighbours


def part1(data):
    paths = Queue()
    result = set()
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == 0:
                paths.put([(r, c)])
    while not paths.empty():
        current_path = paths.get()
        r, c = current_path[-1]
        for next_r, next_c in get_neighbours(r, c, data):
            if data[next_r][next_c] == 9:
                result.add((current_path[0], (next_r, next_c)))
            else:
                paths.put(current_path + [(next_r, next_c)])
    return len(result)


def part2(data):
    paths = Queue()
    result = set()
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == 0:
                paths.put([(r, c)])
    while not paths.empty():
        current_path = paths.get()
        r, c = current_path[-1]
        for next_r, next_c in get_neighbours(r, c, data):
            new_path = current_path + [(next_r, next_c)]
            if data[next_r][next_c] == 9:
                result.add(tuple(new_path))
            else:
                paths.put(new_path)
    return len(result)


if __name__ == "__main__":
    data = read_data("day10.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
