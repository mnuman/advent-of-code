import day11a
import utils


def test_check_cell():
    grid = ["###", "...", "###"]
    assert day11a.check_cell(grid, 0, 0) == 1
    assert day11a.check_cell(grid, 3, 3) == 0
    assert day11a.check_cell(grid, 1, 1) == 0


def test_count_neighbours():
    grid = ["###", "...", "###"]
    assert day11a.count_neighbours(grid, 0, 0) == 1
    assert day11a.count_neighbours(grid, 0, 1) == 2
    assert day11a.count_neighbours(grid, 0, 2) == 1
    assert day11a.count_neighbours(grid, 1, 1) == 6
    assert day11a.count_neighbours(grid, 1, 2) == 4


def test_next_state_1():
    """    012
         0 ###      #L#
         1 #.#  --> L.L
         2 ###      #L#
    """
    almost_full_grid = ["###", "#.#", "###"]
    assert day11a.next_state(almost_full_grid, 0, 0) == day11a.STATE_OCCUPIED
    assert day11a.next_state(almost_full_grid, 0, 1) == day11a.STATE_EMPTY
    assert day11a.next_state(almost_full_grid, 1, 0) == day11a.STATE_EMPTY
    assert day11a.next_state(almost_full_grid, 1, 1) == day11a.STATE_FLOOR


def test_next_state_steady_state():
    """    012
         0 #L#      #L#
         1 L.L  --> L.L
         2 #L#      #L#
    """
    almost_full_grid = ["#L#", "L.L", "#L#"]
    assert day11a.next_state(almost_full_grid, 0, 0) == day11a.STATE_OCCUPIED
    assert day11a.next_state(almost_full_grid, 0, 1) == day11a.STATE_EMPTY
    assert day11a.next_state(almost_full_grid, 1, 0) == day11a.STATE_EMPTY
    assert day11a.next_state(almost_full_grid, 1, 1) == day11a.STATE_FLOOR


def test_next_grid_steady_state():
    current_state = ["#L#", "L.L", "#L#"]
    next_state = day11a.next_grid(current_state)
    assert len(next_state) == 3
    assert len(next_state[0]) == len(next_state[1]) == len(next_state[2])
    assert current_state[0] == next_state[0]
    assert current_state[1] == next_state[1]
    assert current_state[2] == next_state[2]


def test_next_grid_state():
    """    012
         0 ###      #L#
         1 #.#  --> L.L
         2 ###      #L#
    """
    current_state = ["###", "#.#", "###"]
    next_state = day11a.next_grid(current_state)
    assert len(next_state) == 3
    assert len(next_state[0]) == len(next_state[1]) == len(next_state[2])
    assert next_state[0] == "#L#"
    assert next_state[1] == "L.L"
    assert next_state[2] == "#L#"


def test_iterate_until_steady_state():
    current_state = utils.read_file("data/test_day11.txt")
    steady_state = ["#.#L.L#.##",
                    "#LLL#LL.L#",
                    "L.#.L..#..",
                    "#L##.##.L#",
                    "#.#L.LL.LL",
                    "#.#L#L#.##",
                    "..L.L.....",
                    "#L#L##L#L#",
                    "#.LLLLLL.L",
                    "#.#L#L#.##"
                    ]
    new_state = day11a.iterate_until_steady_state(current_state)
    assert all(new_state[i] == steady_state[i]
               for i in range(0, len(steady_state)))


def test_occupied_seats():
    steady_state = ["#.#L.L#.##",
                    "#LLL#LL.L#",
                    "L.#.L..#..",
                    "#L##.##.L#",
                    "#.#L.LL.LL",
                    "#.#L#L#.##",
                    "..L.L.....",
                    "#L#L##L#L#",
                    "#.LLLLLL.L",
                    "#.#L#L#.##"
                    ]
    assert day11a.occupied_seats(steady_state) == 37
