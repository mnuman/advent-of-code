import day16


def test_part1():
    s, e, g = day16.parse_data_from_file("test_day16.txt")
    min_cost, _ = day16.dijkstra(s, e, g)
    assert min_cost == 7036


def test_part2():
    s, e, g = day16.parse_data_from_file("test_day16.txt")
    _, number_of_nodes = day16.dijkstra(s, e, g)
    assert number_of_nodes == 45
