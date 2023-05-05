import day5


def test_nonreducable_identical():
    assert day5.reducable('a', 'a') == False


def test_nonreducable_different():
    assert day5.reducable('a', 'b') == False


def test_reducable_mixed_case():
    assert day5.reducable('a', 'A') == True


def test_reducable_mixed_case_inverted():
    assert day5.reducable('A', 'a') == True


def test_reduce_possible():
    s = 'aBb'
    assert day5.reduce(s) == 'a'


def test_repeated_reduced():
    s = 'aBbBbAa'
    assert day5.reduce(s) == 'a'


def test_example():
    s = 'dabAcCaCBAcCcaDA'
    assert day5.reduce(s) == 'dabCBAcaDA'
