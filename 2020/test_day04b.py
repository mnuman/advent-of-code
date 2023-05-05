import day04a
import utils


def test_validate_hgt():
    assert not day04a.validate_hgt("149cm")
    assert not day04a.validate_hgt("49cm")
    assert not day04a.validate_hgt("58in")
    assert not day04a.validate_hgt("")
    assert not day04a.validate_hgt(None)
    assert not day04a.validate_hgt("0150cm")
    assert not day04a.validate_hgt("150cmm")
    assert day04a.validate_hgt("150cm")
    assert day04a.validate_hgt("193cm")
    assert day04a.validate_hgt("59in")
    assert day04a.validate_hgt("76in")


def test_scenario_1():
    passports = day04a.parse_passports('data/test_day04.txt')
    valid = 0
    for p in passports:
        if day04a.passport_has_required_fields(p) and day04a.passport_is_valid(p):
            valid += 1
    assert valid == 2
