import utils


def find_target(my_list, target):
    for i, first_number in enumerate(my_list):
        for j, second_number in enumerate(my_list[i:]):
            for third_number in my_list[i+j:]:
                if first_number + second_number + third_number == target:
                    return first_number, second_number, third_number, first_number * second_number * third_number

def to_int(s):
    """Inline conversion function from string to integer"""
    return int(s)


if __name__ == "__main__":
    number_list = utils.read_file('data/day01a.txt', convert=to_int)
    print(find_target(number_list, 2020))
