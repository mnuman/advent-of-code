fname = "./data/day04.txt"
# all possible directions to complete
search_directions = [
    (0, 1),  # right
    (0, -1),  # left
    (-1, 0),  # up
    (1, 0),  # down
    (-1, -1),  # left + up
    (-1, 1),  # left + down
    (1, 1),  # right + down
    (1, -1),  # right + up
]


def candidates_gen(x_pos, rows, cols):
    for d in search_directions:
        if 0 <= x_pos[0] + 3 * d[0] < cols and 0 <= x_pos[1] + 3 * d[1] < rows:
            yield [(x_pos[0] + i * d[0], x_pos[1] + i * d[1]) for i in range(4)]


def x_candidates(a_pos, rows, cols):
    diagonals = [(1, 1), (1, -1)]
    x_points = [
        ((a_pos[0] - d[0], a_pos[1] - d[1]), (a_pos[0] + d[0], a_pos[1] + d[1]))
        for d in diagonals
        if 0 <= a_pos[0] - d[0] < rows
        and 0 <= a_pos[1] - d[1] < cols
        and 0 <= a_pos[0] + d[0] < rows
        and 0 <= a_pos[1] + d[1] < cols
    ]
    return x_points


def part1(data, grid_rows, grid_cols):
    x_locations = [
        (row, col)
        for row, line in enumerate(data)
        for col, char in enumerate(line)
        if char == "X"
    ]
    xmas_count = 0
    for x_loc in x_locations:
        for candidate in list(candidates_gen(x_loc, grid_rows, grid_cols)):
            if (
                data[candidate[1][0]][candidate[1][1]] == "M"
                and data[candidate[2][0]][candidate[2][1]] == "A"
                and data[candidate[3][0]][candidate[3][1]] == "S"
            ):
                xmas_count += 1
    print(f"Part1: {xmas_count}")


def part2(data, grid_rows, grid_cols):
    xmas_count = 0
    a_locations = [
        (row, col)
        for row, line in enumerate(data)
        for col, char in enumerate(line)
        if char == "A"
    ]
    for a_loc in a_locations:
        # [((0, 1), (2, 3)), ((0, 3), (2, 1))]
        nb = x_candidates(a_loc, grid_rows, grid_cols)
        if len(nb) > 0:
            diagonal_1 = data[nb[0][0][0]][nb[0][0][1]] + data[nb[0][1][0]][nb[0][1][1]]
            diagonal_2 = data[nb[1][0][0]][nb[1][0][1]] + data[nb[1][1][0]][nb[1][1][1]]
            if diagonal_1 in ("SM", "MS") and diagonal_2 in ("SM", "MS"):
                xmas_count += 1
    print(f"Part2: {xmas_count}")


if __name__ == "__main__":
    data = [list(line.strip()) for line in open(fname).readlines()]
    grid_rows = len(data)
    grid_cols = len(data[0])
    part1(data, grid_rows, grid_cols)
    part2(data, grid_rows, grid_cols)
