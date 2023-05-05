"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact,
it looks like you'll even have time to grab some food: all flights are
currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take to
enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example,
every faded blue bag is empty, every vibrant plum bag contains 11 bags (5
faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other
bag, how many different bag colors would be valid for the outermost bag? (In
other words: how many colors can, eventually, contain at least one shiny gold
bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly. A muted yellow bag,
    which can hold your shiny gold bag directly, plus some other bags. A dark orange bag,
    which can hold bright white and muted yellow bags, either of which could then hold your shiny
    gold bag. A light red bag, which can hold bright white and muted yellow bags, either of which
    could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold
bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite
long; make sure you get all of it.)
"""
import utils
import re

BAG_RULE_LIMITS = {}


def parse_rule_file(filename):
    result = {}
    f = utils.read_file(filename)
    for line in f:
        reg_match = re.match(r"^(.+) bags contain (.+)\.$", line)
        container_key = reg_match.group(1)
        # Append to existing container if it already exists
        container_contents = result[container_key] if container_key in result else {}
        for entry in reg_match.group(2).split(","):
            match_entry = re.match(r"^\s*(\d+) ([\w\s]+) bags?$", entry)
            if match_entry is not None and len(match_entry.groups()) == 2:
                contained_colour = match_entry.group(2)
                if contained_colour:
                    max_contained_qty = int(match_entry.group(1))
                    container_contents[contained_colour] = max_contained_qty
        if container_contents.keys():
            result[container_key] = container_contents
    return result


def can_contain_directly(rules_dict, bag_colour):
    """Which bag colors can contain the given bag color directly?"""
    return [bag for bag in rules_dict if bag_colour in rules_dict[bag]]


def recursive_contain(rules_dict, bag_colour, contained_by=None):
    if contained_by is None:
        contained_by = set()
    continue_search = True
    while continue_search:
        continue_search = False
        for colour in can_contain_directly(rules_dict, bag_colour):
            if colour not in contained_by:
                contained_by.add(colour)
                recursive_contain(rules_dict, colour, contained_by)
                continue_search = True
    return contained_by


if __name__ == '__main__':
    search_colour = "shiny gold"
    f = parse_rule_file("data/day07.txt")
    containers = recursive_contain(f, search_colour)
    print(f"A {search_colour} coloured bag can be contained in {len(containers)} different bag "
          f"colours:\n {containers}")
