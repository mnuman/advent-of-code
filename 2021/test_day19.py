from day19 import *


def test_readfile():
    all_scanners = readfile("data/test-day-19.txt")
    assert len(all_scanners) == 5, "Five scanners read"
    assert len(all_scanners[0]) == 25, "First scanner sees 25  beacons"
