import utils, day02a


def test_parse_policy():
    pw_policy = "1-3 a: abcde"
    assert day02a.parse_policy(pw_policy) == (day02a.Policy(1, 3, 'a'), "abcde")

def test_verify_password():
    assert day02a.verify_password("", day02a.Policy(1, 3, 'a')) == False
    assert day02a.verify_password("bab", day02a.Policy(1, 3, 'a')) == True
    assert day02a.verify_password("baab", day02a.Policy(1, 3, 'a')) == True
    assert day02a.verify_password("caaac", day02a.Policy(1, 3, 'a')) == True
    assert day02a.verify_password("caaaac", day02a.Policy(1, 3, 'a')) == False

def test_find_matches():
    assert day02a.find_matches("data/test_day02a.txt") == 2