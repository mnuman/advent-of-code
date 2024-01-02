"""
--- Day 14: Parabolic Reflector Dish ---

You reach the place where all of the mirrors were pointing: a massive parabolic
reflector dish attached to the side of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves
are roughly in the shape of a parabolic reflector dish, each individual mirror
seems to be pointing in slightly the wrong direction. If the dish is meant to
focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the
reflector dish, maybe you can go where it's pointing and use the light to
fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an
elaborate system of ropes and pulleys to a large metal platform below the dish.
The platform is covered in large rocks of various shapes. Depending on their
position, the weight of the rocks deforms the platform, and the shape of the
platform controls which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish. The platform even
has a control panel on the side that lets you tilt it in one of four directions!
The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped
rocks (#) will stay in place. You note the positions of all of the empty
spaces (.) and rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....

You notice that the support beams along the north side of the platform are damaged;
to ensure the platform doesn't collapse, you should calculate the total load on
the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of
rows from the rock to the south edge of the platform, including the row the
rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount
of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1

The total load is the sum of the load caused by all of the rounded rocks.
In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what
is the total load on the north support beams?

--- Part Two ---

The parabolic reflector dish deforms, but not in a way that focuses the beam.
To do that, you'll need to move the rocks to the edges of the platform.
Fortunately, a button on the side of the control panel labeled "spin cycle"
attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north,
then west, then south, then east. After each tilt, the rounded rocks roll as
far as they can before the platform tilts in the next direction. After one cycle,
the platform will have finished rolling the rounded rocks in those four
directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....

After 2 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O

After 3 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O

This process should work if you leave it running long enough, but you're still
worried about the north support beams. To make sure they'll survive for a while,
you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support
beams is 64.

Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the
north support beams?

"""
import file_utils as u


def transpose(lines: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*lines)))


def mirror(lines: list[list[str]]) -> list[list[str]]:
    return lines[::-1]


def cycle(lines: list[list[str]]) -> list[list[str]]:
    # start north
    lines = move_up(lines)
    # transpose to get west-up, move and transpose to return north on top
    lines = transpose(move_up(transpose(lines)))
    # mirror to get south-up, move and mirror to return north on top
    lines = mirror(move_up(mirror(lines)))
    # transpose and mirror to get east up
    lines = transpose(mirror(move_up(mirror(transpose(lines)))))
    return lines


def parse_input(lines: list[str]) -> list[list[str]]:
    return [[c for c in line] for line in lines]


def move_up(lines: list[list[str]]) -> list[list[str]]:
    for col in range(len(lines[0])):
        block = -1
        for row in range(len(lines)):
            c = lines[row][col]
            if c == "#":
                block = row
            elif c == ".":
                pass
            else:
                # must be an O, so swap places and set new block
                if row != block + 1:    # swap if needed
                    lines[block+1][col], lines[row][col] = lines[row][col], lines[block+1][col]
                block += 1
    return lines        # void


def rock_score(rocks: list[list[str]]):
    return sum((len(rocks) - i) * line.count('O')
               for i, line in enumerate(rocks))


def part1(fname: str) -> int:
    rocks = parse_input(u.read_file(fname))
    moved_rocks = move_up(rocks)
    return rock_score(moved_rocks)


def fingerprint(lines: list[list[str]]):
    return hash(''.join(c for line in lines for c in line))


def part2(fname: str) -> int:
    fingerprints: dict[int, int] = {}
    repeat_freq = None
    rocks = parse_input(u.read_file(fname))
    for idx in range(1, 1000):
        rocks = cycle(rocks)
        fp = fingerprint(rocks)
        if fp in fingerprints:
            print(f"Found cycle at iteration {idx} - {fingerprints[fp]}")
            offset = fingerprints[fp][0]
            repeat_freq = idx - offset
            break
        fingerprints[fp] = (idx, rock_score(rocks))

    # So, for 1_000_000_000 cycles we need `offset` cycles to get to the
    # first instance of the value that is repeated after repeat_freq
    index_to_lookup = offset + ((1_000_000_000 - offset) % repeat_freq)
    return {v[0]: v[1] for _,v in fingerprints.items()}[index_to_lookup]  # type: ignore


if __name__ == "__main__":
    print(f"Result for part1 : {part1("day14.txt")}")
    print(f"Result for part2 : {part2("day14.txt")}")
