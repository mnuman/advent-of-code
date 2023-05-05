from statistics import median

import utils


def read_file(filename: str) -> list[int]:
    return utils.read_file(filename, separator=",", convert=utils.toint)


def best_pos(all_crabs: list[int]) -> int:
    """The best position is the median position"""
    return round(median(all_crabs))


def fuel_cost(all_crabs: list[int], best_position: int) -> int:
    return sum([abs(best_position - crab_position) for crab_position in all_crabs])


def part1(filename: str) -> int:
    crab_positions = read_file(filename)
    best_position = best_pos(crab_positions)
    total_fuel_cost = fuel_cost(crab_positions, best_position)
    return best_position, total_fuel_cost


def increasing_cost(current: int, new: int) -> int:
    """Cost increases by one unit per step; hence moving n units will cost
    1+2+...+n =n(n+1)/2"""
    return abs(current - new) * (abs(current - new) + 1) // 2


def part2(filename: str) -> int:
    crab_positions = read_file(filename)
    costs = {}
    for test_position in range(min(crab_positions), max(crab_positions) + 1):
        costs[test_position] = sum([increasing_cost(crab_position, test_position) for crab_position in crab_positions])
    pos_min_costs = min(costs, key=costs.get)
    return pos_min_costs, costs[pos_min_costs]


if __name__ == '__main__':
    day07_1 = part1("data/day-07.txt")
    print("Day 07 - part 1", f"Best position {day07_1[0]}, total fuel cost {day07_1[1]}")
    day07_2 = part2("data/day-07.txt")
    print("Day 07 - part 2", f"Best position {day07_2[0]}, total fuel cost {day07_2[1]}")
