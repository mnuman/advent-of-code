import day12


def test_readfile():
    caves = day12.readfile("data/test-day-12.txt")
    assert len(caves.keys()) == 6, "Six vertices present in test data"
    assert sum([len(caves[vertex]) for vertex in caves.keys()]) == 14, "Fourteen edges present - undirected graph"


def test_part1():
    assert day12.part1("data/test-day-12.txt") == 10, "Test data returns 10 unique paths"


def test_part2():
    assert day12.part2("data/test-day-12.txt") == 36, "Test data returns 36 unique paths"
