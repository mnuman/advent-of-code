import day08


def test_read_file():
    data = day08.read_file("data/test-day-08.txt")
    assert len(data) == 10, "Test file contains 10 lines"
    assert data[9] == "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"


def test_tokenize_lines():
    result = day08.tokenize_lines(['|a b c a a ab', '|   a b c a a ba'])
    assert result == {'a': 6, 'b': 2, 'c': 2, 'ab': 2}, "Correct tokenization and aggregation"


def test_part1():
    result = day08.part1("data/test-day-08.txt")
    assert sum(list(result)) == 26, "Numbers 1,4 ,7 & 8 occur 26 times in total"


def test_fingerprint():
    assert day08.fingerprint("", []) == ''
    assert day08.fingerprint("a", ["a", " abc", "ddd"]) == "011"
    assert day08.fingerprint("ab", ["a", " abc", "ddd"]) == "012"


def test_interpret_display():
    wiring = ("acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab")
    display = ("cdfeb", "fcadb", "cdfeb", "cdbaf")
    assert day08.interpret_display(wiring, display) == 5353, "Interpretation of 5353"


def test_part2():
    assert day08.part2("data/test-day-08.txt") == 61229, "Test data should result in 61229"
