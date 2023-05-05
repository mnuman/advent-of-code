import day11b

STATE = [".......#.",
         "...#.....",
         ".#.......",
         ".........",
         "..#L....#",
         "....#....",
         ".........",
         "#........",
         "...#....."]


def test_check_cells_all_occupied():
    # from the empty seat at row = 4, col = 3 all eight directions see an
    # occupied seat first.
    assert day11b.check_cells(STATE, 4, 3, 0, 1) == 1
    assert day11b.check_cells(STATE, 4, 3, 1, 0) == 1
    assert day11b.check_cells(STATE, 4, 3, -1, 0) == 1
    assert day11b.check_cells(STATE, 4, 3, 0, -1) == 1
    assert day11b.check_cells(STATE, 4, 3, 1, 1) == 1
    assert day11b.check_cells(STATE, 4, 3, 1, -1) == 1
    assert day11b.check_cells(STATE, 4, 3, -1, 1) == 1
    assert day11b.check_cells(STATE, 4, 3, -1, -1) == 1


def test_not_occupied():
    assert day11b.check_cells(STATE, 4, 2, 0, 1) == 0
    assert day11b.check_cells(STATE, 1, 3, 1, 0) == 0
    assert day11b.check_cells(STATE, 8, 3, -1, 0) == 0
