import day17


def test_read_data():
    tbm = day17.read_data("test_day17.txt")
    assert tbm.A == 729
    assert tbm.B == 0
    assert tbm.C == 0
    assert tbm.outputs == []
    assert tbm.program == [0, 1, 5, 4, 3, 0]
    assert tbm.ip == 0


def test_machine_1():
    m = day17.ThreeBitMachine(0, 0, 9, [2, 6])
    m.run()
    assert m.B == 1


def test_machine_2():
    m = day17.ThreeBitMachine(10, 0, 0, [5, 0, 5, 1, 5, 4])
    m.run()
    assert m.outputs == [0, 1, 2]


def test_machine_3():
    m = day17.ThreeBitMachine(2024, 0, 0, [0, 1, 5, 4, 3, 0])
    m.run()
    assert m.A == 0
    assert m.outputs == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]


def test_machine_4():
    m = day17.ThreeBitMachine(0, 29, 0, [1, 7])
    m.run()
    assert m.B == 26


def test_machine_5():
    m = day17.ThreeBitMachine(0, 2024, 43690, [4, 0])
    m.run()
    assert m.B == 44354


def test_machine_6():
    pgm = [0, 3, 5, 4, 3, 0]
    m = day17.ThreeBitMachine(117440, 0, 0, pgm)
    m.run()
    assert m.outputs == pgm


def test_part1():
    tbm = day17.read_data("test_day17.txt")
    assert day17.part1(tbm) == "4,6,3,5,6,3,5,2,1,0"
