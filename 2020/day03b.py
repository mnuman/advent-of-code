"""
Descent using a toboggan, one down, three right per move. Grid extends infinitely to the right.
When a # is encountered, a tree is hit.

Grid    col: -->
row     0 1 2 3 4 5 6 ...
 |      1
        2

"""
import day03a
import utils
from functools import reduce

if __name__ == '__main__':
    slope_map = utils.read_file("data/day03a.txt")
    hit_list = [day03a.Slope(slope_map, move_col=scenario[0], move_row=scenario[1]).descent() for scenario in
                [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    print(hit_list)
    hits = reduce((lambda x, y: x * y), hit_list)
    print(f'Bumped into {hits} trees.')
