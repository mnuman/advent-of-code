import day6


def test_manhattan_distance_p1_p2():
    # all variations must yield the same result!
    assert day6.manhattan_distance(10, 0, 0, 0) == 10
    assert day6.manhattan_distance(0, 10, 0, 0) == 10
    assert day6.manhattan_distance(0, 0, 10, 0) == 10
    assert day6.manhattan_distance(0, 0, 0, 10) == 10


def test_manhattan_distance_permuations():
    assert day6.manhattan_distance(1, 2, 8, 9) == 14
    assert day6.manhattan_distance(
        1, 2, 8, 9) == day6.manhattan_distance(8, 9, 1, 2)


def test_read():
    points = day6.read_points('data/day6-test.txt')
    assert len(points) == 6
    assert points[0] == (1, 1)
    assert points[5] == (8, 9)


def test_limits():
    # point = col,row
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]
    l = day6.limits(points)
    assert l[0] == 1  # mincol
    assert l[1] == 8  # maxcol
    assert l[2] == 1  # minrow
    assert l[3] == 9  # maxrow


def test_all_nearest():
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]
    nn = day6.walk_all(points, 10)
    assert len(nn) == 6
    assert len(nn[(3, 4)]) == 9
    assert len(nn[(5, 5)]) == 17


def test_filter():
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]
    nn = day6.walk_all(points, 10)
    day6.remove_edges(nn)
    assert len(nn) == 2
    assert len(nn[(3, 4)]) == 9
    assert len(nn[(5, 5)]) == 17


def test_most_neighbours():
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]
    nn = day6.walk_all(points, 10)
    assert day6.find_most_neighbours(nn) == 17
