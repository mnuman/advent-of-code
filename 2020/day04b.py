import day04a

if __name__ == "__main__":
    passports = day04a.parse_passports('data/day04.txt')
    valid = 0
    for p in passports:
        if day04a.passport_has_required_fields(p) and day04a.passport_is_valid(p):
            valid += 1
    print(f"We have found {valid} valid passports")
