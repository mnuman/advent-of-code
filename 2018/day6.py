"""--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel
like you're falling.

"Situation critical," the device announces. "Destination indeterminate.
Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are
they places it thinks are safe or dangerous? It recommends you check
manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each
coordinate by counting the number of integer X,Y locations that are
closest to that coordinate (and aren't tied in distance to any other
coordinate).

Your goal is to find the size of the largest area that isn't infinite.
For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a
grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all
directions. Using the Manhattan distance, each location's closest
coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates,
and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite -
while not shown here, their areas extend forever outside the visible grid.
However, the areas of coordinates D and E are finite: D is closest to 9
locations, and E is closest to 17 (both including the coordinate's
location itself). Therefore, in this example, the size of the largest
area is 17.
What is the size of the largest area that isn't infinite?
"""
import utils
# coordinates are always taken as (col, row)


def line_to_point(line):
    elements = line.split(',')
    return (int(elements[0]), int(elements[1]))


def read_points(fname):
    return utils.read_file(filename=fname, convert=line_to_point)


def manhattan_distance(col1, row1, col2, row2):
    return abs(row1-row2) + abs(col1-col2)


def limits(points):
    """Return the limits to search"""
    _minrow = sorted(
        points, key=lambda p: p[1], reverse=False)[0][1]
    _maxrow = sorted(
        points, key=lambda p: p[1], reverse=True)[0][1]
    _mincol = sorted(
        points, key=lambda p: p[0], reverse=False)[0][0]
    _maxcol = sorted(
        points, key=lambda p: p[0], reverse=True)[0][0]
    return(_mincol, _maxcol, _minrow, _maxrow)


def walk_all(points, size):
    """Build for each point (c,r) a list of (col,row) where the point is
       the closest neighbour"""
    all_nearest_neighbours = {}
    for col in range(-10, size):
        for row in range(-10, size):
            distances = []
            for c, r in points:
                d = manhattan_distance(col, row, c, r)
                distances.append((d, c, r))
            # sort on the DISTANCE, e.g. element 0 of tuple
            distances = sorted(distances, key=lambda x: x[0], reverse=False)
            if distances[0][0] < distances[1][0]:
                p = (distances[0][1], distances[0][2])
                # if the next point is FURTHER away -> c,r is the closest to col,row!
                if p not in all_nearest_neighbours:
                    all_nearest_neighbours[p] = []
                all_nearest_neighbours[p].append((col, row))
    return all_nearest_neighbours


def remove_edges(nearest_neighbours):
    min_col = min([point[0] for point in nearest_neighbours.keys()])
    max_col = max([point[0] for point in nearest_neighbours.keys()])
    min_row = min([point[1] for point in nearest_neighbours.keys()])
    max_row = max([point[1] for point in nearest_neighbours.keys()])
    # remove edge points: these extend infinitely ...
    # need to force a list to prevent the iterator being returned
    for key in list(nearest_neighbours.keys()):
        if key[0] == min_col or key[0] == max_col or key[1] == min_row or key[1] == max_row:
            nearest_neighbours.pop(key)


def find_most_neighbours(nearest_neighbours):
    # first remove the boys on the boundary
    remove_edges(nearest_neighbours)
    # next, retrieve the length of the longest
    return max([len(nearest_neighbours[p]) for p in nearest_neighbours])


def day6():
    res = {}
    points = read_points('data/day6-input.txt')
    nn1 = walk_all(points, 400)
    nn2 = walk_all(points, 410)
    # if length of nearest neighbours on both grids does not change with size
    # this is problably not an infinite area.
    for p in nn1:
        if nn1[p] == nn2[p]:
            res[p] = []
            for l in nn1[p]:
                if l[0] >= 0 and l[1] >= 0:
                    res[p].append(l)

    return max([len(res[p]) for p in res])


if __name__ == '__main__':
    print(day6())
