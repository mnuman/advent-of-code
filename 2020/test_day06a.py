import day06a


def test_group_answers():
    groups = day06a.group_answers("data/test_day06.txt")
    assert len(groups) == 5  # five groups
    assert len(groups[0]) == 1
    assert len(groups[1]) == 3
    assert len(groups[2]) == 2
    assert len(groups[3]) == 4
    assert len(groups[4]) == 1


def test_unique_answers():
    groups = day06a.group_answers("data/test_day06.txt")
    assert day06a.unique_answers(groups[0]) == {'a', 'b', 'c'}
    assert day06a.unique_answers(groups[1]) == {'a', 'b', 'c'}
    assert day06a.unique_answers(groups[2]) == {'a', 'b', 'c'}
    assert day06a.unique_answers(groups[3]) == {'a'}
    assert day06a.unique_answers(groups[4]) == {'b'}


def test_scenario():
    groups = day06a.group_answers("data/test_day06.txt")
    assert sum([len(day06a.unique_answers(group)) for group in groups]) == 11
