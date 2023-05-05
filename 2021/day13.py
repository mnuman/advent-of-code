import re
import utils


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return True if self.x < other.x or (self.x == other.x and self.y < other.y) else False

    def fold(self, fold_spec):
        """"
        Folding is not like mirroring ! If x > a, then the fold has NO effect. Otherwise, x' = 2a - x
        """
        fold_coord = fold_spec[1]
        if fold_spec[0] == "x":
            if self.x > fold_coord:
                self.x = 2 * fold_coord - self.x
        else:
            if self.y > fold_coord:
                self.y = 2 * fold_coord - self.y


def readfile(filename):
    lines = utils.read_file(filename)
    dots = []
    folds = []
    for line in lines:
        if "," in line:
            r, c = re.match(r"(\d+),(\d+)", line).groups()
            dots.append(Point(int(r), int(c)))
        elif line != '':
            xy, m = re.match(r"fold along ([xy])=(\d+)", line).groups()
            folds.append((xy,int(m)))
    return dots, folds

def draw_dots(dots):
    max_x = max(d.x for d in dots)+1
    max_y = max(d.y for d in dots)+1
    grid = [['.' for x in range(max_x)] for y in range(max_y)]
    for d in dots:
        grid[d.y][d.x] = '#'
    display = []
    for i in range(len(grid)):
        display.append(''.join(grid[i]))
    return display

def part1(filename):
    dots, folds = readfile(filename)
    for d in dots:
        d.fold(folds[0])
    return len(set(dots))


def part2(filename):
    dots, folds = readfile(filename)
    for f in folds:
        for d in dots:
            d.fold(f)
    return draw_dots(set(dots))


if __name__ == '__main__':
    day13_1 = part1("data/day-13.txt")
    print("Day 13 - part 1", day13_1)
    day13_2 = part2("data/day-13.txt")
    print("Day 13 - part 2\n")
    for line in day13_2:
        print(line)
