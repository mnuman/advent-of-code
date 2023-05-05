import day9

"""
10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305
"""


def test_10p_last_1618():
    assert day9.day9(players=10, max_marble=1618) == 8317


def test_13p_last_7999():
    assert day9.day9(players=13, max_marble=7999) == 146373


def test_17p_last_1104():
    assert day9.day9(players=17, max_marble=1104) == 2764


def test_21p_last_6111():
    assert day9.day9(players=21, max_marble=6111) == 54718


def test_30p_last_5807():
    assert day9.day9(players=30, max_marble=5807) == 37305
