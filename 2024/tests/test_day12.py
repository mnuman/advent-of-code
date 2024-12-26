import day12


def test_read_data():
    data = day12.read_data("test_day12.txt")
    assert len(data) == len(data[0]) == 10


def test_part1():
    data = day12.read_data("test_day12.txt")
    assert day12.part1(data) == 1930


def test_part2():
    data = day12.read_data("test_day12.txt")
    assert day12.part2(data) == 1206


def test_count_sides_simple():
    region = {(0, 0), (0, 1)}
    assert day12.count_sides(region) == 4


def test_count_sides_complex_1():
    """ "
    C
    C C
      C
    """
    region = {(1, 2), (2, 2), (2, 3), (3, 3)}
    assert day12.count_sides(region) == 8


def test_count_sides_complex_2():
    region = {
        (7, 4),
        (6, 2),
        (7, 1),
        (9, 3),
        (8, 1),
        (6, 4),
        (7, 3),
        (8, 3),
        (7, 2),
        (8, 2),
        (7, 5),
        (6, 3),
        (8, 5),
        (5, 2),
    }
    assert day12.count_sides(region) == 16
