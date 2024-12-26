import file_utils as f
from functools import cache

"""
Cannot solve this one right now. My first implementation was incorrect for the last code. Reset brain.

Observations:
- after every input code, the arm moves to the "A" position again as this is the last action (button press).
- setup:
  NUM > DIR#1 > DIR#2 > DIR#3
- start encoding from the left
- every character that is sent from the numeric_keypad also makes the next keypad move to "A" after encoding
- for the numeric_keypad: right before down, up before left to avoid the gap
- for the directional_keypad: right before up, down before left to avoid the gap
"""
NUMBER_COORDS = {
    char: (r, c)
    for r, row in enumerate(["789", "456", "123", "X0A"])
    for c, char in enumerate(row)
}
del NUMBER_COORDS["X"]
COORDS_NUMBER = {v: k for k, v in NUMBER_COORDS.items()}

DIRECTION_COORDS = {
    char: (r, c) for r, row in enumerate(["X^A", "<v>"]) for c, char in enumerate(row)
}
del DIRECTION_COORDS["X"]
COORDS_DIRECTION = {v: k for k, v in DIRECTION_COORDS.items()}


def code_value(code: str):
    """Extract the numerical value from the code string"""
    return int("".join(c for c in code if c.isdigit()))


@cache
def move(key, next_key, numeric):
    if key == next_key:
        return "A"

    key_coord, coord_key = (
        (NUMBER_COORDS, COORDS_NUMBER)
        if numeric
        else (DIRECTION_COORDS, COORDS_DIRECTION)
    )
    start_row, start_col = key_coord[key]
    next_row, next_col = key_coord[next_key]
    d_cols, d_rows = next_col - start_col, next_row - start_row

    move_cols = ">" * d_cols if d_cols >= 0 else "<" * -d_cols
    move_rows = "v" * d_rows if d_rows >= 0 else "^" * -d_rows

    # only linear movement ... no turns, so no alternatives
    if d_cols == 0:
        return move_rows + "A"
    elif d_rows == 0:
        return move_cols + "A"

    result = []
    # consider both paths with a single turn if possible
    if (start_row, next_col) in coord_key:
        result.append(move_cols + move_rows + "A")
    if (next_row, start_col) in coord_key:
        result.append(move_rows + move_cols + "A")

    if len(result) != 2 or d_cols < 0:
        result = result[0]  # paths with left movement are slower (< is farthest from A)
    else:
        result = result[1]

    return result


@cache
def get_path_length(path, level, numeric):
    if level == 0:
        return len(path)  # we're done!

    path = "A" + path  # start at "A"
    total = 0
    for key, next_key in zip(path, path[1:]):
        total += get_path_length(
            move(key, next_key, numeric),
            level - 1,
            False,  # only on upper level we use the numeric keypad!
        )
    return total


def read_data(fname: str):
    return f.read_file(fname)


def part1(data):
    return sum(code_value(code) * get_path_length(code, 2 + 1, True) for code in data)


def part2(data):
    return sum(code_value(code) * get_path_length(code, 25 + 1, True) for code in data)


if __name__ == "__main__":
    data = read_data("day21.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
