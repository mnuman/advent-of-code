import day8


def test_read_file():
    s = day8.readfile('data/day8-test.txt')
    assert len(s) == 16
    assert s[4] == 10


def test_process_node():
    s = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    day8.all_nodes = []
    day8.process_node(0, s)
    assert len(day8.all_nodes) == 4
    assert len(day8.all_nodes[0].metadata) == 3
    assert day8.all_nodes[0].metadata == [1, 1, 2]
    assert day8.all_nodes[0].parent is None
    assert day8.all_nodes[1].metadata == [10, 11, 12]
    assert day8.all_nodes[1].id == 1
    assert day8.all_nodes[1].parent.id == 0


def test_day8():
    day8.all_nodes = []
    res = day8.day8('data/day8-test.txt')
    assert res == 138


def test_day8_2():
    day8.all_nodes = []
    day8.day8_2('data/day8-test.txt')
    assert len(day8.all_nodes) == 4
    assert len(day8.all_nodes[0].children) == 2
    assert day8.all_nodes[1].value() == 33
    assert day8.all_nodes[2].value() == 0
    assert day8.all_nodes[3].value() == 99
    assert day8.all_nodes[0].value() == 66
