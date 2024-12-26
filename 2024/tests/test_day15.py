import day15


def test_read_data():
    grid, moves = day15.read_data("test_day15.txt")
    assert len(grid) == len(grid[0]) == 10, "Incorrect grid size"
    assert len(moves) == 700, "Incorrect number of moves"


def test_part1():
    grid, moves = day15.read_data("test_day15.txt")
    assert day15.part1(grid, moves) == 10092


def test_part2():
    grid, moves = day15.read_data("test_day15.txt")
    assert day15.part2(grid, moves) == 9021
