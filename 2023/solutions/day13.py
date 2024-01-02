"""
--- Day 13: Point of Incidence ---

With your help, the hot springs team locates an appropriate spring which launches you
neatly and precisely up to the edge of Lava Island.

There's just one problem: you don't see any lava.

You do see a lot of ash and igneous rock; there are even what look like gray
mountains scattered around. After a while, you make your way to a nearby cluster
of mountains only to discover that the valley between them is completely full of
large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps
you should head in that direction?

As you move through the valley of mirrors, you find that several of them have
fallen from the large metal frames keeping them in place. The mirrors are extremely
flat and shiny, and many of the fallen mirrors have lodged into the ash at strange
angles. Because the terrain is all one color, it's hard to tell where it's safe
to walk or where you're about to run into a mirror.

You note down the patterns of ash (.) and rocks (#) that you see as you walk
(your puzzle input); perhaps by carefully analyzing these patterns, you can
figure out where the mirrors are!

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

To find the reflection in each pattern, you need to find a perfect reflection across
either a horizontal line between two rows or across a vertical line between two
columns.

In the first pattern, the reflection is across a vertical line between two columns;
arrows on each of the two columns point at the line between the columns:

123456789
    ><
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><
123456789

In this pattern, the line of reflection is the vertical line between columns
5 and 6. Because the vertical line is not perfectly in the middle of the
pattern, part of the pattern (column 1) has nowhere to reflect onto and
can be ignored; every other column has a reflected column within the
pattern and must match exactly: column 2 matches column 9,
column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

This pattern reflects across the horizontal line between rows 4 and 5.
Row 1 would reflect with a hypothetical row 8, but since that's not
in the pattern, row 1 doesn't need to match anything. The remaining
rows match: row 2 matches row 7, row 3 matches row 6, and row 4
matches row 5.

To summarize your pattern notes, add up the number of columns to the left of each
 vertical line of reflection; to that, also add 100 multiplied by the number of
 rows above each horizontal line of reflection. In the above example, the
 first pattern's vertical line has 5 columns to its left and the second
 pattern's horizontal line has 4 rows above it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What
number do you get after summarizing all of your notes?

You resume walking through the valley of mirrors and - SMACK! - run directly into one.
Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge:
exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different
reflection line to be valid. (The old reflection line won't necessarily continue
 being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

The first pattern's smudge is in the top-left corner. If the top-left # were instead .,
it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7

With the smudge in the top-left corner repaired, a new horizontal line of
reflection between rows 3 and 4 now exists. Row 7 has no corresponding
reflected row and can be ignored, but every other row matches exactly:
row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth
symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7

Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines.
In this example, the first pattern's new horizontal line has 3 rows above it and
the second pattern's new horizontal line has 1 row above it, summarizing to the
value 400.

In each pattern, fix the smudge and find the different line of reflection. What
number do you get after summarizing the new reflection line in each pattern in
your notes?

"""
from typing import Optional
import file_utils as u


def transpose(lines: list[str]) -> list[str]:
    """Transpose the list of strings into a new list of strings"""
    return [''.join([c for c in t])
            for t in list(zip(*[[c for c in line] for line in lines]))]


def mirrors(lines: list[str]) -> Optional[int]:
    n = len(lines)
    for m in range(0, len(lines)):
        pairs: list[tuple[int, int]] = [
            (m-j-1, m+j) for j in range(0, n) if m-j > 0 and m+j < n]
        if len(pairs) > 0 and all(lines[i] == lines[j] for i, j in pairs):
            return m


def parse_input(fname: str) -> list[list[str]]:
    content = u.read_raw_file(fname)
    return [grp.split("\n") for grp in content.split("\n\n")]


def count_differences(line_1: str, line_2: str) -> int:
    return sum(1 for char_1, char_2 in zip(line_1, line_2) if char_1 != char_2)


def find_reflection(group: list[str]) -> tuple[int, int]:
    for row in range(len(group) - 1):
        differences = 0
        for idx in range(min(row + 1, len(group)-row-1)):
            differences += count_differences(group[row - idx], group[row + idx + 1])
            if differences > 1:
                break
        else:
            """else in for loop only executes if no break has occurred """
            if differences == 1:
                return row + 1, 0   # reflection with a single difference - done!
    col, row = find_reflection(transpose(group))
    return row, col


def part1(fname: str) -> int:
    groups: list[list[str]] = parse_input(fname)
    rows = [mirrors(g) for g in groups]
    cols = [mirrors(transpose(g)) for g in groups]
    return 100*sum(r for r in rows if r is not None) + \
        sum(c for c in cols if c is not None)


def part2(fname: str) -> int:
    return sum(
        100*res[0] + res[1]
        for res in [find_reflection(g) for g in parse_input(fname)]
        )


if __name__ == "__main__":
    print(f"Result for part1 : {part1("day13.txt")}")
    # print(f"Check for part2 - both row/col for symmetry: {check("day13.txt")}")
    print(f"Result for part2 : {part2("day13.txt")}")
