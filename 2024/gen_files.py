import sys
import datetime


def gen_files(day_number: int):
    program_file = """import file_utils as f


def read_data(fname: str):
    data = f.read_file(fname)
    return data


def part1(data):
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    data = read_data("day{day_number}.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
"""
    test_file = """import day{day_number}


def test_read_data():
    data = day{day_number}.read_data("test_day{day_number}.txt")
    assert True


def test_part1():
    data = day{day_number}.read_data("test_day{day_number}.txt")
    assert day{day_number}.part1(data) == 1


def test_part2():
    data = day{day_number}.read_data("test_day{day_number}.txt")
    assert day{day_number}.part2(data) == 2

"""
    with open(f"./solutions/day{day_number:02}.py", "w") as s:
        s.write(program_file.replace("{day_number}", f"{day_number:02}"))
    with open(f"./tests/test_day{day_number:02}.py", "w") as t:
        t.write(test_file.replace("{day_number}", f"{day_number:02}"))
    with open(f"./data/test_day{day_number:02}.txt", "w") as dt:
        dt.write("")
    with open(f"./data/day{day_number:02}.txt", "w") as ds:
        ds.write("")
    print(f"Files for day {day_number:02} created")


if __name__ == "__main__":
    day_number = (
        int(sys.argv[1]) if len(sys.argv) > 1 else datetime.datetime.now().day + 1
    )
    print(f"Generating files for day {day_number}")
    gen_files(day_number)
