import utils
import re
"""
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at
least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for
Santa's suit. All claims have an ID and consist of a single rectangle with
edges parallel to the edges of the fabric. Each claim's rectangle is defined
as follows:

The number of inches between the left edge of the fabric and the left edge
of the rectangle.
The number of inches between the top edge of the fabric and the top edge
of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle
3 inches from the left edge, 2 inches from the top edge, 5 inches wide,
and 4 inches tall. Visually, it claims the square inches of fabric represented
by # (and ignores the square inches of fabric represented by .) in the
diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to
 cover part of the same areas. For example, consider the following claims:

# 1 @ 1,3: 4x4
# 2 @ 3,1: 4x4
# 3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2.
(Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have
enough fabric. How many square inches of fabric are within two or more claims?
"""
"""Day3, part 2:
Amidst the chaos, you notice that exactly one claim doesn't overlap 
by even a single square inch of fabric with any other claim. If you 
can somehow draw attention to it, maybe the Elves will be able to make 
Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all 
claims are made.

What is the ID of the only claim that doesn't overlap?
"""
line_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def initialize(size):
    """Initialize a square of size x size """
    result = []
    for i in range(0, size):
        result.append([0]*size)
    return result


def fill_array(array, x, y, w, h):
    """Add value to the array, starting at
    x,y for a width w and height h
    If there is already a value append an element to the list
    """
    for i in range(x, x + w):
        for j in range(y, y + h):
            array[j][i] += 1
    return array


def find_overlaps(array):
    return sum([1 for i in range(0, len(array)) for j in range(0, len(array)) if array[i][j] > 1])


def parse_instruction(s):
    """format: #1295 @ 240,934: 29x28"""
    match = line_regex.match(s)
    g = match.groups()
    return [int(g[0]), int(g[1]), int(g[2]), int(g[3]), int(g[4])]


def read_file(fname):
    return utils.read_file(fname, convert=parse_instruction)


def find_non_overlapped(array, op):
    x0 = op[1]
    y0 = op[2]
    w = op[3]
    h = op[4]
    NonOverlapped = True
    for i in range(x0, x0 + w):
        for j in range(y0, y0 + h):
            if array[j][i] != 1:
                NonOverlapped = False
    return NonOverlapped


if __name__ == '__main__':
    array = initialize(2000)
    instructions = read_file('data/day3-input.txt')
    for op in instructions:
        array = fill_array(array, op[1], op[2], op[3], op[4])
    # 3 - part1
    # print(find_overlaps(array))
    # 105071
    # day3 part 2 - revisit the array to see which entry has NO
    # overlaps with any others, i.e. count of all entries is 1.
    for op in instructions:
        if find_non_overlapped(array, op):
            print(f"Found non-overlapping entry: {op[0]} - {str(op)}")
            break
