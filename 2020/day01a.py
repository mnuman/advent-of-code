import utils


def find_target(my_list, target):
    for idx, number in enumerate(my_list):
        for second_number in my_list[idx:]:
            if number + second_number == target:
                return number, second_number, number * second_number


def to_int(s):
    """Inline conversion function from string to integer"""
    return int(s)


if __name__ == "__main__":
    number_list = utils.read_file('data/day01a.txt', convert=to_int)
    print(find_target(number_list, 2020))