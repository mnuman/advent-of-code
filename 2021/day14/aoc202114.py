# aoc_template.py
import sys
import os
import math
import parse as parser
import collections
from functools import reduce

sys.path.extend(os.path.normpath(os.path.join(os.getcwd(), "..")))
import fileutils  # noqa: E402


def parse(puzzle_input):
    """Parse input.
       The first line is the starting material;
       rules are from line 3 onwards in format: pair -> insert
    """
    start = puzzle_input[0]
    rules = {}
    for line in puzzle_input[2:]:
        result = parser.parse("{pair} -> {insert}", line)
        rules[result["pair"]] = result["insert"]
    return start, rules


def expand_polymer(polymer, rules):
    polymer_pairs = [polymer[i - 1 : i + 1] for i in range(1, len(polymer))]
    expanded_pairs = [
        polymer_pair[0] + rules[polymer_pair] + polymer_pair[1]
        for polymer_pair in polymer_pairs
    ]
    # when stitching the expanded fragments together, there is overlap
    # between the first triple's last and the second triple's first element!
    return reduce(lambda val, el: val + el[1:], expanded_pairs[1:], expanded_pairs[0])


def pair_expand(polymer_pairs, rules):
    result = collections.Counter()
    for pair in polymer_pairs:
        pair_count = polymer_pairs[pair]
        new_pairs = pair[0] + rules[pair], rules[pair] + pair[1]
        result[new_pairs[0]] += pair_count
        result[new_pairs[1]] += pair_count
    return result


def iterate(data, cycles):
    polymer = data[0]
    rules = data[1]
    polymer_pairs = collections.Counter(
        [polymer[i - 1 : i + 1] for i in range(1, len(polymer))]
    )
    for i in range(cycles):
        polymer_pairs = pair_expand(polymer_pairs, rules)
    # unfold
    count_elements = collections.Counter()
    for pair, cnt in polymer_pairs.items():
        count_elements[pair[0]] += cnt
        count_elements[pair[1]] += cnt
    # we're counting double here due to the overlap, except for
    # the begin and end elements of the original string - hence ceil!
    return math.ceil(max(count_elements.values()) / 2) - math.ceil(
        min(count_elements.values()) / 2
    )


def part1(data):
    """Solve part 1"""
    return iterate(data, 10)


def part2(data):
    """Solve part 2.
    Tried brute-forcing it, but this is not going to work for 40 iterations.
    Starting with a polymer of length n, after m iterations we have a polymer
    of length: 2^m*n - 2^m + 1
    The puzzle input has length 20
    After 10 iterations                    2^10*n - 2^10+1 = 1024n-1023 = 19457
    For 40 iterations this would entail:   20.890.720.927.745 ... Oops

      polymer = data[0]
      rules = data[1]
      for i in range(40):
          print(f"Iterating in expansion {i}, polymer has length {len(polymer)}")
          polymer = expand_polymer(polymer, rules)
      count_elements = collections.Counter(polymer)
      return max(count_elements.values()) - min(count_elements.values())

      this should be done differently ...
      Initial polymer = NNCB => pairs NN, NC, CB
      As per the rules, these expand into NCN, NBC, CHB.
      But this is generating new pairs: NC, CN, NB, BC, CH & HB.
      When starting with a polymer of length 4 having 3 pairs, this expands
      into a polymer of length 7 having 6 pairs
    """
    return iterate(data, 40)


def solve(my_input):
    """Solve the puzzle for the given input."""
    data = parse(my_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = fileutils.read_file("day14/day-14.txt")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
