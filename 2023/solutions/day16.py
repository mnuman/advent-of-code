"""
With the beam of light completely focused somewhere, the reindeer leads you
deeper still into the Lava Production Facility. At some point, you realize
that the steel facility walls have been replaced with cave, and the doorways
are just cave, and the floor is cave, and you're pretty sure this is actually
just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a
bright light in a cavern up ahead. There, you discover that the beam of
light you so carefully focused is emerging from the cavern wall closest to
the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional
square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the
grid, but each tile on the grid converts some of the beam's light into
heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

The beam enters in the top-left corner from the left and heading to the right.
Then, its behavior depends on what it encounters as it moves:

    If the beam encounters empty space (.), it continues in the same direction.
    If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees
    depending on the angle of the mirror. For instance, a rightward-moving
    beam that encounters a / mirror would continue upward in the mirror's
    column, while a rightward-moving beam that encounters a \ mirror would
    continue downward from the mirror's column.
    If the beam encounters the pointy end of a splitter (| or -), the
    beam passes through the splitter as if the splitter were empty space.
    For instance, a rightward-moving beam that encounters a - splitter would
    continue in the same direction.
    If the beam encounters the flat side of a splitter (| or -), the beam is
    split into two beams going in each of the two directions the splitter's
    pointy ends are pointing. For instance, a rightward-moving beam that
    encounters a | splitter would split into two beams: one that continues
    upward from the splitter's column and one that continues downward from
    the splitter's column.

Beams do not interact with other beams; a tile can have many beams passing
through it at the same time. A tile is energized if that tile has at least
one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..

Beams are only shown on empty tiles; arrows indicate the direction of the
 beams. If a tile contains beams moving in multiple directions, the number
 of distinct directions is shown instead. Here is the same diagram but
 instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..

Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the
contraption, you need to start by analyzing the current situation. With
the beam starting in the top-left heading right, how many tiles end up
being energized?
"""
import file_utils as u


def calculate_paths(
    grid: dict[tuple[int, int], str],
    visited: set[tuple[int, int, int, int]],
    rows: int,
    cols: int,
    row: int = 0,
    col: int = 0,
    drow: int = 0,
    dcol: int = 1,
):
    while 0 <= row < rows and 0 <= col < cols and not (row, col, drow, dcol) in visited:
        visited.add((row, col, drow, dcol))  # mark current as visited
        match grid[(row, col)]:
            case ".":
                row, col = row + drow, col + dcol
            case "\\":
                drow, dcol = dcol, drow
                row, col = row + drow, col + dcol
            case "/":
                drow, dcol = -dcol, -drow
                row, col = row + drow, col + dcol
            case "-":
                if dcol == 0:  # split
                    calculate_paths(
                        grid, visited, rows, cols, row, col - 1, 0, -1
                    )  # left
                    calculate_paths(
                        grid, visited, rows, cols, row, col + 1, 0, 1
                    )  # right
                    return  # no need to continue current iteration as we split
                else:
                    row, col = row + drow, col + dcol
            case "|":
                if drow == 0:
                    calculate_paths(
                        grid, visited, rows, cols, row - 1, col, -1, 0
                    )  # up
                    calculate_paths(
                        grid, visited, rows, cols, row + 1, col, +1, 0
                    )  # down
                    return
                else:
                    row, col = row + drow, col + dcol
            case _:
                row, col = row + drow, col + dcol


def part1(fname: str) -> int:
    lines: list[str] = u.read_file(fname)
    grid: dict[tuple[int, int], str] = {
        (r, c): char for r, line in enumerate(lines) for c, char in enumerate(line)
    }
    visited: set[tuple[int, int, int, int]] = set()
    calculate_paths(grid, visited, len(lines), len(lines[0]))
    return len(set((r, c) for r, c, _, _ in visited))


def part2(fname: str) -> int:
    lines: list[str] = u.read_file(fname)
    grid: dict[tuple[int, int], str] = {
        (r, c): char for r, line in enumerate(lines) for c, char in enumerate(line)
    }
    rows = len(lines)
    cols = len(lines[0])
    assert rows == cols
    results = []
    for i, (row, col, drow, dcol) in enumerate(
        [(0, i, 1, 0) for i in range(rows)]
        + [(i, 0, 0, 1) for i in range(rows)]
        + [(rows - 1, i, -1, 0) for i in range(rows)]
        + [(i, rows - 1, 0, -1) for i in range(rows)]
    ):
        visited: set[tuple[int, int, int, int]] = set()
        calculate_paths(grid, visited, rows, cols, row, col, drow, dcol)
        val = len(set((r, c) for r, c, _, _ in visited))
        print(
            f"Considered candidate {i}, starting at row {row}, col {col} - score {val}"
        )
        results.append(val)
    return max(results)


if __name__ == "__main__":
    print(f"Result for part1 : {part1('day16.txt')}")
    print(f"Result for part2 : {part2('day16.txt')}")
