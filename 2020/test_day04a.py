import day04a
import utils


def test_parse_passports():
    passports = day04a.parse_passports('data/test_day04.txt')
    assert len(passports) == 4
    assert passports[0]['byr'] == '1937'


def test_passport_has_all_required_fields():
    p = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147',
         'hgt': '183cm'}
    assert day04a.passport_has_required_fields(p)


def test_passport_has_not_all_required_fields():
    p = {'ecl': 'gry', 'pid': '860033327', 'thiswaseyr': '2020', 'hcl': '#fffffd', 'byr': '1937'}
    assert not (day04a.passport_has_required_fields(p))


def test_scenario_1():
    passports = day04a.parse_passports('data/test_day04.txt')
    valid = 0
    for p in passports:
        if day04a.passport_has_required_fields(p):
            valid += 1
    assert valid == 2
