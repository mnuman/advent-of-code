"""
--- Part Two ---

Before you can give the destination to the captain, you realize that the
actual action meanings were printed on the back of the instructions the whole
time.

Almost all of the actions indicate how to move a waypoint which is relative
to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (
    counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise)
    the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to
    the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The
waypoint is relative to the ship; that is, if the ship moves, the waypoint
moves with it.

For example, using the same instructions as above:

    F10 moves the ship to the waypoint 10 times (a total of 100 units east
    and 10 units north), leaving the ship at east 100, north 10. The waypoint
    stays 10 units east and 1 unit north of the ship.
    N3 moves the waypoint 3 units north to 10 units east and 4 units north of
    the ship. The ship remains at east 100, north 10.
    F7 moves the ship to the waypoint 7 times (a total of 70 units east and
    28 units north), leaving the ship at east 170, north 38. The waypoint
    stays 10 units east and 4 units north of the ship.
    R90 rotates the waypoint around the ship clockwise 90 degrees, moving it
    to 4 units east and 10 units south of the ship. The ship remains at east
    170, north 38.
    F11 moves the ship to the waypoint 11 times (a total of 44 units east and
    110 units south), leaving the ship at east 214, south 72. The waypoint
    stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting
position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?

"""
import day12a
import utils


class Ferry:

    def __init__(self):
        self.position = (0, 0)
        self.waypoint = (10, 1)

    def action(self, action):
        operation = action[0]
        amount = int(action[1:])

        # NSWE just move the waypoint, not the ferry
        if operation == "N":
            self.waypoint = self.waypoint[0], self.waypoint[1] + amount
        elif operation == "S":
            self.waypoint = self.waypoint[0], self.waypoint[1] - amount
        elif operation == "E":
            self.waypoint = self.waypoint[0] + amount, self.waypoint[1]
        elif operation == "W":
            self.waypoint = self.waypoint[0] - amount, self.waypoint[1]

        dx, dy = self.waypoint[0] - self.position[0], self.waypoint[1] - \
                 self.position[1]

        if operation in "LR" and amount == 180:
            self.waypoint = self.position[0] - dx, \
                            self.position[1] - dy
        elif operation == "L" and amount == 90 or operation == "R" and amount \
                == 270:
            self.waypoint = self.position[0] - dy, \
                            self.position[1] + dx
        elif operation == "L" and amount == 270 or operation == "R" and amount \
                == 90:
            self.waypoint = self.position[0] + dy, \
                            self.position[1] - dx
        elif operation == "F":
            self.position = self.position[0] + amount * dx, \
                            self.position[1] + amount * dy
            self.waypoint = self.position[0] + dx, \
                            self.position[1] + dy
        print(f"Pos: {self.position}, way: {self.waypoint}")

    def current_position(self):
        return self.position

    def current_waypoint(self):
        return self.waypoint


if __name__ == "__main__":
    instructions = utils.read_file("data/day12.txt")
    ferry = Ferry()
    for instruction in instructions:
        ferry.action(instruction)
    print(
        f"After completing the instructions the current position is "
        f"{ferry.current_position()} and the manhattan distance from the "
        f"start is {day12a.manhattan_distance(*ferry.current_position())}")
