import file_utils as f

"""
Using a complex regex does work on the problem's test data, but not on the
actual data. In my case, it chokes on the eight and eleventh patterns (and
probably quite some more after that).
Need to invent a proper chomping algorithm myself.

281 too low
"""


def read_data(fname: str):
    data = f.read_file(fname)
    patterns = set([p.strip() for p in data[0].split(",")])
    designs = data[2:]
    return patterns, designs


def can_compose(patterns, string):
    n = len(string)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in patterns:
            if (
                i >= len(pattern)
                and dp[i - len(pattern)]
                and string[i - len(pattern) : i] == pattern
            ):
                dp[i] = True
                break

    return dp[n]


def count_ways(patterns, string):
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and string[i - len(pattern) : i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[n]


def part1(data):
    patterns, designs = data
    return sum(1 for design in designs if count_ways(patterns, design))


def part2(data):
    patterns, designs = data
    return sum(count_ways(patterns, design) for design in designs)


if __name__ == "__main__":
    data = read_data("day19.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
