import day07a

TEST_RULES = {
    "light red": {"bright white": 1, "muted yellow": 2},
    "dark orange": {"bright white": 3, "muted yellow": 4},
    "bright white": {"shiny gold": 1},
    "muted yellow": {"shiny gold": 2, "faded blue": 9},
    "shiny gold": {"dark olive": 1, "vibrant plum": 2},
    "dark olive": {"faded blue": 3, "dotted black": 4},
    "vibrant plum": {"faded blue": 1, "dotted black": 6}
}


def test_can_contain_directly():
    # check the bags that can contain the given bag color
    assert day07a.can_contain_directly(TEST_RULES, "bright white") == ["light red", "dark orange"]


def test_parse_rule_file():
    # Verify file is parsed by checking the keys present
    rules = day07a.parse_rule_file("data/test_day07.txt")
    assert rules.keys() == {"light red", "dark orange", "bright white", "muted yellow",
                            "shiny gold", "dark olive", "vibrant plum"}


def test_parse_rule_checks():
    # Verify entries
    rules = day07a.parse_rule_file("data/test_day07.txt")
    assert rules["shiny gold"] == {"dark olive": 1, "vibrant plum": 2}
    assert "dotted black" not in rules


def test_all_containers_scenario_1():
    # which bag colours can contain a shiny gold bag (recursively)
    assert day07a.recursive_contain(TEST_RULES, "shiny gold") == {'muted yellow', 'bright white',
                                                                  'light red', 'dark orange'}
