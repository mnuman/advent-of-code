import day15a


def test_add_number():
    r = day15a.Recitation()
    assert r.ctr == 0
    assert r.seq == {}
    r.add_number(10)
    r.add_number(9)
    r.add_number(10)
    assert r.ctr == 3
    assert r.last == 10
    assert r.seq == {10: [1, 3], 9: [2]}


def test_start():
    r = day15a.Recitation()
    r.start((1, 2, 3))
    assert r.ctr == 3
    assert r.last == 3
    for i in (1, 2, 3):
        assert i in r.seq


def test_calc_next():
    r = day15a.Recitation()
    r.start((1, 2, 3))
    assert r.calc_next() == 0


def test_next():
    r = day15a.Recitation()
    r.start((1, 2, 3, 4))
    assert r.next() == 0
    assert r.next() == 0
    assert r.next() == 1
    assert r.next() == 6


def test_iterate():
    r = day15a.Recitation()
    r.start((0, 3, 6))
    assert r.iterate(2020) == 436


def test_scenarios():
    for (seq, val) in [((1, 3, 2), 1), ((2, 1, 3), 10), ((1, 2, 3), 27),
                       ((2, 3, 1), 78), ((3, 2, 1), 438), ((3, 1, 2), 1836)]:
        r = day15a.Recitation()
        r.start(seq)
        assert r.iterate(2020) == val
