import file_utils as f
import parse
from functools import reduce
from operator import mul
from copy import deepcopy


class Robot:
    wide = 0
    tall = 0

    def __init__(self, state):
        self.px = state["px"]
        self.py = state["py"]
        self.vx = state["vx"]
        self.vy = state["vy"]

    def position(self, t):
        self.px = (self.px + t * self.vx) % self.wide
        self.py = (self.py + t * self.vy) % self.tall
        return self.px, self.py

    def quadrant(self):
        if self.px == self.wide // 2 or self.py == self.tall // 2:
            return None
        if self.px < self.wide // 2 and self.py < self.tall // 2:
            return 0
        if self.px > self.wide // 2 and self.py < self.tall // 2:
            return 1
        if self.px < self.wide // 2 and self.py > self.tall // 2:
            return 2
        return 3


def read_data(fname: str):
    return [
        Robot(parse.parse("p={px:d},{py:d} v={vx:d},{vy:d}", line))
        for line in f.read_file(fname)
    ]


def part1(data, wide=101, tall=103):
    Robot.wide = wide
    Robot.tall = tall
    quadrants = [0, 0, 0, 0]
    for robot in data:
        robot.position(100)
        q = robot.quadrant()
        if q is not None:
            quadrants[q] += 1
    return reduce(mul, quadrants, 1)


def part2(data, wide=101, tall=103):
    Robot.wide = wide
    Robot.tall = tall
    steps = 0
    # assuming all robots need to have *unique* positions to be aligned
    while True:
        steps += 1
        new_positions = [robot.position(1) for robot in data]
        # print(f"Step {steps}: unique positions: {len(set(new_positions))}")
        if len(set(new_positions)) == len(data):
            break
    # Visually verify the tree
    tree = [
        "".join(("*" if (x, y) in new_positions else " " for x in range(wide)))
        for y in range(tall)
    ]
    for y in range(tall):
        for x in range(wide):
            if (x, y) in new_positions:
                print("#", end="")
            else:
                print(".", end="")
        print()
    return steps, tree


if __name__ == "__main__":
    data = read_data("day14.txt")
    print(f"Part 1: {part1(deepcopy(data))}")
    steps, tree = part2(deepcopy(data))
    print(f"Part 2: {steps}")
    for line in tree:
        print(line)
