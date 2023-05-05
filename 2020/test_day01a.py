import day01a, utils


def test_find_target():
    number_list = utils.read_file('data/test_day01a.txt', convert=day01a.to_int)
    assert day01a.find_target(number_list, 2020) == (1721,299,514579)
