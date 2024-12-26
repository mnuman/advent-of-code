import file_utils as f

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}
EXPANSION = {"#": ("#", "#"), "O": ("[", "]"), ".": (".", "."), "@": ("@", ".")}


def read_data(fname: str):
    data = f.read_file(fname)
    grid = []
    moves = []
    for line in data:
        if "#" in line:
            grid.append([c for c in line])
        else:
            for e in line:
                moves.append(e)
    return grid, moves


class Warehouse:
    def __init__(self, grid):
        self.grid = grid
        self._parse()

    def _parse(self):
        self.position = (0, 0)
        boxes = []
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    self.position = (r, c)
                elif cell == "O":
                    boxes.append((r, c))
        self.boxes = boxes

    def move(self, direction):
        r, c = self.position
        dr, dc = direction
        new_r, new_c = r + dr, c + dc

        if self.grid[new_r][new_c] == "#":  # wall
            return False
        if (new_r, new_c) in self.boxes:  # box
            hit_wall = False
            found_empty = False
            boxes_to_move = [(new_r, new_c)]
            while not (hit_wall or found_empty):  # consider until wall or empty space
                r_next_pos, c_next_pos = (
                    boxes_to_move[-1][0] + dr,
                    boxes_to_move[-1][1] + dc,
                )
                if self.grid[r_next_pos][c_next_pos] == "#":
                    hit_wall = True
                elif (r_next_pos, c_next_pos) in self.boxes:
                    boxes_to_move.append((r_next_pos, c_next_pos))
                else:
                    found_empty = True
            """
            When moving multiple boxes, if the last box can move, all boxes in between will also move.
            Pop off the first box, append one in the same direction to the end.
            """
            if not hit_wall:
                if len(boxes_to_move) > 1:
                    self.boxes.remove(boxes_to_move[0])
                    self.boxes.append(
                        (boxes_to_move[-1][0] + dr, boxes_to_move[-1][1] + dc)
                    )
                else:  # single box
                    r_box, c_box = boxes_to_move[0][0] + dr, boxes_to_move[0][1] + dc
                    self.boxes.remove(boxes_to_move[0])
                    self.boxes.append((r_box, c_box))
                self.position = (new_r, new_c)
        else:  # empty
            self.position = (new_r, new_c)

        return True

    def score(self):
        return sum(100 * r + c for r, c in self.boxes)


class Box:
    def __init__(self, r, c):
        self.left_position = (r, c)
        self.right_position = (r, c + 1)

    def move(self, direction):
        dr, dc = direction
        self.left_position = (self.left_position[0] + dr, self.left_position[1] + dc)
        self.right_position = (self.right_position[0] + dr, self.right_position[1] + dc)


class ExpandedWarehouse:
    def __init__(self, grid):
        self._expand(grid)
        self._parse()

    def _expand(self, grid):
        new_grid = []
        for line in grid:
            new_line = []
            for c in line:
                for e in EXPANSION[c]:
                    new_line.append(e)
            new_grid.append(new_line)
        self.grid = new_grid

    def _parse(self):
        self.position = (0, 0)
        boxes = []
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    self.position = (r, c)
                elif cell == "[":
                    boxes.append(Box(r, c))
        self.boxes = boxes

    def move_current_box(self, box, direction):
        dr, dc = direction
        new_box_positions = [
            (box.left_position[0] + dr, box.left_position[1] + dc),
            (box.right_position[0] + dr, box.right_position[1] + dc),
        ]
        if any(self.grid[r][c] == "#" for r, c in new_box_positions):
            self.move_boxes = False
            self.boxes_to_move = []
        else:
            self.boxes_to_move.append(box)
            overlapping_boxes = [
                b
                for b in self.boxes
                if (
                    b.left_position in new_box_positions
                    or b.right_position in new_box_positions
                )
                and b not in self.boxes_to_move
            ]
            for b in overlapping_boxes:
                self.move_current_box(b, direction)

    def move(self, direction):
        self.boxes_to_move = []
        self.move_boxes = True
        r, c = self.position
        dr, dc = direction
        new_r, new_c = r + dr, c + dc

        if self.grid[new_r][new_c] == "#":  # wall - blocked - do nothing
            return
        hit_box = [
            b
            for b in self.boxes
            if b.left_position == (new_r, new_c) or b.right_position == (new_r, new_c)
        ]
        if len(hit_box) > 0:  # box/es - check all can move
            for b in hit_box:
                self.move_current_box(b, direction)
            if self.move_boxes:
                for box in self.boxes_to_move:
                    box.move(direction)
                self.position = (new_r, new_c)
            self.boxes_to_move = []
        else:  # empty space - move
            self.position = (new_r, new_c)

    def score(self):
        return sum(100 * b.left_position[0] + b.left_position[1] for b in self.boxes)


def part1(grid, moves):
    wh = Warehouse(grid)
    for m in moves:
        wh.move(DIRECTIONS[m])
    return wh.score()


def part2(grid, moves):
    wh = ExpandedWarehouse(grid)
    for m in moves:
        wh.move(DIRECTIONS[m])
    return wh.score()


if __name__ == "__main__":
    grid, moves = read_data("day15.txt")
    print(f"Part 1: {part1(grid, moves)}")
    print(f"Part 2: {part2(grid, moves)}")
