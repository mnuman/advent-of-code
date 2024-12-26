import file_utils as f
import re


def read_data(fname: str) -> list[str]:
    return f.read_file(filename=fname)


def part1(data: list[str]) -> int:
    PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
    matches = []
    result = 0
    for line in data:
        matches += re.findall(PATTERN, line)
    for m in matches:
        operands = m[4:-1].split(",")
        result += int(operands[0]) * int(operands[1])
    return result


def part2(data: list[str]) -> int:
    PATTERN = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    matches = []
    result = 0
    for line in data:
        matches += re.findall(PATTERN, line)
    factor = 1
    for m in matches:
        if m == "do()":
            factor = 1
        elif m == "don't()":
            factor = 0
        else:
            operands = m[4:-1].split(",")
            result += factor * int(operands[0]) * int(operands[1])
    return result


if __name__ == "__main__":
    data = read_data("day03.txt")
    print(part1(data))
    print(part2(data))
