import day06a
import day06b


def test_separate_answers():
    assert day06b.separate_answers(['abc']) == [['a', 'b', 'c']]
    assert day06b.separate_answers(['a', 'b', 'c']) == [['a'], ['b'], ['c']]


def test_intersect_answers():
    assert day06b.intersect_answers([['a', 'b', 'c']]) == 'abc'
    assert day06b.intersect_answers([['a'], ['b'], ['c']]) == ''
    assert day06b.intersect_answers([['a', 'b'], ['a', 'c']]) == 'a'


def test_scenario():
    groups = day06a.group_answers("data/test_day06.txt")
    separated_answers = day06b.separate_answers(groups)
    assert sum([len(day06b.intersect_answers(group)) for group in separated_answers]) == 6
