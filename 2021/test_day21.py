from day21 import *


def test_dirac_die():
    dd = DiracDie()
    for i in range(1, 101):
        assert dd.roll() == i, "Face value should equal iteration"
    assert dd.roll() == 1, "Must reset after 100"
    assert dd.number_of_rolls() == 101


def test_move():
    assert move(10, 1) == 1
    assert move(1, 10) == 1
    assert move(7, 4) == 1
    assert move(7, 33) == 10


def test_part1():
    result = part1(4, 8)
    print(result)
