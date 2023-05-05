"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in
faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning;
rather than giving a route directly to safety, it produced extremely
circuitous instructions. When the captain uses the PA system to ask if anyone
can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring at
them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the
    ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction
the ship is facing. (That is, if the ship is facing east and the next
instruction is N10, the ship would move north 10 units, but would still move
east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing
    east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still
    facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it
    remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the
absolute values of its east/west position and its north/south position) from
its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan
distance between that location and the ship's starting position?

"""
import utils


def manhattan_distance(xcur, ycur, xstart=0, ystart=0):
    # return manhattan distance = steps along the grid
    return abs(xcur - xstart) + abs(ycur - ystart)


"""Directions 
  N    ^
W   E  | 
  S    y  x-->
"""


class Ferry:

    def __init__(self):
        self.direction = (1, 0)
        self.position = (0, 0)

    def action(self, action):
        operation = action[0]
        amount = int(action[1:])

        # Rotations
        if (operation == "L" and amount == 90 or
                operation == "R" and amount == 270):
            self.direction = -self.direction[1], self.direction[0]
        elif operation in "LR" and amount == 180:
            self.direction = -self.direction[0], -self.direction[1]
        elif (operation == "L" and amount == 270 or
              operation == "R" and amount == 90):
            self.direction = self.direction[1], -self.direction[0]
        else:
            pass

        # Movements
        if operation == "F":
            self.position = self.position[0] + amount * self.direction[0], \
                            self.position[1] + amount * self.direction[1]
        elif operation == "N":
            self.position = self.position[0], self.position[1] + amount
        elif operation == "S":
            self.position = self.position[0], self.position[1] - amount
        elif operation == "W":
            self.position = self.position[0] - amount, self.position[1]
        elif operation == "E":
            self.position = self.position[0] + amount, self.position[1]

    def current_position(self):
        return self.position

    def current_direction(self):
        return self.direction


if __name__ == "__main__":
    instructions = utils.read_file("data/day12.txt")
    ferry = Ferry()
    for instruction in instructions:
        ferry.action(instruction)
    print(
        f"After completing the instructions the direction faced is "
        f"{ferry.current_direction()}, current position is "
        f"{ferry.current_position()} and the manhattan distance from the "
        f"start is {manhattan_distance(*ferry.current_position())}")
