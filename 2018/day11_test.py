import day11


def test_power_levels():
    assert day11.power_level(3, 5, 8) == 4
    assert day11.power_level(122, 79, 57) == -5
    assert day11.power_level(217, 196, 39) == 0
    assert day11.power_level(101, 153, 71) == 4


def test_calc_grid():
    """ For grid serial number 18, the largest total 3x3 square 
        has a top-left corner of 33,45 (with a total power of 29); 
        these fuel cells appear in the middle of this 5x5 region:
    x -->       33  34  35
            -2  -4   4   4   4
            -4   4   4   4  -5     45
             4   3   3   4  -4     46
             1   1   2   4  -3     47
            -1   0   2  -5  -2
"""
    g = day11.calc_grid(300, 18)
    assert g[(33, 45)] == 4
    assert g[(34, 45)] == 4
    assert g[(35, 45)] == 4

    assert g[(33, 46)] == 3
    assert g[(34, 46)] == 3
    assert g[(35, 46)] == 4

    assert g[(33, 47)] == 1
    assert g[(34, 47)] == 2
    assert g[(35, 47)] == 4


def test_search_grid():
    g = day11.calc_grid(300, 18)
    assert day11.search_grid(g) == (33, 45)


def test_search_grid_2():
    g = day11.calc_grid(300, 42)
    assert day11.search_grid(g) == (21, 61)


def test_search_variable_1():
    """    For grid serial number 18, the largest total square(with a total power of 113) is 16x16 and has a top-left corner of 90, 269, so its identifier is 90, 269, 16.
        For grid serial number 42, the largest total square(with a total power of 119) is 12x12 and has a top-left corner of 232, 251, so its identifier is 232, 251, 12.)
    """
    g = day11.calc_grid(300, 18)
    assert day11.search_grid_variable(g) == ((90, 269), 16, 113)
