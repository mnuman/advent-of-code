import file_utils as f


def read_data(fname: str):
    data = f.read_file(fname)
    idx = 0
    keys = []
    locks = []
    while idx < len(data):
        block = data[idx : idx + 7]
        if block[0].startswith("#"):
            locks.append(count_pins(block))
        else:
            keys.append(count_pins(list(reversed(block))))
        idx += 8
    return locks, keys


def count_pins(lines):
    return tuple(
        max(
            r
            for r, c in [
                (r, c)
                for r, line in enumerate(lines)
                for c, char in enumerate(line)
                if char == "#"
            ]
            if c == col
        )
        for col in range(len(lines[0]))
    )


# lock and key match if there is no overlap, i.e. sum of the corresponding
# counts must be 5 or less for all pin locations
def matches(lock, key):
    return all([c[0] + c[1] <= 5 for c in zip(lock, key)])


def part1(locks, keys):
    return sum(1 for lock in locks for key in keys if matches(lock, key))


if __name__ == "__main__":
    locks, keys = read_data("day25.txt")
    print(f"Part 1: {part1(locks, keys)}")
