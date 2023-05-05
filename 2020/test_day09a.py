import day09a


def test_verify_xmas_list():
    test_list = [35, 20, 15, 25, 47, 62]
    assert day09a.first_non_sum(test_list, window_size=2) == (15, 3)
    assert day09a.first_non_sum(test_list, window_size=5) is None


def test_scenario():
    scenario_list = day09a.parse_xmas_list("data/test_day09.txt")
    assert day09a.first_non_sum(scenario_list, window_size=5) == (127, 15)
