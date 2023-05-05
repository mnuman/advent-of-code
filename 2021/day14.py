from datetime import datetime
import re
from collections import Counter

import utils

"""
Could not find a performing solution myself ... looking for some insights, I came across this solution:
https://github.com/kresimir-lukin/AdventOfCode2021/blob/main/day14.py

Just running this to see how it performs - not submitting the solution for AoC.
"""
def readfile(filename):
    lines = utils.read_file(filename)
    starting_polymer = lines[0]
    rules = {}
    for line in lines[2:]:
        source, target = re.match(r"(\w+) -> (\w+)", line).groups()
        rules[source] = target
    return starting_polymer, rules


def part1(filename):
    template, rules = readfile(filename)
    return polymerize(template, rules, 10)


def part2(filename):
    template, rules = readfile(filename)
    return polymerize(template, rules, 40)


def polymerize(template, rules, steps):
    pair_frequencies = Counter()
    char_frequencies = Counter(template)

    for pos in range(1, len(template)):
        pair = template[pos - 1:pos + 1]
        pair_frequencies[pair] += 1

    for _ in range(steps):
        pair_frequencies_step = Counter()
        for pair, frequency in pair_frequencies.items():
            if pair in rules:
                pair_frequencies_step[pair[0] + rules[pair]] += frequency
                pair_frequencies_step[rules[pair] + pair[1]] += frequency
                char_frequencies[rules[pair]] += frequency
        pair_frequencies = pair_frequencies_step

    return max(char_frequencies.values()) - min(char_frequencies.values())


if __name__ == '__main__':
    day14_1 = part1("data/day-14.txt")
    print("Day 14 - part 1", day14_1)
    day14_2 = part2("data/day-14.txt")
    print("Day 14 - part 2", day14_2)

