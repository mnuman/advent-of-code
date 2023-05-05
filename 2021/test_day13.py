from day13 import *


def test_readfile():
    p, f = readfile("data/test-day-13.txt")
    assert len(p) == 18, "Test data contains 18 points"
    assert len(f) == 2, "Test data contains 2 folds"
    assert sorted(f) == sorted([("y", 7), ("x", 5)]), "Folds are correctly read"


def test_point_fold():
    p = Point(5,7)
    p.fold(("x", 7))
    assert p.x == 5, "No effect if coordinate less than fold"
    assert p.y == 7, "Fold only works on a single coordinate"
    p.fold(("x", 2))
    assert p.x == -1, "Distance is mirrored"



def test_object_equality():
    p1 = Point(0,0)
    p2 = Point(1,1)
    p3 = Point(0,0)

    assert p1 != p2, "Different coordinates result in different objects"
    assert id(p1) != id(p3) and p1 == p3, "Different objects are considered equal when having the same coordinates"
    assert len({p1,p2,p3}) == 2, "Only two unique objectss"


def test_part1():
    assert part1("data/test-day-13.txt") == 17
