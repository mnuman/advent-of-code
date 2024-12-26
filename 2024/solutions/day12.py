from collections import defaultdict
import file_utils as f

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def read_data(fname: str):
    return [[char for char in line] for line in f.read_file(fname)]


def find_symbols(data):
    symbols = defaultdict(set)
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            symbols[char].add((r, c))
    return symbols


def find_regions(symbols):
    all_regions = defaultdict(list)
    for k in symbols:
        positions = symbols[k]
        while positions:
            r, c = positions.pop()
            region = {(r, c)}
            expand_region(r, c, positions, region)
            all_regions[k].append(region)
    return all_regions


def expand_region(r, c, positions, region):
    for dr, dc in DIRECTIONS:
        new_r = r + dr
        new_c = c + dc
        if (new_r, new_c) in positions:
            positions.remove((new_r, new_c))
            region.add((new_r, new_c))
            expand_region(new_r, new_c, positions, region)


def determine_perimeter(region, data):
    perimeter = 0
    for r, c in region:
        for dr, dc in DIRECTIONS:
            new_r = r + dr
            new_c = c + dc
            # need to consider the case where the region is on the edge of the grid
            if (
                -1 <= new_r <= len(data)
                and -1 <= new_c <= len(data[0])
                and (new_r, new_c) not in region
            ):
                perimeter += 1
    return perimeter


def count_sides(region):
    """The number of sides is the number of corners of the region.
    Outside corners are:
      O      O
    O X  or  X O  or  X O  or O X
                      O         O

    Inside corners are:
     O X       X O
     X X  or   X X  or  X X   or  X  X
                        X O       O  X
    """
    sides = 0
    for r, c in region:
        for idx in range(4):
            dr1, dc1 = DIRECTIONS[idx]
            dr2, dc2 = DIRECTIONS[(idx + 1) % 4]
            new_1 = (r + dr1, c + dc1)
            new_2 = (r + dr2, c + dc2)
            if new_1 not in region and new_2 not in region:
                sides += 1
        for dr1, dc1, dr2, dc2, dr3, dc3 in [
            (0, 1, 1, 0, 1, 1),  # straight, straight, diagonal
            (0, -1, 1, 0, 1, -1),
            (0, -1, -1, 0, -1, -1),
            (-1, 0, 0, 1, -1, 1),
        ]:
            straight_1 = (r + dr1, c + dc1)
            straight_2 = (r + dr2, c + dc2)
            diagonal = (r + dr3, c + dc3)
            if straight_1 in region and straight_2 in region and diagonal not in region:
                sides += 1

    return sides


def part1(data):
    symbols = find_symbols(data)
    regions = find_regions(symbols)
    result = 0
    for symbol in regions:
        for region in regions[symbol]:
            area = len(region)
            perimeter = determine_perimeter(region, data)
            result += area * perimeter
    return result


def part2(data):
    symbols = find_symbols(data)
    regions = find_regions(symbols)
    result = 0
    for symbol in regions:
        for region in regions[symbol]:
            area = len(region)
            sides = count_sides(region)
            result += area * sides
    return result


if __name__ == "__main__":
    data = read_data("day12.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
