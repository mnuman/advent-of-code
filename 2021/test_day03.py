import day03
import utils


def test_rate():
    data = utils.read_file("data/test-day-03.txt")
    assert len(data) == 12, "Report should contain 8 lines"
    value = day03.rate(data, day03.compare_lower_threshold)
    assert value == "10110"


def test_compare_lower_threshold():
    assert day03.compare_lower_threshold(1, 2) is True
    assert day03.compare_lower_threshold(1, 1) is False


def test_part1():
    assert day03.part1("data/test-day-03.txt") == 198, "9 x 22 = 198"


def test_find_filter_value():
    assert day03.find_filter_value(True, 10, 10) == '1'
    assert day03.find_filter_value(True, 10, 9) == '0'
    assert day03.find_filter_value(False, 10, 10) == '0'
    assert day03.find_filter_value(False, 10, 9) == '1'


def test_prune_report():
    report = ['00', '01', '10', '11']
    assert day03.prune_report(report, 0, '0') == ['00', '01']
    assert day03.prune_report(report, 0, '1') == ['10', '11']
    assert day03.prune_report(report, 1, '0') == ['00', '10']
    assert day03.prune_report(report, 1, '1') == ['01', '11']


def test_part2():
    assert day03.part2("data/test-day-03.txt") == 230, "23 x 10 = 230"
