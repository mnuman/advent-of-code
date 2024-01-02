"""
--- Day 21: Step Counter ---

You manage to catch the airship right as it's dropping someone else off on their
all-expenses-paid trip to Desert Island! It even helpfully drops you off near
the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we
have enough sand to filter the water for Snow Island and we'll have snow again
in no time."

While you wait, one of the Elves that works with the gardener heard how good
you are at solving problems and would like your help. He needs to get his steps
in for the day, and so he'd like to know which garden plots he can reach with
exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S),
garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

The Elf starts at the starting position (S) which also counts as a garden plot. Then,
he can take one step north, south, east, or west, but only onto tiles that are garden
plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

Then, he takes a second step. Since at this point he could be at either tile marked O,
his second step would allow him to reach any garden plot that is one step north,
south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........

After two steps, he could be at any of the tiles marked O above, including the
starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........

He will continue like this until his steps for the day have been exhausted. After a
total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........

In this example, if the Elf's goal was to get exactly 6 more steps today, he
could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed
you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots
could the Elf reach in exactly 64 steps?

The Elf seems confused by your answer until he realizes his mistake: he was reading
from a list of his favorite numbers that are both perfect squares and perfect
cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map
repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the
edge of the example map above, you would find that it keeps repeating:
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................

This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm
layout; garden plots and rocks repeat as far as you can see. The Elf still starts
on the one middle tile marked S, though - every other repeated S is replaced with
a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the
example map for different numbers of steps:

    In exactly 6 steps, he can still reach 16 garden plots.
    In exactly 10 steps, he can reach any of 50 garden plots.
    In exactly 50 steps, he can reach 1594 garden plots.
    In exactly 100 steps, he can reach 6536 garden plots.
    In exactly 500 steps, he can reach 167004 garden plots.
    In exactly 1000 steps, he can reach 668697 garden plots.
    In exactly 5000 steps, he can reach 16733044 garden plots.

However, the step count the Elf needs is much larger! Starting from the garden
plot marked S on your infinite map, how many garden plots could the Elf reach
in exactly 26501365 steps?
"""
from dataclasses import dataclass
import file_utils as u
from enum import Enum
from queue import Queue

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Plot(Enum):
    ROCK = "#"
    GARDEN = "."
    START = "S"


@dataclass(frozen=True)
class Position:
    row: int
    col: int


def parse_file(fname):
    return {
        Position(row, col): Plot(val)
        for row, line in enumerate(u.read_file(fname))
        for col, val in enumerate(line)
    }


def neighbours_on_infinite_grid(
    p: Position, m: dict[Position, Plot], max_row: int, max_col: int
) -> list[Position]:
    return [
        Position(p.row + drow, p.col + dcol)
        for drow, dcol in DIRECTIONS
        if m[Position((p.row + drow) % (max_row + 1), (p.col + dcol) % (max_col + 1))]
        != Plot.ROCK
    ]


def accessible_neighbours(
    p: Position, m: dict[Position, Plot], max_row: int, max_col: int
) -> list[Position]:
    return [
        Position(p.row + drow, p.col + dcol)
        for drow, dcol in DIRECTIONS
        if 0 <= p.row + drow <= max_row
        and 0 <= p.col + dcol <= max_col
        and m[Position(p.row + drow, p.col + dcol)] != Plot.ROCK
    ]


def bfs(map: dict[Position, Plot], max_steps: int) -> dict[Position, int]:
    start = [pos for pos, val in map.items() if val == Plot.START][0]
    max_row, max_col = max(p.row for p in map.keys()), max(p.col for p in map.keys())
    fringe = Queue()
    fringe.put((start, 0))
    visited = {start: 0}
    steps = 0
    while not fringe.empty() and steps <= max_steps:
        curr, steps = fringe.get()
        for n in accessible_neighbours(curr, map, max_row, max_col):
            if n not in visited:
                visited[n] = steps + 1
                fringe.put((n, steps + 1))
    return visited


def infinite_grid(map: dict[Position, Plot], max_steps: int) -> dict[Position, int]:
    start = [pos for pos, val in map.items() if val == Plot.START][0]
    max_row, max_col = (max(p.row for p in map.keys()), max(p.col for p in map.keys()))
    fringe = Queue()
    fringe.put(start)
    visited = {start: 0}
    steps = 0
    while steps <= max_steps and not fringe.empty():
        curr = fringe.get()
        for n in neighbours_on_infinite_grid(curr, map, max_row, max_col):
            steps = visited[curr]
            if n not in visited or (steps + 1) < visited[n]:
                visited[n] = steps + 1
                fringe.put(n)
    return visited


def part1(fname: str, max_steps=64) -> int:
    map = parse_file(fname)
    visits = bfs(map, max_steps)
    candidate_steps = [x for x in range(max_steps + 1) if x % 2 == 0]
    return len([k for k, v in visits.items() if v in candidate_steps])


def part2(fname: str, max_steps=64) -> int:
    map = parse_file(fname)
    visits = infinite_grid(map, 500)
    for i in range(401, 501, 2):
        odd_steps = [j for j in range(1, i + 1) if j % 2 != 0]
        cnt = len([k for k, v in visits.items() if v in odd_steps])
        print(f"Max: {i} - count {cnt}")


def sample_part2(fname: str, max_steps=64):
    map = parse_file(fname)
    visits = infinite_grid(map, max_steps)
    for i in range(1, max_steps + 1, 2):
        odd_steps = [j for j in range(1, i + 1) if j % 2 != 0]
        cnt = len([k for k, v in visits.items() if v in odd_steps])
        print(f"Max: {i} - count {cnt}")
    pass


if __name__ == "__main__":
    print(f"Results part1: {part1('day21.txt')}")
    print(f"Results part2: {part2('day21.txt', 500)}")
