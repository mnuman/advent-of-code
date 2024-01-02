"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.
It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.
"Aaah!"
You turn around to see a slightly-greasy Elf with a wrench and a look of surprise.
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now;
it'll still be a while before I can fix it." You offer to help.
The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.
The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally, is a "part number"
and should be included in your sum. (Periods (.) do not count as a symbol.)
Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent
to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent
to a symbol and so is a part number; their sum is 4361.
Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?
Your puzzle answer was 520019.
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine
springs to life, you jump in the closest gondola, finally ready to ascend to
the water source.
You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.
Before you can explain the situation, she suggests that you look out the window.
There stands the engineer, holding a phone in one hand and waving with the other.
You're going so slowly that you haven't even left the station. You exit the gondola.
The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear
ratio is the result of multiplying those two numbers together.
This time, you need to find the gear ratio of every gear and add them all up so
that the engineer can figure out which gear needs to be replaced.
Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part
numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower
right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because
it is only adjacent to one part number.) Adding up all of the gear ratios
produces 467835.
What is the sum of all of the gear ratios in your engine schematic?
Your puzzle answer was 75519888.
"""
from dataclasses import dataclass
import file_utils as u
import re
from typing import Tuple


@dataclass(frozen=True)
class PartNumber:
    line: int
    start_col: int
    end_col: int
    value: int


@dataclass
class Offset:
    dx: int
    dy: int


def offsets(
        line_number: int,
        start_col: int,
        end_col: int,
        max_lines: int,
        max_cols: int) -> list[Tuple[int, int]]:
    return [
        (line, col)
        for line in range(line_number - 1, line_number + 2)
        for col in range(start_col - 1, end_col + 2)
        if 0 <= line < max_lines and
        0 <= col < max_cols and
        (line != line_number or
         (line == line_number and col < start_col or col > end_col))
        ]


def is_symbol(c: str) -> bool:
    return c != "." and not c.isdigit()


def has_adjacent_symbol(
        lines: list[str],
        line_number: int,
        start: int,
        end: int) -> bool:
    return any(
        is_symbol(lines[l][c])
        for (l, c) in offsets(line_number, start, end, len(lines), len(lines[0]))
    )


def part1(fname: str) -> int:
    result: int = 0
    lines = u.read_file((fname))
    for line_number, line in enumerate(lines):
        number_matches = re.finditer(r"\d+", line)
        result += sum(int(m.group()) for m in number_matches
                      if has_adjacent_symbol(lines, line_number, m.start(), m.end() - 1)
                      )
    return result


def find_part_numbers(lines: list[str]) -> list[PartNumber]:
    return [
        PartNumber(line_number, m.start(), m.end() - 1, int(m.group()))
        for line_number, line in enumerate(lines) for m in re.finditer(r"\d+", line)
    ]


def find_gears(lines: list[str]) -> list[Tuple[int, int]]:
    return [(line_number, m.start()) for line_number, line in enumerate(lines)
            for m in re.finditer(r"\*", line)]


def find_parts_around_gear(
        gear: Tuple[int, int],
        parts: list[PartNumber]
        ) -> Tuple[int, int]:
    offsets: list[Offset] = [
        Offset(dx, dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == 0 and dy == 0)
    ]
    matching_parts: set[PartNumber] = set(
        part
        for offset in offsets
        for part in parts
        if part.line == gear[0] + offset.dx and
        part.start_col <= gear[1] + offset.dy <= part.end_col
    )
    return (0, 0) if len(matching_parts) != 2 else (
        matching_parts.pop().value, matching_parts.pop().value)


def part2(fname: str) -> int:
    result: int = 0
    lines = u.read_file((fname))
    gears = find_gears(lines)
    part_numbers = find_part_numbers(lines)
    for gear in gears:
        parts = find_parts_around_gear(gear, part_numbers)
        result += parts[0] * parts[1]
    return result


if __name__ == "__main__":
    print(f"Result for part1 : {part1("day03.txt")}")
    print(f"Result for part2 : {part2("day03.txt")}")
