import file_utils as f
from operator import mul, add
from itertools import product

operators_part1 = [mul, add]
operators_part2 = [mul, add, lambda x, y: int(str(x) + str(y))]


def read_data(fname: str):
    data = []
    for line in f.read_file(filename=fname):
        target, inputs = line.split(":")
        values = list(map(int, inputs.split()))
        data.append((int(target), values))
    return data


def can_produce(operators, values, target):
    for ops in product(operators, repeat=len(values) - 1):
        result = values[0]
        for i in range(1, len(values)):
            result = ops[i - 1](result, values[i])
        if result == target:
            return True
    return False


def part1(data):
    return sum(
        target
        for target, values in data
        if can_produce(operators_part1, values, target)
    )


def part2(data):
    return sum(
        target
        for target, values in data
        if can_produce(operators_part2, values, target)
    )


if __name__ == "__main__":
    data = read_data("day07.txt")
    print(data)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
