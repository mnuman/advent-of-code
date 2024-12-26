from collections import Counter


def read_data(fname):
    with open(fname, "r") as f:
        lines = [line.strip().split() for line in f]
    locs_1, locs_2 = [], []
    for pair in lines:
        locs_1.append(int(pair[0]))
        locs_2.append(int(pair[1]))
    return locs_1, locs_2


def part1(locs_1, locs_2):
    l1 = sorted(locs_1)
    l2 = sorted(locs_2)
    return sum(abs(x - y) for x, y in zip(l1, l2))


def part2(locs_1, locs_2):
    l2 = Counter(locs_2)
    return sum(l2[i] * i for i in locs_1)


if __name__ == "__main__":
    locs_1, locs_2 = read_data("data/day01.txt")
    print(part1(locs_1, locs_2))
    print(part2(locs_1, locs_2))
