import utils
import re

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def parse_passports(fname):
    passport_list = utils.read_file(fname)
    all_passports = []
    passport = {}
    for line in passport_list:
        if len(line) > 0:
            props = {keyval.split(':')[0]: keyval.split(':')[1] for keyval in line.split(' ')}
            passport = {**passport, **props}  # standard python idiom for merging two dicts
        else:  # next passport
            all_passports.append(passport)
            passport = {}
    else:  # if the file does not end with a blank line, still push the last passport to the list
        if passport not in all_passports:
            all_passports.append(passport)

    return all_passports


def passport_has_required_fields(passport):
    return all(field in passport for field in REQUIRED_FIELDS)


def validate_hgt(h):
    if h is None:
        return False
    m = re.match('^(\\d{2,3})([ci][mn])$', h)
    if m is not None:
        if len(m.groups()) == 2:
            if m.group(2) == 'cm':
                return '150' <= m.group(1) <= '193'
            elif m.group(2) == 'in':
                return '59' <= m.group(1) <= '76'
            else:
                return False
        else:
            return False
    else:
        return False


def passport_is_valid(passport):
    """ Additional requirements on passport:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.

    """
    byr, iyr, eyr, hgt, hcl, ecl, pid = passport['byr'], passport['iyr'], passport['eyr'], passport['hgt'], passport[
        'hcl'], passport['ecl'], passport['pid']
    return len(byr) == 4 and '1920' <= byr <= "2002" and \
           len(iyr) == 4 and '2010' <= iyr <= "2020" and \
           len(eyr) == 4 and '2020' <= eyr <= "2030" and \
           re.match('^#[a-f0-9]{6}$', hcl) is not None and \
           validate_hgt(hgt) and \
           ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
           re.match('^\\d{9}$', pid) is not None


if __name__ == "__main__":
    passports = parse_passports('data/day04.txt')
    valid = 0
    for p in passports:
        if passport_has_required_fields(p):
            valid += 1
    print(f"We have found {valid} valid passports")
