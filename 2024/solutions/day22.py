from collections import defaultdict
import file_utils as f
from functools import cache

buyers_prices = defaultdict(list)


@cache
def mix(num, secret):
    return num ^ secret


@cache
def prune(secret):
    return secret % 0x1000000


def read_data(fname: str):
    return list(map(int, f.read_file(fname)))


@cache
def op1(secret):
    return prune(mix(64 * secret, secret))


@cache
def op2(secret):
    return prune(mix(secret // 32, secret))


@cache
def op3(secret):
    return prune(mix(secret * 2048, secret))


def generate_secret(secret):
    return op3(op2(op1(secret)))


def part1(data):
    result = []
    for idx, number in enumerate(data):
        secret = number
        buyers_prices[idx].append(secret % 10)
        for i in range(2000):
            secret = generate_secret(secret)
            buyers_prices[idx].append(secret % 10)
        result.append(secret)
    return sum(result)


def part2(data):
    # for the actual datafile, the some of all lengths of the pricepoints is approximately 4M.
    pricepoint = defaultdict(int)
    for buyer in buyers_prices:
        seen = set()  # diff sequences seen for this buyer
        prices = buyers_prices[buyer]
        diffs = [p2 - p1 for p1, p2 in zip(prices, prices[1:])]
        for i in range(len(diffs) - 3):
            seq = tuple(diffs[i : i + 4])
            if seq not in seen:  # first time - for this buyer
                pricepoint[seq] += prices[i + 4]
                seen.add(seq)
    return max(pricepoint.values())


if __name__ == "__main__":
    data = read_data("day22.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
