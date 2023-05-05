import re
from collections import namedtuple

import utils

Point = namedtuple("Point", ["x", "y", "z"])


def readfile(filename):
    data = utils.read_file(filename)
    reboot_sequence = []
    for line in data:
        state, xmin, xmax, ymin, ymax, zmin, zmax = re.match(
            r"^(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line).groups()
        reboot_sequence.append((state, int(xmin), int(xmax), int(ymin), int(ymax), int(zmin), int(zmax)))
    return reboot_sequence


def f(c):
    return -50 if c < -50 else 50 if c > 50 else c


def cuboids(x_min, x_max, y_min, y_max, z_min, z_max):
    if any([x in range(x_min, x_max + 1) for x in range(-50, 51)]) and any(
            [y in range(y_min, y_max + 1) for y in range(-50, 51)]) and any(
            [z in range(z_min, z_max + 1) for z in range(-50, 51)]):
        return [Point(x, y, z) for x in range(f(x_min), f(x_max) + 1) for y in range(f(y_min), f(y_max) + 1) for z in
                range(f(z_min), f(z_max) + 1)]
    else:
        return []


def part1(filename):
    reboot_sequence = readfile(filename)
    states = {}
    for state, xmin, xmax, ymin, ymax, zmin, zmax in reboot_sequence:
        affected_cuboids = cuboids(xmin, xmax, ymin, ymax, zmin, zmax)
        print(f"Affected cuboids: {len(affected_cuboids)}")
        for c in affected_cuboids:
            if state == 'on':
                states[c] = state
            elif c in states:
                states.pop(c)
            else:
                pass
    return len(states)


if __name__ == '__main__':
    part_1 = part1("data/day-22.txt")
    print("Day 22 - part 1", part_1)
    part_2 = None
    print("Day 22 - part 2", part_2)
