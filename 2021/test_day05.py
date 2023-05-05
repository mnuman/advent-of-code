import day05


def test_readfile():
    vent_list = day05.read_file("data/test-day-05.txt")
    assert len(vent_list) == 10, "List contains correct number of entries"
    assert vent_list[0] == ((0, 9), (5, 9)), "Entry is  correctly parsed into a tuple of coordinate pairs"


def test_is_horizontal_vent():
    assert day05.is_horizontal_vent(((0, 0), (2, 0)))
    assert not day05.is_horizontal_vent(((0, 0), (1, 2)))


def test_is_vertical_vent():
    assert day05.is_vertical_vent(((0, 0), (0, 2)))
    assert not day05.is_vertical_vent(((0, 0), (1, 2)))


def test_vent_eligible():
    assert day05.vent_eligible(((0, 0), (2, 0)), [day05.is_horizontal_vent])
    assert day05.vent_eligible(((0, 0), (2, 0)), [day05.is_vertical_vent, day05.is_horizontal_vent])
    assert not day05.vent_eligible(((0, 0), (2, 0)), [day05.is_vertical_vent])
    assert day05.vent_eligible(((0, 0), (2, 0)), [])


def test_vent_trajectory_v1():
    assert day05.vent_trajectory_v1(((0, 0), (2, 0))) == [(0, 0), (1, 0), (2, 0)]
    assert day05.vent_trajectory_v1(((2, 1), (2, 0))) == [(2, 0), (2, 1)]


def test_part1():
    result = day05.part1("data/test-day-05.txt")
    assert result[0] == 5


def test_vent_trajectory_v2():
    assert day05.vent_trajectory_v2(((0, 0), (2, 0))) == [(0, 0), (1, 0), (2, 0)]
    assert day05.vent_trajectory_v2(((2, 1), (2, 0))) == [(2, 0), (2, 1)]
    assert day05.vent_trajectory_v2(((1, 1), (3, 3))) == [(1, 1), (2, 2), (3, 3)]
    assert day05.vent_trajectory_v2(((7, 9), (9, 7))) == [(7, 9), (8, 8), (9, 7)]


def test_part2():
    result = day05.part2("data/test-day-05.txt")
    assert result[0] == 12
