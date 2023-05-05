import day4
import re

s1 = '[1518-10-29 00:52] falls asleep'
s2 = '[1518-06-01 23:53] Guard #101 begins shift'
s3 = '[1518-07-31 00:35] wakes up'


def test_splitfields():
    assert day4.splitfields(s1) == ('1518-10-29', '00:52', 'S')
    assert day4.splitfields(s2) == ('1518-06-01', '23:53', '101')
    assert day4.splitfields(s3) == ('1518-07-31', '00:35', 'W')


def test_read_files():
    f = day4.prepare_data('data/day4-test.txt')
    assert len(f) == 5
    # make sure rows are sorted
    for i in range(1, 5):
        assert (f[i - 1][0] + f[i - 1][1]) <= (f[i][0] + f[i][1])
        assert (f[i][2] in ['S', 'W'] or re.match(r'\d+', f[i][2]))
    assert f[3][2] == '1627'


def test_sleeper():
    s = day4.sleeper(0, 5)
    assert len(s) == 60
    assert s[0] == '#'
    assert s[1] == '#'
    assert s[2] == '#'
    assert s[3] == '#'
    assert s[4] == '#'
    assert s[5] == '.'


def test_full_sleeper():
    s = day4.sleeper(0, 60)
    assert len(s) == 60
    assert s[59] == '#'
    assert '.' not in s


def test_parse_data():
    data = [
        ('1518-11-20', '23:59', '1627'),
        ('1518-11-21', '00:22', 'S'),
        ('1518-11-21', '00:50', 'W'),
        ('1518-11-21', '23:57', '827'),
        ('1518-11-23', '00:03', '743'),
        ('1518-11-23', '00:41', 'S'),
        ('1518-11-23', '00:42', 'W'),
        ('1518-11-23', '00:49', 'S'),
        ('1518-11-23', '00:52', 'W')
    ]
    parsed = day4.parse_data(data)
    assert len(parsed) == 2
    # only 1627 and 743 occur
    assert '1627' in parsed
    assert '743' in parsed
    assert '827' not in parsed
    # 1627 falls asleep on min 22, so 0-21 must be awake
    # awakens in min 50, so 22-49 must be '#'.
    # awakes 50-, so must be '.'
    res = ('.' * 22 + '#' * 28 + '.' * 10)
    assert parsed['1627'][0] == res

    assert parsed['743'][0][40] == '.'
    assert parsed['743'][0][41] == '#'  # only asleeop on min 41!
    assert parsed['743'][0][42] == '.'
    # three minutes of sleep again ...
    assert parsed['743'][1][48:53] == '.###.'


def test_most_minutes():
    data = [
        ('1518-11-20', '23:59', '1627'),
        ('1518-11-21', '00:22', 'S'),
        ('1518-11-21', '00:50', 'W'),
        ('1518-11-21', '23:57', '827'),
        ('1518-11-23', '00:03', '743'),
        ('1518-11-23', '00:41', 'S'),
        ('1518-11-23', '00:42', 'W'),
        ('1518-11-23', '00:49', 'S'),
        ('1518-11-23', '00:52', 'W')
    ]
    parsed = day4.select_most_minutes(day4.parse_data(data))
    assert parsed == '1627'


def test_mostly_in_minute():
    input_data = [
        ('1518-11-20', '23:59', '1627'),
        ('1518-11-21', '00:22', 'S'),
        ('1518-11-21', '00:50', 'W'),
        ('1518-11-21', '00:15', 'S'),
        ('1518-11-21', '00:23', 'W'),
        ('1518-11-21', '23:57', '827'),
        ('1518-11-23', '00:03', '743'),
        ('1518-11-23', '00:41', 'S'),
        ('1518-11-23', '00:42', 'W'),
        ('1518-11-23', '00:49', 'S'),
        ('1518-11-23', '00:52', 'W')
    ]
    data = day4.parse_data(input_data)
    guard = day4.select_most_minutes(data)
    assert guard == '1627'  # sleepy guard
    x = day4.select_minute(data, guard)
    assert x == (22, 2)  # beautifully crafted minute 22 occurring twice


def test_sleepiest_minute_same_guard():
    input_data = [
        ('1518-11-20', '23:59', '1627'),
        ('1518-11-21', '00:22', 'S'),
        ('1518-11-21', '00:50', 'W'),
        ('1518-11-21', '00:15', 'S'),
        ('1518-11-21', '00:23', 'W'),
        ('1518-11-21', '23:57', '827'),
        ('1518-11-23', '00:03', '743'),
        ('1518-11-23', '00:41', 'S'),
        ('1518-11-23', '00:42', 'W'),
        ('1518-11-23', '00:49', 'S'),
        ('1518-11-23', '00:52', 'W')
    ]
    data = day4.parse_data(input_data)
    x = day4.sleepiest_minute_same_guard(data)
    assert x['1627'][22] == 2


def test_find_sleepiest_minute():
    input_data = [
        ('1518-11-20', '23:59', '1627'),
        ('1518-11-21', '00:22', 'S'),
        ('1518-11-21', '00:50', 'W'),
        ('1518-11-21', '00:15', 'S'),
        ('1518-11-21', '00:23', 'W'),
        ('1518-11-21', '23:57', '827'),
        ('1518-11-23', '00:03', '743'),
        ('1518-11-23', '00:41', 'S'),
        ('1518-11-23', '00:42', 'W'),
        ('1518-11-23', '00:49', 'S'),
        ('1518-11-23', '00:52', 'W')
    ]
    data = day4.parse_data(input_data)
    x = day4.find_sleepiest_minute(day4.sleepiest_minute_same_guard(data))
    assert x[0] == '1627'
    assert x[1] == 22
    assert x[2] == 2
