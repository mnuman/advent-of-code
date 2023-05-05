import day10a
import utils

TEST_JOLTAGES = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_device_joltage():
    assert day10a.device_joltage(TEST_JOLTAGES) == 22


def test_diffs():
    assert day10a.diffs(day10a.sort_adapters(TEST_JOLTAGES)) == (7, 5)


def test_scenario():
    mylist = day10a.sort_adapters(utils.read_file("data/test_day10.txt", convert=int))
    assert day10a.diffs(mylist) == (22, 10)
