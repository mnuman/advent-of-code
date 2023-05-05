import day18a


def test_parse_input():
    assert day18a.parse_input('1*2+3/4') == [1, '*', 2, '+', 3, '/', 4]
    assert day18a.parse_input('100*((1+2)*3)') == \
           [100, '*', '(', '(', 1, '+', 2, ')', '*', 3, ')']
