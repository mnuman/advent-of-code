from day22 import *


def test_readfile():
    reboots = readfile("data/test-day-22.txt")
    assert len(reboots) == 22, "Correct number of instructions read"
    assert len(reboots[0]) == 7, "Correct number of elements in instruction"
    assert all([reboots[i][0] in ('on','off') for i in range(len(reboots))]), "All lines have valid states"
    assert all([isinstance(reboots[i][j], int) for i in range(len(reboots)) for j in range(1,7)]), "All lines six coordinates"


def test_part1():
    assert part1("data/test-day-22.txt") == 590784
