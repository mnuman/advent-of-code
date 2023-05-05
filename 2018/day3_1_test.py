import day3_1


def test_array_init():
    a = day3_1.initialize(12)
    assert len(a) == 12
    for i in range(0, len(a)):
        assert len(a[i]) == 12


def test_fill_array_single_fill():
    a = day3_1.initialize(8)
    a = day3_1.fill_array(a, 1, 3, 4, 4)
    assert a[0] == [0, 0, 0, 0, 0, 0, 0, 0]
    assert a[1] == [0, 0, 0, 0, 0, 0, 0, 0]
    assert a[2] == [0, 0, 0, 0, 0, 0, 0, 0]
    assert a[3] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[4] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[5] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[6] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[7] == [0, 0, 0, 0, 0, 0, 0, 0]


def test_fill_array_multi_fill():
    a = day3_1.initialize(8)
    a = day3_1.fill_array(a, 1, 3, 4, 4)
    a = day3_1.fill_array(a, 3, 1, 4, 4)
    assert a[0] == [0, 0, 0, 0, 0, 0, 0, 0]
    assert a[1] == [0, 0, 0, 1, 1, 1, 1, 0]
    assert a[2] == [0, 0, 0, 1, 1, 1, 1, 0]
    assert a[3] == [0, 1, 1, 2, 2, 1, 1, 0]
    assert a[4] == [0, 1, 1, 2, 2, 1, 1, 0]
    assert a[5] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[6] == [0, 1, 1, 1, 1, 0, 0, 0]
    assert a[7] == [0, 0, 0, 0, 0, 0, 0, 0]


def test_find_overlaps():
    a = day3_1.initialize(8)
    a = day3_1.fill_array(a, 1, 3, 4, 4)
    a = day3_1.fill_array(a, 3, 1, 4, 4)
    assert day3_1.find_overlaps(a) == 4


def test_parse():
    x = day3_1.parse_instruction('#1295 @ 240,934: 29x28')
    assert x[0] == 1295
    assert x[1] == 240
    assert x[2] == 934
    assert x[3] == 29
    assert x[4] == 28


def test_read():
    f = day3_1.read_file('data/day3-test.txt')
    assert len(f) == 3
    assert f[0] == [1, 306, 433, 16, 11]
    assert f[1] == [2, 715, 698, 18, 29]


def test_non_overlap():
    array = day3_1.initialize(10)
    instructions = day3_1.read_file('data/day3-1-test.txt')
    for op in instructions:
        array = day3_1.fill_array(array, op[1], op[2], op[3], op[4])
    for op in instructions:
        if day3_1.find_non_overlapped(array, op):
            result = op
    print(op)
    assert result[0] == 3
