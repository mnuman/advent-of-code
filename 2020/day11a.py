"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey
is a ferry that goes directly to the tropical island where you can finally
start your vacation. As you reach the waiting area to board the ferry,
you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You
make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.),
an empty seat (L), or an occupied seat (#). For example, the initial seat
layout might look like this:

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

Now, you just need to model the people who will be arriving shortly.
Fortunately, people are entirely predictable and always follow a simple set
of rules. All decisions are based on the number of occupied seats adjacent to
a given seat (one of the eight positions immediately up, down, left, right,
or diagonal from the seat). The following rules are applied to every seat
simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it,
    the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also
    occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes
occupied:

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

After a second round, the seats with four or more occupied adjacent seats
become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and
further applications of these rules cause no seats to change state! Once
people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?

"""
import utils

STATE_OCCUPIED = '#'
STATE_FLOOR = '.'
STATE_EMPTY = 'L'


def check_cell(current_grid, r, c):
    # check if cell within bounds, return 1 if cell is occupied else 0
    if 0 <= r < len(current_grid) and 0 <= c < len(current_grid[0]):
        return 1 if current_grid[r][c] == STATE_OCCUPIED else 0
    else:
        return 0


def count_neighbours(current_grid, row, col):
    # check adjacent cells for neighbours; offset 0,0 is the current cell itself
    neighbours = 0
    for row_offset in (-1, 0, 1):
        for col_offset in (-1, 0, 1):
            if not (row_offset == 0 and col_offset == 0):
                neighbours += check_cell(current_grid, row + row_offset,
                                         col + col_offset)
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
        if count_neighbours(current_grid, row, col) >= 4:
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
