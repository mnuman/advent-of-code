from day18 import *


def test_snailfishnumber_value():
    a = SnailFishNumber(7, 8)
    assert a.value() == 37, "3*7 +2*8"
    b = SnailFishNumber(5, 6)
    assert b.value() == 27, "3*5 +2*6"

