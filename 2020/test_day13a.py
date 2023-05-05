import day13a

TIMESTAMP = 939
BUSES = '7,13,x,x,59,x,31,19'


def test_parse_schedule():
    assert day13a.determine_schedule(TIMESTAMP, BUSES) == (944, 59)


def test_calc_product():
    assert day13a.calc_product(TIMESTAMP, BUSES) == 295
