"""
--- Day 17: Conway Cubes ---

As your flight slowly drifts through the sky, the Elves at the Mythical
Information Bureau at the North Pole contact you. They'd like some help
debugging a malfunctioning experimental energy source aboard one of their
super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of
Conway Cubes contained in a pocket dimension! When you hear it's having
problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every
integer 3-dimensional coordinate (x,y,z), there exists a single cube which is
either active or inactive.

In the initial state of the pocket dimension, almost all cubes start
inactive. The only exception to this is a small flat region of cubes (your
puzzle input); the cubes in this region start in the specified active (#) or
inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where
any of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,
y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the
following rules:

    If a cube is active and exactly 2 or 3 of its neighbors are also active,
    the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube
    becomes active. Otherwise, the cube remains inactive.

The engineers responsible for this experimental energy source would like you
to simulate the pocket dimension and determine what the configuration of
cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###

Even though the pocket dimension is 3-dimensional, this initial state
represents a small 2-dimensional slice of it. (In particular, this initial
state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following
configurations, where the result of each cycle is shown layer-by-layer at
each given z coordinate (and the frame of view follows the active cells in
each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......

After the full six-cycle boot process completes, 112 cubes are left in the
active state.

Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?
"""
import itertools

import utils

ACTIVE_STATE = "#"
INACTIVE_STATE = "."


def read_initial_state(filename):
    current_state = {}
    lines = utils.read_file(filename)
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            current_state[(x, y, 0)] = val
    return current_state


def all_neighbours(x, y, z):
    # Generate all neighbours for the given point
    offsets = [*itertools.product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))]
    offsets.remove((0, 0, 0))
    return [(x + offset_x, y + offset_y, z + offset_z) for
            offset_x, offset_y, offset_z in offsets]


def get_current_cell_state(current_state, x, y, z):
    # if the point does not yet exist it is inactive
    return current_state[(x, y, z)] \
        if (x, y, z) in current_state else INACTIVE_STATE


def expand_calculation_boundaries(current_state):
    all_x = [x for x, y, z in [k for k in current_state]]
    all_y = [y for x, y, z in [k for k in current_state]]
    all_z = [z for x, y, z in [k for k in current_state]]
    return (min(all_x) - 1, max(all_x) + 1), (min(all_y) - 1, max(all_y) + 1), \
           (min(all_z) - 1, max(all_z) + 1)


def next_cell_state(current_state, x, y, z):
    active_neighbours = sum(
        [1 if get_current_cell_state(current_state, *n) == ACTIVE_STATE else 0
         for n in all_neighbours(x, y, z)])
    calculated_state = ACTIVE_STATE \
        if (get_current_cell_state(current_state, x, y, z) == ACTIVE_STATE and
            active_neighbours in (2, 3)) or \
           (get_current_cell_state(current_state, x, y, z) == INACTIVE_STATE and
            active_neighbours == 3) else INACTIVE_STATE
    return calculated_state


def calculate_next_state(current_state):
    (xmin, xmax), (ymin, ymax), (zmin, zmax) = \
        expand_calculation_boundaries(current_state)
    next_state = {}
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                new_cell_state = next_cell_state(current_state, x, y, z)
                if new_cell_state == ACTIVE_STATE:
                    next_state[(x, y, z)] = ACTIVE_STATE
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
    print(f"Active cubes after 6 cycles: {cycle(inital_state)}")
