from day07 import *


def test_part1():
    assert part1("test_day07_1.txt") == 6440


def test_part2():
    assert part2("test_day07_1.txt") == 5905


def test_extra_tests():
    assert part1("test_day07_2.txt") == 1343
    assert part2("test_day07_2.txt") == 1369


def test_rank_hand_type():
    assert rank_hand_type("AAAAA") == 7
    assert rank_hand_type("ABBBB") == 6
    assert rank_hand_type("AABBB") == 5
    assert rank_hand_type("AAABC") == 4
    assert rank_hand_type("AABBC") == 3
    assert rank_hand_type("AABCD") == 2
    assert rank_hand_type("ABCDE") == 1
    assert rank_hand_type("AJJJJ", jokers=False) == 6
    assert rank_hand_type("AJJJJ", jokers=True) == 7


def test_value_hand():
    assert value_hand("AAAAA") == 7 * 10**10 + 14 * (
        10**8 + 10**6 + 10**4 + 10**2 + 10**0
    )
    assert value_hand("23456") == 1 * 10**10 + (
        2 * 10**8 + 3 * 10**6 + 4 * 10**4 + 5 * 10**2 + 6 * 10**0
    )
    assert value_hand("AJJJJ", jokers=True) == 7 * 10**10 + 14 * 10**8 + (
        10**6 + 10**4 + 10**2 + 10**0
    )


def test_hand_score():
    assert hand_score("AAAAA") == 7 * 14**5 + 13 * (
        14**4 + 14**3 + 14**2 + 14**1 + 1
    )
    assert hand_score("JJJJJ") == 7 * 14**5 + 1 * (
        14**4 + 14**3 + 14**2 + 14**1 + 1
    )
    assert hand_score('9922J') == 5 * 14**5 + (
        9*14**4 + 9*14**3 + 2*14**2 + 2*14 + 1
    )
