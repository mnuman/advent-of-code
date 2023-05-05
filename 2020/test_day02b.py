import utils, day02b


def test_verify_password():
    assert day02b.verify_password("bab", day02b.Policy(1, 3, 'a')) == False
    assert day02b.verify_password("aab", day02b.Policy(1, 3, 'a')) == True
    assert day02b.verify_password("baa", day02b.Policy(1, 3, 'a')) == True
    assert day02b.verify_password("aaa", day02b.Policy(1, 3, 'a')) == False


def test_find_matches():
    assert day02b.find_matches("data/test_day02a.txt") == 1