import day12a
import utils


def test_manhattan_distance():
    assert day12a.manhattan_distance(0, 0) == 0
    assert day12a.manhattan_distance(1, 1) == 2
    assert day12a.manhattan_distance(-1, -1) == 2
    assert day12a.manhattan_distance(-1, -1, 1, 1) == 4


def test_init():
    f = day12a.Ferry()
    assert f.current_position() == (0, 0)
    assert f.current_direction() == (1, 0)


def test_move_r90():
    f = day12a.Ferry()
    f.action("R90")
    assert f.current_direction() == (0, -1)


def test_move_r180():
    f = day12a.Ferry()
    f.action("R180")
    assert f.current_direction() == (-1, 0)


def test_move_f10():
    f = day12a.Ferry()
    f.action("F10")
    assert f.current_direction() == (1, 0)
    assert f.current_position() == (10, 0)


def test_move_e10():
    f = day12a.Ferry()
    f.action("R180")
    f.action("E10")
    assert f.current_direction() == (-1, 0)
    assert f.current_position() == (10, 0)


def test_move_w10():
    f = day12a.Ferry()
    f.action("W10")
    assert f.current_position() == (-10, 0)


def test_move_n10():
    f = day12a.Ferry()
    f.action("N10")
    assert f.current_position() == (0, 10)


def test_move_s10():
    f = day12a.Ferry()
    f.action("S10")
    assert f.current_position() == (0, -10)


def test_scenario():
    instructions = utils.read_file("data/test_day12.txt")
    ferry = day12a.Ferry()
    for instruction in instructions:
        ferry.action(instruction)
    assert ferry.current_direction() == (0, -1)
    assert ferry.current_position() == (17, -8)
    assert day12a.manhattan_distance(*ferry.current_position()) == 25
