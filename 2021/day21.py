class DiracDie:
    def __init__(self):
        self.face = 0
        self.rolls = 0

    def roll(self):
        self.face = 1 if self.face == 100 else self.face + 1
        self.rolls += 1
        return self.face

    def number_of_rolls(self):
        return self.rolls


def move(pos, steps):
    new_pos = (pos + steps) % 10
    return new_pos if new_pos != 0 else 10


def part1(p1, p2):
    scores, positions, i = [0, 0], [p1, p2], 0
    die = DiracDie()
    while all([scores[j] < 1000 for j in range(len(scores))]):
        positions[i] = move(positions[i], sum([die.roll() for _ in range(3)]))
        scores[i] += positions[i]
        i = (i + 1) % 2
    return min(scores) * die.number_of_rolls()


if __name__ == '__main__':
    part_1 = part1(8, 3)
    print("Day 21 - part 1", part_1)
    part_2 = None
    print("Day 21 - part 2", part_2)
