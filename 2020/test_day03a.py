import day03a
import utils
from functools import reduce

area = [".....#", "#.....", "......"]


def test_init():
    p = day03a.Slope(area)
    assert p.col == 0
    assert p.row == 0
    assert p.max_col == 5  # x in range [0,5]
    assert p.max_row == 2  # y in range [0,2]


def test_normalize_coordinates_0():
    p = day03a.Slope(area)
    p.normalize_coordinates()
    assert p.col == 0
    assert p.row == 0


def test_normalize_coordinates_1():
    p = day03a.Slope(area, col=6, row=3)  # equates to origin
    p.normalize_coordinates()
    assert p.col == 0
    assert p.row == 0


def test_normalize_coordinates_2():
    p = day03a.Slope(area, col=99, row=99)
    p.normalize_coordinates()
    assert p.col == 3
    assert p.row == 0


def test_no_move():
    p = day03a.Slope(area)
    p.move(0, 0)
    assert p.col == 0
    assert p.row == 0


def test_move_1_1():
    p = day03a.Slope(area)
    p.move(1, 1)
    assert p.col == 1
    assert p.row == 1


def test_move_10_10():
    p = day03a.Slope(area)
    p.move(10, 10)
    assert p.col == 4
    assert p.row == 1


def test_hit_tree_origin():
    p = day03a.Slope(area)
    assert not (p.hit_tree())


def test_hit_tree_1():
    p = day03a.Slope(area, col=5, row=0)
    assert p.hit_tree()


def test_descent_1():
    p = day03a.Slope(area)
    hits = p.descent()
    assert hits == 0


def test_descent_2():
    hit_map = [
        '.........'
        , '...#.....'
        , '......#..'
        , '#........'
    ]
    p = day03a.Slope(hit_map)
    hits = p.descent()
    assert hits == 3


def test_scenario():
    slope_map = utils.read_file("data/test_day3.txt")
    p = day03a.Slope(slope_map)
    hits = p.descent()
    assert hits == 7


def test_scenario_2():
    slope_map = utils.read_file("data/test_day3.txt")
    hit_list = [day03a.Slope(slope_map, move_col=scenario[0], move_row=scenario[1]).descent() for scenario in
                [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    assert hit_list == [2, 7, 3, 4, 2]


def test_scenario_2():
    slope_map = utils.read_file("data/test_day3.txt")
    hit_list = [day03a.Slope(slope_map, move_col=scenario[0], move_row=scenario[1]).descent() for scenario in
                [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    assert hit_list == [2, 7, 3, 4, 2]
    assert reduce((lambda x, y: x * y), hit_list) == 336
