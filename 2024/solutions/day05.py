from collections import defaultdict
from typing import Tuple
import file_utils as f


def read_data(fname: str) -> Tuple[dict[int, set[int]], list[str]]:
    """
    Read and parse the input file; return two items. The first is the dictionary of
    rules, which is returned with the key = before page, the value is the set of
    pages that *must* come after that page. The second item
    is the ordered list of pages to be printed.
    """
    rules = defaultdict(set)
    prints = []
    target = "rules"

    for line in f.read_file(filename=fname):
        if line != "":
            if target == "rules":
                before, after = line.split("|")
                rules[int(before)].add(int(after))
            else:
                prints.append(list(map(int, line.split(","))))
        else:
            target = "prints"
    return rules, prints


def in_order(rules: dict[int, set[int]], prints: list[int]) -> bool:
    """
    Given the rules and the list of pages to print, determine if the pages
    are in the correct order.
    """
    for idx, page in enumerate(prints):
        if page in rules:
            previous_pages = prints[:idx]
            must_print_after = rules[page]
            if any([p in must_print_after for p in previous_pages]):
                return False
    return True


def part1(rules: dict[int, set[int]], prints: list[int]) -> int:
    in_order_prints = list(filter(lambda x: in_order(rules, x), prints))  # type: ignore
    return sum(p[len(p) // 2] for p in in_order_prints)  # type: ignore


def order_print(rules: dict[int, set[int]], prints: list[int]) -> list[int]:
    """
    Given the rules and the list of pages to print, determine the correct order
    """
    print_first = defaultdict(set)
    pages_to_print = set(prints)
    for b, a in rules.items():
        for page in a:
            if page in pages_to_print and b in pages_to_print:
                print_first[page].add(b)
    ordered = []
    while pages_to_print:
        unconstrained_pages = [
            page for page in pages_to_print if page not in print_first
        ]
        # assuming deterministic ordering - just a single page in unconstrained_pages
        assert len(unconstrained_pages) == 1
        current_page = unconstrained_pages[0]
        ordered.append(current_page)
        for key in print_first.keys():
            if current_page in print_first[key]:
                print_first[key].remove(current_page)
        print_first = {k: v for k, v in print_first.items() if v}
        pages_to_print.remove(current_page)
    return ordered


def part2(rules: dict[int, set[int]], prints: list[int]) -> int:
    out_of_order_prints = list(
        filter(lambda x: not in_order(rules, x), prints)
    )  # type: ignore
    ordered_prints = [order_print(rules, p) for p in out_of_order_prints]
    return sum(p[len(p) // 2] for p in ordered_prints)  # type: ignore


if __name__ == "__main__":
    rules, prints = read_data("day05.txt")
    print(part1(rules, prints))
    print(part2(rules, prints))
