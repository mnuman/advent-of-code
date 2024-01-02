"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look.
The Elves have even given you a map; on it, they've used stars to mark the top fifty
locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need
to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in
the Advent calendar; the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly blank
("you sure ask a lot of questions") and hang on did you just say the sky ("of course,
where do you think snow comes from") when you realize that the Elves are already
loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document
(your puzzle input) has been amended by a very young Elf who was apparently just
excited to show off her art skills. Consequently, the Elves are having trouble
reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally
contained a specific calibration value that the Elves now need to recover. On each line,
the calibration value can be found by combining the first digit and the last
digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document.
What is the sum of all of the calibration values?
"""
import file_utils as u
import re

DIGITS: dict[str, int] = {str(d): d for d in range(1, 10)}
SPELLED_NUMBERS: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
NUMBERS: dict[str, int] = {**SPELLED_NUMBERS, **DIGITS}
REGEX_PATTERN = "|".join(NUMBERS.keys())


def extract_number(line: str) -> int:
    digits: list[str] = re.findall(pattern=r"\d", string=line)
    return int(digits[0] + digits[-1])


def reverse(s: str) -> str:
    return s[::-1]


def extract_number_or_spelled_out_number(line: str) -> int:
    # scan left to right - need to parenthesize patterns
    digits: list[str] = re.findall(r"(" + REGEX_PATTERN + ")", string=line)
    # scan right to left by reversing both the string and the patterns looked for
    # need to parenthesize patterns after reversing
    reverse_digits: list[str] = re.findall(
        r"(" + reverse(REGEX_PATTERN) + ")", reverse(line)
    )
    return NUMBERS[digits[0]] * 10 + NUMBERS[reverse(reverse_digits[0])]


def part1f() -> int:
    return sum(map(lambda x: extract_number(x), u.read_file("day01.txt")))


def part1() -> int:
    return sum([extract_number(line) for line in u.read_file("day01.txt")])


def part2() -> int:
    all_numbers = [
        extract_number_or_spelled_out_number(line) for line in u.read_file("day01.txt")
    ]

    return sum(all_numbers)


def part2f() -> int:
    return sum(
        map(lambda x: extract_number_or_spelled_out_number(x), u.read_file("day01.txt"))
    )


if __name__ == "__main__":
    print(f"Result for part1 : {part1()}")
    print(f"Result for part1f: {part1f()}")
    print(f"Result for part2 : {part2()}")
    print(f"Result for part2f: {part2f()}")
