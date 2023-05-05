import day01b, utils


def test_find_target():
    number_list = utils.read_file('data/test_day01a.txt', convert=day01b.to_int)
    assert day01b.find_target(number_list, 2020) == (979, 366, 675, 241861950)
