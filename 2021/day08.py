from collections import defaultdict
from typing import Iterable

import utils


def read_file(filename: str) -> list[str]:
    return utils.read_file(filename)


def read_file_v2(filename: str) -> list[tuple[tuple[str], tuple[str]]]:
    data = utils.read_file(filename)
    result = []
    for line in data:
        parts = line.split("|")
        result.append((tuple(parts[0].strip().split()), tuple(parts[1].strip().split())))
    return result


def tokenize_lines(lines: list[str]) -> dict[str, int]:
    """Split line, process part after separator and tokenize."""
    tokenized = [''.join(sorted([c for c in token]))
                 for line in lines
                 for token in line.split("|")[1].strip(" ").split(" ")
                 ]
    result = defaultdict(lambda: 0)
    for token in tokenized:
        result[token] += 1
    return result


def determine_unique_entries(digit_representations: tuple[str]) -> tuple[str]:
    """From the representation of the digits, determine the ones with a unique length (i.e. occurring once).
       The digits that are unique represented will be returned, sorted by ascending length.
    """
    all_lengths = [len(s) for s in digit_representations]
    unique_lengths = [s for s in set(all_lengths) if all_lengths.count(s) == 1]
    return tuple(sorted([ul for ul in digit_representations if len(ul) in unique_lengths], key=lambda x: len(x)))


def fingerprint(pattern: str, other_patterns: Iterable[str]) -> str:
    """
    Compute similarities for given str to collection of other strings, i.e. count identical characters
    and return joined as a string in sorted order. This should uniquely identify each digit in all
    consistent representation.
    """
    unique_digit_patterns = determine_unique_entries(other_patterns)
    return ''.join(sorted([str(sum([1 for c in pattern if c in up])) for up in unique_digit_patterns]))


def part1(filename: str) -> tuple[int, int, int, int]:
    data = read_file(filename)
    tokenized_data = tokenize_lines(data)
    number_1, number_4, number_7, number_8 = 0, 0, 0, 0
    for i in tokenized_data.keys():
        match (len(i)):
            case 2:
                number_1 += tokenized_data[i]
            case 4:
                number_4 += tokenized_data[i]
            case 3:
                number_7 += tokenized_data[i]
            case 7:
                number_8 += tokenized_data[i]
    return number_1, number_4, number_7, number_8



digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

digit_fingerprints = {fingerprint(v, digits.values()): str(k) for k, v in digits.items()}


def interpret_display(wiring: Iterable[str], display: Iterable[str]) -> int:
    """
    Compute the similarity for the digits in the display to the items in the wiring. The similarities form a
    fingerprint for the number, so we can look the correct digit up in the standard digit_fingerprints.
    Concatenate (keys are strings there) and convert to an integer for the answer
    """
    return int(''.join([digit_fingerprints[fingerprint(d, wiring)] for d in display]))


def part2(filename: str) -> int:
    all_lines = read_file_v2(filename)
    return sum([interpret_display(wiring, display) for wiring, display in all_lines])


if __name__ == '__main__':
    day08_1 = part1("data/day-08.txt")
    print("Day 08 - part 1", day08_1, sum(day08_1))
    day08_2 = part2("data/day-08.txt")
    print("Day 08 - part 2", day08_2)
