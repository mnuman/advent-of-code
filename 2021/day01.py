import utils


def get_data(filename):
    return utils.read_file(filename=filename, convert=utils.toint)


def count_next_is_greater(iterable):
    count = 0
    if len(iterable) > 1:
        count = sum(
            [1 for i in range(1, len(iterable)) if iterable[i - 1] < iterable[i]]
        )
    return count


def part1(measurements):
    return sum([1 for (a, b) in zip(measurements, measurements[1:]) if b > a])


def count_window_is_greater(iterable):
    count = 0
    if len(iterable) > 3:
        # element i and i-1 occur on both sides - omitted
        count = sum(
            [
                1
                for i in range(2, len(iterable) - 1)
                if iterable[i - 2] < iterable[i + 1]
            ]
        )
    return count


def part2(measurements):
    windowed = [
        measurements[i] + measurements[i + 1] + measurements[i + 2]
        for i in range(len(measurements) - 2)
    ]
    return sum([1 for (a, b) in zip(windowed, windowed[1:]) if b > a])


if __name__ == "__main__":
    day01_1 = count_next_is_greater(get_data("data/day-01.txt"))
    print("Day 01 - part 1", day01_1)
    print("Day 01 - part 1", part1(get_data("data/day-01.txt")))
    day01_2 = count_window_is_greater(get_data("data/day-01.txt"))
    print("Day 01 - part 2", day01_2)
    print("Day 01 - part 2", part2(get_data("data/day-01.txt")))
