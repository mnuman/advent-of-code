"""
Descent using a toboggan, one down, three right per move. Grid extends infinitely to the right.
When a # is encountered, a tree is hit.

Grid    col: -->
row     0 1 2 3 4 5 6 ...
 |      1
        2

"""
import utils


class Slope:

    def __init__(self, slope_map, col=0, row=0, move_row=1, move_col=3):
        self.col, self.row = col, row
        self.max_col, self.max_row = len(slope_map[0]) - 1, len(slope_map) - 1
        self.slope_map = slope_map
        self.move_row, self.move_col = move_row, move_col

    def normalize_coordinates(self):
        self.col, self.row = self.col % (self.max_col + 1), self.row % (self.max_row + 1)
        return

    def move(self, move_row=None, move_col=None):
        self.col += move_col if move_col is not None else self.move_col
        self.row += move_row if move_row is not None else self.move_row
        self.normalize_coordinates()
        return

    def hit_tree(self):
        return self.slope_map[self.row][self.col] == "#"

    def descent(self):
        hits = 0
        while self.row < self.max_row:
            self.move()
            if self.hit_tree():
                hits += 1
        return hits


if __name__ == '__main__':
    slope_map = utils.read_file("data/day03a.txt")
    p = Slope(slope_map)
    hits = p.descent()
    print(f'Bumped into {hits} trees.')
