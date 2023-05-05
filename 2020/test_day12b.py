import day12a
import day12b
import utils


def test_current_position():
    f = day12b.Ferry()
    f.current_position() == (0, 0)


def test_current_waypoint():
    f = day12b.Ferry()
    f.current_waypoint() == (10, 1)


def test_r90_l270():
    f1 = day12b.Ferry()
    f2 = day12b.Ferry()
    f1.action("R90")
    f2.action("L270")
    assert f1.current_waypoint() == f2.current_waypoint()
    assert f1.current_waypoint() == (1, -10)


def test_r180():
    f1 = day12b.Ferry()
    f1.action("R180")
    assert f1.current_waypoint() == (-10, -1)


def test_f1_r180():
    f1 = day12b.Ferry()
    f1.action("F1")
    assert f1.current_waypoint() == (20, 2)
    assert f1.current_position() == (10, 1)
    f1.action("R180")
    assert f1.current_waypoint() == (0, 0)
    assert f1.current_position() == (10, 1)


def test_f10():
    f1 = day12b.Ferry()
    f1.action("F10")
    assert f1.current_position() == (100, 10)
    assert f1.current_waypoint() == (110, 11)


def test_r90_l90():
    f1 = day12b.Ferry()
    f1.action("R90")
    assert f1.current_waypoint() == (1, -10)
    f1.action("L90")
    assert f1.current_waypoint() == (10, 1)


def test_f1_r90_r90_r90_r90():
    f1 = day12b.Ferry()
    f1.action("F1")
    assert f1.current_position() == (10, 1)
    assert f1.current_waypoint() == (20, 2)
    f1.action("R90")
    assert f1.current_position() == (10, 1)
    assert f1.current_waypoint() == (11, -9)
    f1.action("R90")
    assert f1.current_position() == (10, 1)
    assert f1.current_waypoint() == (0, 0)
    f1.action("R90")
    assert f1.current_position() == (10, 1)
    assert f1.current_waypoint() == (9, 11)
    f1.action("R90")
    assert f1.current_position() == (10, 1)
    assert f1.current_waypoint() == (20, 2)


def test_scenario():
    instructions = utils.read_file("data/test_day12.txt")
    ferry = day12b.Ferry()
    for instruction in instructions:
        ferry.action(instruction)
    assert ferry.current_position() == (214, -72)
    assert ferry.current_waypoint() == (218, -82)
    assert day12a.manhattan_distance(*ferry.position) == 286
