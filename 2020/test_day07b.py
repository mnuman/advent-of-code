import day07b

TEST_RULES = {
    "light red": {"bright white": 1, "muted yellow": 2},
    "dark orange": {"bright white": 3, "muted yellow": 4},
    "bright white": {"shiny gold": 1},
    "muted yellow": {"shiny gold": 2, "faded blue": 9},
    "shiny gold": {"dark olive": 1, "vibrant plum": 2},
    "dark olive": {"faded blue": 3, "dotted black": 4},
    "vibrant plum": {"faded blue": 5, "dotted black": 6}
}

TEST_RULES_7B = {'shiny gold': {'dark red': 2}, 'dark red': {'dark orange': 2},
                 'dark orange': {'dark yellow': 2}, 'dark yellow': {'dark green': 2},
                 'dark green': {'dark blue': 2}, 'dark blue': {'dark violet': 2}}


def test_recursive_bag_counter_end_bag():
    assert day07b.recursive_bag_counter(TEST_RULES, "dotted black") == 0


def test_recursive_bag_counter_vibrant_plum():
    assert day07b.recursive_bag_counter(TEST_RULES, "vibrant plum") == 11


def test_recursive_bag_counter_dark_olive():
    assert day07b.recursive_bag_counter(TEST_RULES, "dark olive") == 7


def test_recursive_bag_counter_shiny_gold():
    assert day07b.recursive_bag_counter(TEST_RULES, "shiny gold") == 32


def test_test_scenario_7b():
    assert day07b.recursive_bag_counter(TEST_RULES_7B, "shiny gold") == 126
