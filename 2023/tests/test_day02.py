from day02 import parse_line, is_possible, part1, part2
import file_utils as u


def test_parse_line():
    s = "Game 42: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_id, turns = parse_line(s)
    assert game_id == 42
    assert len(turns) == 3
    assert turns == [
        {"blue": 3, "red": 4},
        {"green": 2, "blue": 6, "red": 1},
        {"green": 2},
    ]


def test_is_possible():
    assert is_possible(
        [{"blue": 14, "red": 12}, {"green": 2, "blue": 6, "red": 1}, {"green": 2}]
    )
    assert not (is_possible([{"blue": 3, "black": 4}])), "Black not present in colours"
    assert not (is_possible([{"blue": 3, "red": 54}])), "Not so many reds"
    assert not (is_possible([{"green": 8, "blue": 6, "red": 20}]))
    assert not (
        is_possible([{"blue": 14, "red": 12}, {"green": 8, "blue": 6, "red": 20}])
    )


def test_part1():
    assert part1("test_day02_1.txt") == 8


def test_part2():
    assert part2("test_day02_1.txt") == 2286
