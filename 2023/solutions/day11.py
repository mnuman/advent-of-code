"""
--- Day 11: Cosmic Expansion ---

You continue following signs for "Hot Springs" and eventually come across an 
observatory. The Elf within turns out to be a researcher studying cosmic 
expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this 
research project. However, he confirms that the hot springs are the next-closest area 
likely to have people; he'll even take you straight there once he's done with today'
s observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single 
giant image (your puzzle input). The image includes empty space (.) and galaxies 
(#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The researcher is trying to figure out the sum of the lengths of the shortest path 
between every pair of galaxies. However, there's a catch: the universe expanded in 
the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In 
fact, the result is that any rows or columns that contain no galaxies should 
all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^

These rows and columns need to be twice as big; the result of cosmic expansion 
therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......

Equipped with this expanded universe, the shortest path between every pair of 
galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the 
pair doesn't matter. For each pair, find any shortest path between the two galaxies 
using only steps that move up, down, left, or right exactly one . or # at a time. 
(The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......

This path has length 9 because it takes a minimum of nine steps to get from 
galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 
itself). Here are some other example shortest path lengths:

    Between galaxy 1 and galaxy 7: 15
    Between galaxy 3 and galaxy 6: 17
    Between galaxy 8 and galaxy 9: 5

In this example, after expanding the universe, the sum of the shortest path between 
all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of 
galaxies. What is the sum of these lengths?

The galaxies are much older (and thus much farther apart) than the researcher 
initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million 
times larger. That is, each empty row should be replaced with 1000000 empty rows, and 
each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the 
sum of the shortest paths between every pair of galaxies would be 1030. If each empty 
row or column were merely 100 times larger, the sum of the shortest paths between every 
pair of galaxies would be 8410. However, your universe will need to expand far beyond 
these values.)

Starting with the same initial image, expand the universe according to these new rules, 
then find the length of the shortest path between every pair of galaxies. 
What is the sum of these lengths?
"""
import file_utils as u
from aoc_utils import manhattan_distance
import numpy as np
from itertools import combinations


def add_rows(g: np.array) -> np.array:
    empties = [idx for idx, row in enumerate(g) if sum(row) == 0]
    empties.reverse()
    for row_number in empties:
        g = np.insert(g, row_number + 1, g[row_number], axis=0)
    return g


def expand_universe(g: np.array) -> None:
    result = add_rows(g.copy())
    result = add_rows(result.transpose())
    return result.transpose()


def find_galaxies(expanded_map: np.array) -> list[tuple[int, int]]:
    return [
        (row_idx, col_idx) 
        for row_idx, row in enumerate(expanded_map) 
        for col_idx, c in enumerate(row) if c == 1
        ]


def modified_manhattan_distance(
        g1: tuple[int, int], 
        g2: tuple[int, int], 
        empty_rows: list[int], 
        empty_cols: list[int]
) -> int:
    """Adjust manhattan distance by counting all empty rows/cols
    as 1000000 instead of 1. As the distance 1 has already been
    incorporated into the manhattan distance, a correction of
    1000000 - 1 is needed for each empty row or column.
    """
    return manhattan_distance(g1, g2) + \
        (1_000_000 - 1) * (
            sum(
                1 for r in empty_rows if min(g1[0], g2[0]) < r < max(g1[0], g2[0])
            ) +
            sum(
                1 for c in empty_cols if min(g1[1], g2[1]) < c < max(g1[1], g2[1])
            )
        )


def part1(fname: str) -> int:
    lines = u.read_file(fname)
    galaxy_map = np.array([[0 if c == '.' else 1 for c in line] for line in lines])
    expanded_map = expand_universe(galaxy_map)
    galaxies: list[tuple[int, int]] = find_galaxies(expanded_map)
    return sum(manhattan_distance(g1, g2) 
               for i, g1 in enumerate(galaxies) 
               for j, g2 in enumerate(galaxies) 
               if i < j)


def part2(fname: str) -> int:
    lines = u.read_file(fname)
    galaxy_map = np.array([[0 if c == '.' else 1 for c in line] for line in lines])
    galaxies: list[tuple[int, int]] = find_galaxies(galaxy_map)
    empty_rows: list[int] = [
        idx for idx, row in enumerate(galaxy_map) if sum(row) == 0]
    empty_cols: list[int] = [
        idx for idx, col in enumerate(galaxy_map.transpose()) if sum(col) == 0]
    return sum(modified_manhattan_distance(g1, g2, empty_rows, empty_cols)
               for i, g1 in enumerate(galaxies) 
               for j, g2 in enumerate(galaxies) 
               if i < j)


if __name__ == "__main__":
    print(f"Result for part1 : {part1("day11.txt")}")
    print(f"Result for part2 : {part2("day11.txt")}")
