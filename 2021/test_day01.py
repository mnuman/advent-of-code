import day01


def test_day01_get_data():
    data = day01.get_data("data/test-day-01-1.txt")
    assert len(data) == 10, "returned list should contain 10 data points"
    assert data == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263], \
        "Data order hasn't changed"


def test_count_next_is_greater():
    assert 0 == day01.count_next_is_greater(
        []), "Empty list yields 0"
    assert 2 == day01.count_next_is_greater(
        [1, 2, 3, 2]), "1,2,3,2 yields 2"
    assert 0 == day01.count_next_is_greater(
        [9, 8, 7, 7]), "9,8,7,7 yields 0"


def test_count_window_is_greater():
    assert 0 == day01.count_window_is_greater(
        []), "Empty list yields 0"
    assert 1 == day01.count_window_is_greater(
        [1, 2, 3, 2]), "1,2,3,2 yields 1"
    assert 0 == day01.count_window_is_greater(
        [9, 8, 7, 7]), "9,8,7,7 yields 0"


def test_day01_1():
    data = day01.get_data("data/test-day-01-1.txt")
    assert 7 == day01.count_next_is_greater(
        data), "Day01 - part 1 result is correct"


def test_day01_2():
    data = day01.get_data("data/test-day-01-1.txt")
    assert 5 == day01.count_window_is_greater(
        data), "Day01 - part 2 result is correct"
