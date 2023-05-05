"""
As soon as people start to arrive, you realize your mistake. People don't
just care about adjacent seats - they care about the first seat they can see
in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats,
consider the first seat in each of those eight directions. For example,
the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see
any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or
more visible occupied seats for an occupied seat to become empty (rather than
four or more from the previous rules). The other rules still apply: empty
seats that see no occupied seats become occupied, seats matching no rule
don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating
area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area
reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats
becoming empty, once equilibrium is reached, how many seats end up occupied?
"""
import utils

STATE_OCCUPIED = '#'
STATE_FLOOR = '.'
STATE_EMPTY = 'L'


def check_cells(current_grid, r, c, dr, dc):
    # from the cell at r,c check the direction dr, dc and return 0 if the
    # first visible seat is empty, otherwise return 1
    result = 0
    check_row, check_col = r + dr, c + dc
    no_seat_found = True
    while 0 <= check_row < len(current_grid) and \
            0 <= check_col < len(current_grid[0]) and no_seat_found:
        if current_grid[check_row][check_col] == STATE_OCCUPIED:
            result = 1
            no_seat_found = False
        elif current_grid[check_row][check_col] == STATE_EMPTY:
            result = 0
            no_seat_found = False
        check_row += dr
        check_col += dc
    return result


def count_neighbours(current_grid, row, col):
    # check adjacent cells for neighbours; offset 0,0 is the current cell itself
    neighbours = 0
    for row_offset in (-1, 0, 1):
        for col_offset in (-1, 0, 1):
            if not (row_offset == 0 and col_offset == 0):
                print(
                    f"Row,col:{row},{col} - direction {row_offset},"
                    f"{col_offset}")
                neighbours += check_cells(current_grid, row, col, row_offset,
                                          col_offset)
    return neighbours


def next_state(current_grid, row, col):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also
    occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    if current_grid[row][col] == STATE_FLOOR:
        return STATE_FLOOR
    elif current_grid[row][col] == STATE_OCCUPIED:
        if count_neighbours(current_grid, row, col) >= 5:
            return STATE_EMPTY
        else:
            return STATE_OCCUPIED
    else:
        if count_neighbours(current_grid, row, col) == 0:
            return STATE_OCCUPIED
        else:
            return STATE_EMPTY


def next_grid(current_grid):
    """Calculate the entire next grid by applying the rules on the current
       grid layout
    """
    result = []
    for r in range(0, len(current_grid)):
        new_row = ''.join([next_state(current_grid, r, c)
                           for c in range(0, len(current_grid[r]))])
        result.append(new_row)
    return result


def iterate_until_steady_state(current_layout):
    iteration = 0
    continue_iteration = True
    next_layout = current_layout[:]
    while continue_iteration:
        iteration += 1
        current_layout = next_layout[:]
        next_layout = next_grid(current_layout)
        continue_iteration = not all(next_layout[i] == current_layout[i]
                                     for i in range(0, len(current_layout)))
        print(f"Completed iteration {iteration}")
    return next_layout


def occupied_seats(layout):
    cnt = 0
    for row in layout:
        for col in row:
            cnt += 1 if col == STATE_OCCUPIED else 0
    return cnt


if __name__ == "__main__":
    current_state = utils.read_file("data/day11.txt")
    new_state = iterate_until_steady_state(current_state)
    print(f"Completed! Number of occupied seats {occupied_seats(new_state)}")
