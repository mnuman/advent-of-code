import file_utils as f

DIRECTION_OFFSETS = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


class Day06:
    def __init__(self, fname):
        self.data = self.read_data(fname)
        self.starting_pos = self.find_symbol_locations("^")[0]  # starting position
        self.obstacles = self.find_symbol_locations("#")

    def part1(self):
        direction_index = 0
        current_pos = self.starting_pos
        max_rows = len(self.data)
        max_cols = len(self.data[0])
        visited = set()

        while 0 <= current_pos[0] < max_rows and 0 <= current_pos[1] < max_cols:
            visited.add(current_pos)
            next_pos = (
                current_pos[0] + DIRECTION_OFFSETS[direction_index][0],
                current_pos[1] + DIRECTION_OFFSETS[direction_index][1],
            )
            if next_pos in self.obstacles:
                direction_index = (direction_index + 1) % 4
            else:
                current_pos = next_pos
        return visited

    def part2(self):
        # determine number of possible locations for the obstacle.
        # we always turn right - so if we add an obstacle, we must have a specific
        # rectangulararrangment (off by 1):
        """
         #
         zzzzzzzzzzzzzz#
         z            z
         z            z
        #zzzzzzzzzzzzzz
                      #
        So this would amount to locations:
        - top left: (r1, c1)
        - top right: (r1+1, c2)
        - bottom right: (r2, c2-1)
        - bottom left: (r2-1, c1-1)

        The analytical solution is more complex to implement, as the obstacle
        we locate can be either of the corners of the rectangle. Instead,
        brute force by considering the path it will run when
        unimpeded and check if it will cross itself for each candidate
        obstacle.
        """

        obstacle_candidates = self.part1()  # candidates must be on the current path
        obstacle_candidates.remove(
            self.starting_pos
        )  # starting position is not a candidate
        result = 0
        max_rows = len(self.data)
        max_cols = len(self.data[0])
        for i, obstacle in enumerate(obstacle_candidates):
            obstacles = self.obstacles + [obstacle]
            visited = set()
            direction_index = 0
            current_pos = self.starting_pos
            while 0 <= current_pos[0] < max_rows and 0 <= current_pos[1] < max_cols:
                visited.add((current_pos, direction_index))
                next_pos = (
                    current_pos[0] + DIRECTION_OFFSETS[direction_index][0],
                    current_pos[1] + DIRECTION_OFFSETS[direction_index][1],
                )
                if next_pos in obstacles:
                    direction_index = (direction_index + 1) % 4
                elif (next_pos, direction_index) in visited:
                    result += 1
                    break
                else:
                    current_pos = next_pos
        return result

    def read_data(self, fname: str):
        return f.read_file(filename=fname, convert=list)

    def find_symbol_locations(self, symbol):
        return [
            (r, c)
            for r, row in enumerate(self.data)
            for c, col in enumerate(row)
            if col == symbol
        ]


if __name__ == "__main__":
    d = Day06("day06.txt")
    print(len(d.part1()))
    print(d.part2())
