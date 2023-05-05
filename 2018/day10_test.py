import day10


def test_read_file():
    p = day10.readfile('data/day10-test.txt')
    assert len(p) == 31
    assert p[0] == [9, 1, 0, 2]


def test_move_single():
    points = [[0, 0, 1, 1]]
    day10.move(points)
    assert points == [[1, 1, 1, 1]]


def test_move_multiple():
    points = [[1, -5, 2, 4]]
    day10.move(points, 10)
    assert points == [[21, 35, 2, 4]]


def test_display():
    points = day10.readfile('data/day10-test.txt')
    day10.move(points, 3)
    viewport = day10.viewport(points)
    print(viewport)
    assert viewport == ['*   *  ***          ', '*   *   *           ', '*   *   *           ', '*****   *           ', '*   *   *           ', '*   *   *           ', '*   *   *           ', '*   *  ***          ', '                    ', '                    ',
                        '                    ', '                    ', '                    ', '                    ', '                    ', '                    ', '                    ', '                    ', '                    ', '                    ']
