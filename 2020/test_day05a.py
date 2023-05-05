import day05a


def test_seatposition():
    assert day05a.seatposition("BFFFBBFRRR") == (70, 7)
    assert day05a.seatposition("FFFBBBFRRR") == (14, 7)
    assert day05a.seatposition("BBFFBBFRLL") == (102, 4)


def test_seat_number():
    assert day05a.seat_number((70, 7)) == 567
    assert day05a.seat_number((14, 7)) == 119
    assert day05a.seat_number((102, 4)) == 820
