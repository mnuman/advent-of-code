import day2_1


def test_unique():
    t, d = day2_1.box_analyzer('abcdef')
    assert t == 0 and d == 0


def test_2_3():
    t, d = day2_1.box_analyzer('aabcdeefe')
    assert t == 1 and d == 1


def test_2_only():
    t, d = day2_1.box_analyzer('aabcdfe')
    assert t == 1 and d == 0


def test_3_only():
    t, d = day2_1.box_analyzer('abcdeefeff')
    assert t == 0 and d == 1


def test_box_analyzer():
    t, d, p = day2_1.analyze_all_boxes('data/day2-test.txt')
    assert t == 2
    assert d == 3
    assert p == 6
