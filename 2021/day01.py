import utils


def get_data(filename):
    return utils.read_file(filename=filename, convert=utils.toint)


def count_next_is_greater(iterable):
    count = 0
    if len(iterable) > 1:
        count = sum([1 for i in range(1, len(iterable)) if
                     iterable[i - 1] < iterable[i]])
    return count


def count_window_is_greater(iterable):
    count = 0
    if len(iterable) > 3:
        # element i and i-1 occur on both sides - omitted
        count = sum([1 for i in range(2, len(iterable) - 1) if
                     iterable[i - 2] < iterable[i + 1]])
    return count


if __name__ == '__main__':
    day01_1 = count_next_is_greater(get_data("data/day-01.txt"))
    print("Day 01 - part 1", day01_1)
    day01_2 = count_window_is_greater(get_data("data/day-01.txt"))
    print("Day 01 - part 2", day01_2)
