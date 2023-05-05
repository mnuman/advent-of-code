import utils
from collections import Counter


def read_file(filename:  str) -> Counter[int]:
    data = utils.read_file(filename, separator=",", convert=utils.toint)
    fish_counter = Counter()
    for fish_age in data:
        fish_counter[fish_age] += 1
    return fish_counter


def calculate_next_generation(current_generation: Counter[int]) -> Counter[int]:
    """From the current, calculate the next generation"""
    next_generation = Counter()
    next_generation[8] = current_generation[0]     # spawn
    next_generation[6] += current_generation[0]    # reset spawned
    for fish_age in sorted(current_generation.keys()):
        if fish_age > 0:
            next_generation[fish_age-1] += current_generation[fish_age]
    return next_generation


def part1(filename):
    current_generation = read_file(filename)
    for i in range(80):
        next_generation = calculate_next_generation(current_generation)
        current_generation = next_generation
    return current_generation.total()


def part2(filename):
    current_generation = read_file(filename)
    for i in range(256):
        next_generation = calculate_next_generation(current_generation)
        current_generation = next_generation
    return current_generation.total()


if __name__ == '__main__':
    day06_1 = part1("data/day-06.txt")
    print("Day 06 - part 1", day06_1)
    day06_2 = part2("data/day-06.txt")
    print("Day 06 - part 2", day06_2)
