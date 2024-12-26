import day05


def test_read_data():
    rules, prints = day05.read_data("test_day05.txt")
    assert len(rules.keys()) == 6
    assert len(prints) == 6


def test_in_order():
    prints = [75, 47, 61, 53, 29]
    nok_rules = {61: {47, 75}}
    no_rules = {}
    ok_rules = {61: {53, 29, 17}}
    assert day05.in_order(
        ok_rules, prints
    ), "Satisfied all rules should return in order"
    assert day05.in_order(no_rules, prints), "No rules should return in order"
    assert not day05.in_order(
        nok_rules, prints
    ), "Failed rule should return not in order"


def test_part1():
    rules, prints = day05.read_data("test_day05.txt")
    assert day05.part1(rules, prints) == 143


def test_part2():
    rules, prints = day05.read_data("test_day05.txt")
    assert day05.part2(rules, prints) == 123
