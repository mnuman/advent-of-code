import day21


def test_read_data():
    data = day21.read_data("test_day21.txt")
    assert len(data) == 5


def test_code_value():
    assert day21.code_value("029A") == 29
    assert day21.code_value("980A") == 980
    assert day21.code_value("179A") == 179
    assert day21.code_value("456A") == 456
    assert day21.code_value("379A") == 379


def test_get_path_length():
    assert day21.get_path_length("029A", 3, True) == 68
    assert day21.get_path_length("980A", 3, True) == 60
    assert day21.get_path_length("179A", 3, True) == 68
    assert day21.get_path_length("456A", 3, True) == 64
    assert day21.get_path_length("379A", 3, True) == 64


def test_part1():
    data = day21.read_data("test_day21.txt")
    assert day21.part1(data) == 126384


def test_part2():
    pass  # no test value for second scenario
