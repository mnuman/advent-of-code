import day10a
import day10b
import utils

TEST_JOLTAGES = [9, 7, 5, 4, 3, 2, 1]


def test_build_next_dict():
    d = day10b.build_next_dict(TEST_JOLTAGES)
    assert d[0] == [1, 2, 3]
    assert d[1] == [2, 3, 4]
    assert d[4] == [5, 7]
    assert d[9] == []


def test_build_tree():
    # adapters = 1, 2, 3, 4, 6
    d = {0: [1, 2, 3], 1: [2, 3, 4], 2: [3, 4], 3: [4, 6], 4: [6], 6: []}
    assert day10b.build_tree({0: 1}, d) == {1: 1, 2: 1, 3: 1}
    assert day10b.build_tree({2: 1, 3: 1, 4: 2}, d) == {3: 1, 4: 2, 6: 3}


def test_counts_paths():
    adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert day10b.counts_paths(adapters) == 8


def test_scenario():
    adapters = day10a.sort_adapters(
        utils.read_file("data/test_day10.txt", convert=int))
    assert day10b.counts_paths(adapters) == 19208
