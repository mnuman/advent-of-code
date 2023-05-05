from collections.abc import Callable

import utils

DiagnosticReport = list[str]


def compare_lower_threshold(a: int, b: int) -> bool:
    return a < b


def compare_higher_threshold(a: int, b: int) -> bool:
    return compare_lower_threshold(b, a)


def rate(collection: DiagnosticReport,
         comparison_function: Callable[[int, int], bool]) -> str:
    """Given the diagnostic report (list of binary numbers represented as
        strings), calculated the gamma-rate: for each position, the most
        occurring value (either 0 or 1) is used.
    """
    threshold = len(collection)
    digits = ''
    for i in range(0, len(collection[0])):
        ones = sum([int(report[i]) for report in collection])
        digits += '1' if comparison_function(threshold / 2, ones) else '0'
    return digits


def rating(collection: DiagnosticReport, most_common: bool) -> str:
    """Iterate diagnostic report, implement bitwise filtering:
       1. for each bit, determine the number of '1's and '0' in that position
       2. if most_common, retain only the entries that have the MOST occurring
        value in that bit-position, otherwise retain the entries that have
        the LEAST occurring value in that position. Remove the other ones.
        When tied: for the most common prefer 1, least common prefer 0
       3. until only a single value remains
    """
    local_report = collection.copy()
    number_of_bits = len(local_report[0])
    for bit_number in range(0, number_of_bits):
        ones = sum([int(report[bit_number]) for report in local_report])
        zeroes = len(local_report) - ones
        filter_value = find_filter_value(most_common, zeroes, ones)
        local_report = prune_report(local_report, bit_number, filter_value)
        if len(local_report) == 1:
            break
    assert len(
        local_report) == 1, "Panic: procedure does not yield exactly one " \
                            "element"
    return local_report[0]


def prune_report(report: DiagnosticReport, bit_number: int,
                 bit_value: str) -> DiagnosticReport:
    """Filter the report to retain only the entries with the bit_value
    in bit_number"""
    return [rep for rep in report if rep[bit_number] == bit_value]


def find_filter_value(most_common: bool, zeroes: int, ones: int) -> str:
    """Implement filtering rules, i.e. determine on which value to filter"""
    if most_common:
        if ones >= zeroes:
            return '1'
        else:
            return '0'
    else:
        if ones >= zeroes:
            return '0'
        else:
            return '1'


def part2(filename):
    data = utils.read_file(filename)
    oxygen_generator_rating = rating(data, most_common=True)
    co2_scrubber_rating = rating(data, most_common=False)
    print(
        f"Ratings - oxygen {oxygen_generator_rating}, "
        f"co2 {co2_scrubber_rating}")
    return utils.binary_to_int(oxygen_generator_rating) * utils.binary_to_int(co2_scrubber_rating)


def part1(filename):
    data = utils.read_file(filename)
    gamma_rate = rate(data, compare_lower_threshold)
    epsilon_rate = rate(data, compare_higher_threshold)
    return utils.binary_to_int(gamma_rate) * utils.binary_to_int(epsilon_rate)


if __name__ == '__main__':
    day03_1 = part1("data/day-03.txt")
    print("Day 03 - part 1", day03_1)
    day03_2 = part2("data/day-03.txt")
    print("Day 03 - part 2", day03_2)
