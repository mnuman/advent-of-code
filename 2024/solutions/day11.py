import file_utils as f
import functools
from copy import deepcopy


def read_data(fname: str):
    return [int(i) for line in f.read_file(fname) for i in line.split()]


def process(seq, cycles):
    return sum(expand(e, cycles) for e in deepcopy(seq))


@functools.cache
def expand_number(n):
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        s = str(n)
        mid = len(s) // 2
        return [int(s[:mid]), int(s[mid:])]
    else:
        return [2024 * n]


@functools.cache
def expand(n, c):
    if c == 0:
        return 1
    else:
        expanded = expand_number(n)
        return sum([expand(e, c - 1) for e in expanded])


def part1(data):
    return process(data, 25)


def part2(data):
    return process(data, 75)


if __name__ == "__main__":
    data = read_data("day11.txt")
    print(f"Part 1: {process(data, 25)}")
    print(f"Part 2: {process(data, 75)}")
