import day02


def test_day02_get_data():
    data = day02.get_data("data/test-day-02-1.txt")
    assert len(data) == 6, "returned list should contain 6 action lines"
    assert data[0] == ("forward", "5"), "Data is parsed"


def test_day02_adjust_position():
    start = (0, 0, None)
    target = day02.adjust_position(start, ("forward", "5"))
    assert target == (5, 0, None), "Correct horizontal position"
    target = day02.adjust_position(start, ("down", "8"))
    assert target == (0, 8, None), "Correct depth position after diving"
    target = day02.adjust_position(start, ("up", "2"))
    assert target == (
        0, -2, None), "Correct depth position after going up - albeit strange"


def test_day01_1():
    data = day02.get_data("data/test-day-02-1.txt")
    final_pos = day02.process_instructions((0, 0, None), data)
    assert final_pos == (15, 10, None)


def test_day01_2():
    data = day02.get_data("data/test-day-02-1.txt")
    final_pos = day02.process_instructions((0, 0, 0), data)
    assert final_pos == (15, 60, 10)
