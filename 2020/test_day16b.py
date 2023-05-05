import day16b


def test_drop_invalid_tickets():
    tv = day16b.TicketValidator("data/test_day16.txt")
    assert len(tv.nearby_tickets) == 4
    tv.drop_invalid_tickets()
    assert len(tv.nearby_tickets) == 1


def test_match_rules_to_ticket_order():
    tv = day16b.TicketValidator("data/test_day16b.txt")
    tv.drop_invalid_tickets()
    assert tv.match_rules_to_ticket_order() == {0: 'row', 1: 'class', 2: 'seat'}
