import day09b


def test_scenario():
    test_list = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277,
                 309, 576]
    assert day09b.find_sum(test_list, 15 - 1) == ([15, 25, 47, 40], 127, 15 + 47)
