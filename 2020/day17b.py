"""
--- Part Two ---

For some reason, your simulated results don't match what the experimental
energy source engineers expected. Apparently, the pocket dimension actually
has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every
integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (
really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where
any of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube
at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat
region of cubes. Furthermore, the same rules for cycle updating still apply:
during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even
though the pocket dimension is 4-dimensional, this initial state represents a
small 2-dimensional slice of it. (In particular, this initial state defines a
3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following
configurations, where the result of each cycle is shown layer-by-layer at
each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....

After the full six-cycle boot process completes, 848 cubes are left in the
active state.

Starting with your given initial configuration, simulate six cycles in a
4-dimensional space. How many cubes are left in the active state after the
sixth cycle?
"""
import itertools

import utils

ACTIVE_STATE = "#"
INACTIVE_STATE = "."


# Basically, this is extrapolation into four dimensions for all functions


def read_initial_state(filename):
    current_state = {}
    lines = utils.read_file(filename)
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            current_state[(x, y, 0, 0)] = val
    return current_state


def all_neighbours(x, y, z, w):
    # Generate all neighbours for the given point - except the point itself
    offsets = [
        *itertools.product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1), (-1, 0, 1))]
    offsets.remove((0, 0, 0, 0))
    return [(x + offset_x, y + offset_y, z + offset_z, w + offset_w) for
            offset_x, offset_y, offset_z, offset_w in offsets]


def get_current_cell_state(current_state, x, y, z, w):
    # if the point does not yet exist it is inactive
    return current_state[(x, y, z, w)] \
        if (x, y, z, w) in current_state else INACTIVE_STATE


def expand_calculation_boundaries(current_state):
    all_x = [x for x, y, z, w in [k for k in current_state]]
    all_y = [y for x, y, z, w in [k for k in current_state]]
    all_z = [z for x, y, z, w in [k for k in current_state]]
    all_w = [w for x, y, z, w in [k for k in current_state]]
    return (min(all_x) - 1, max(all_x) + 1), (min(all_y) - 1, max(all_y) + 1), \
           (min(all_z) - 1, max(all_z) + 1), (min(all_w) - 1, max(all_w) + 1)


def next_cell_state(current_state, x, y, z, w):
    active_neighbours = sum(
        [1 if get_current_cell_state(current_state, *n) == ACTIVE_STATE else 0
         for n in all_neighbours(x, y, z, w)])
    calculated_state = ACTIVE_STATE \
        if (get_current_cell_state(current_state, x, y, z,
                                   w) == ACTIVE_STATE and
            active_neighbours in (2, 3)) or \
           (get_current_cell_state(current_state, x, y, z,
                                   w) == INACTIVE_STATE and
            active_neighbours == 3) else INACTIVE_STATE
    return calculated_state


def calculate_next_state(current_state):
    (xmin, xmax), (ymin, ymax), (zmin, zmax), (wmin, wmax) = \
        expand_calculation_boundaries(current_state)
    next_state = {}
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                for w in range(wmin, wmax + 1):
                    new_cell_state = next_cell_state(current_state, x, y, z, w)
                    if new_cell_state == ACTIVE_STATE:
                        next_state[(x, y, z, w)] = ACTIVE_STATE
    return next_state


def cycle(state, num_cycles=6):
    cycle = 1
    current_state = state
    while cycle <= 6:
        new_state = calculate_next_state(current_state)
        cycle += 1
        current_state = new_state
    return len(current_state)


if __name__ == "__main__":
    inital_state = read_initial_state("data/day17.txt")
    print(
        f"Active hyperdimensional cubes after 6 cycles: {cycle(inital_state)}")
