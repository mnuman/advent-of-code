# symbols for CARs, the direction they travel (row,col) and replacement symbol
CARTS = {'v': ((1, 0), '|'), '^': ((-1, 0), '|'),
         '>': ((0, 1), '-'), '<': ((0, -1), '-')}


class Cart():
    TURN_LEFT = {(0, 1): (-1, 0), (-1, 0): (0, -1),
                 (0, -1): (1, 0), (1, 0): (0, 1)}
    TURN_RIGHT = {(0, 1): (1, 0), (-1, 0): (0, 1),
                  (0, -1): (-1, 0), (1, 0): (0, -1)}

    def __init__(self, row, col, moverow, movecol):
        self.row = row
        self.col = col
        self.moverow = moverow
        self.movecol = movecol
        self.intersections = 0

    def __str__(self):
        """Return out some human readable representation for this instance"""
        return f'(row,col) = ({self.row}, {self.col}), move: {self.moverow}, {self.movecol})'

    def turn_left(self):
        """Adjust the direction when turning left """
        self.moverow, self.movecol = self.TURN_LEFT[(
            self.moverow, self.movecol)]

    def turn_right(self):
        """Adjust the direction when turning right """
        self.moverow, self.movecol = self.TURN_RIGHT[(
            self.moverow, self.movecol)]

    def move(self):
        """Perform one move"""
        self.col += self.movecol
        self.row += self.moverow

    def change_direction(self, symbol):
        """Adjust the direction this car moves. There are two
           reasons to change direction:
           1) an edge has been reached (forward or backslash) - mandatory turn
           2) an intersection has been reached (+) - optional turn
                   # left, straight, right

        """
        if symbol == '\\':
            self.moverow, self.movecol = self.movecol, self.moverow
        elif symbol == '/':
            self.moverow, self.movecol = -1 * self.movecol, -1 * self.moverow
        elif symbol == '+':
            if self.intersections == 0:
                self.turn_left()
            elif self.intersections == 1:
                pass  # no action on next intersection after turning left
            else:
                self.turn_right()
            self.intersections = (self.intersections + 1) % 3
        else:
            pass    # not a special symbol, no action


class Track():
    def __init__(self, track, carts):
        self.track = track
        self.carts = carts
        self.ticks = 0

    def order_carts(self):
        # return the carts sorted on row first, column next
        return sorted(self.carts, key=lambda cart: (cart.row, cart.col))

    def tick(self):
        """Move all carts one step ahead, plus set their new direction after completing
           the step for the cart.
           """
        for cart in self.order_carts():
            # 1. move the cart
            cart.move()
            # 2. adjust its direction based on its new position
            cart.change_direction(self.track[cart.row][cart.col])
            if self.collision() != []:
                break
        self.ticks += 1

    def tick_remove_collided(self):
        """Move all carts one step ahead, plus set their new direction after completing
           the step for the cart.
           After each tick, remove all the carts that have collided.
           """
        collided = []
        for cart in self.order_carts():
            if cart not in collided:
                # 1. move the cart
                cart.move()
                # 2. adjust its direction based on its new position
                cart.change_direction(self.track[cart.row][cart.col])
                for c in self.collision():
                    collided.append(c)
        # remove all collided carts from the track
        for collided_cart in collided:
            if collided_cart in self.carts:
                self.carts.remove(collided_cart)
        self.ticks += 1

    def collision(self):
        """Return the collided carts or an empty list if there are no collisions ..."""
        return [c1 for i, c1 in enumerate(self.carts) for j, c2 in enumerate(self.carts) if i != j and c1.row == c2.row and c1.col == c2.col]


def process_line(line, track, carts):
    """Add all carts on line to array carts,
       replacing them with the correct track symbol.
       After replacing all carts, add the current line to the track.
       """
    for s in CARTS.keys():
        while s in line:
            move, replacement = CARTS[s]
            col = line.index(s)
            line = line.replace(s, replacement)
            carts.append(Cart(len(track), col, move[0], move[1]))

    track.append(line)


def readfile(fname):
    with open(fname, 'r') as src:
        all_lines = src.readlines()
    track = []
    carts = []
    for l in all_lines:
        l = l.strip('\n')
        process_line(l, track, carts)
    return (track, carts)


def day13(fname, maxiter=200):
    lines, carts = readfile(fname)
    track = Track(lines, carts)
    iter = 0
    while iter < maxiter and track.collision() == []:
        track.tick()
        iter += 1
    return track.collision()


def day13_2(fname, maxiter=20000):
    lines, carts = readfile(fname)
    track = Track(lines, carts)
    iter = 0
    while iter < maxiter and len(carts) > 1:
        track.tick_remove_collided()
        iter += 1
    return carts


carts = day13_2('data/day13-input.txt', maxiter=20000)
print(
    f'Last cart standing ... at x:col = {carts[0].col} and y:row = {carts[0].row}')
# x:col = 143, y:row = 123
