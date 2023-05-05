import day13b


def test_parse_list():
    schedule = day13b.parse_list('7,13,x,x,59,x,31,19')
    assert schedule == {0: 7, 1: 13, 4: 59, 6: 31, 7: 19}
