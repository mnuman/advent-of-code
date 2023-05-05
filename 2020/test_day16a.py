import day16a


def test_read_file():
    rules, my_ticket, other_tickets = day16a.read_file("data/test_day16.txt")
    assert len(rules) == 3
    assert rules['class'] == [(1, 3), (5, 7)]

    assert my_ticket == [7, 1, 14]
    assert len(other_tickets) == 4


def test_check_in_any_range():
    tv = day16a.TicketValidator("data/test_day16.txt")
    assert not tv.check_in_any_range(4)
    assert not tv.check_in_any_range(12)
    assert tv.check_in_any_range(7)
    assert tv.check_in_any_range(50)


def test_validate_tickets():
    tv = day16a.TicketValidator("data/test_day16.txt")
    assert tv.validate_tickets() == 71
