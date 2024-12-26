from fractions import Fraction
import file_utils as f
import re

# Constants
NUMBER = r"\d+"


class ClawMachine:
    def __init__(self, strings) -> None:
        assert len(strings) == 3
        self.a_x, self.a_y = map(int, re.findall(r"\d+", strings[0]))
        self.b_x, self.b_y = map(int, re.findall(r"\d+", strings[1]))
        self.prize_x, self.prize_y = map(int, re.findall(r"\d+", strings[2]))
        self.flag = abs(self.a_x / self.a_y - self.b_x / self.b_y) < 1e-4

    def solve(self):
        self.a_x, self.a_y, self.b_x, self.b_y, self.prize_x, self.prize_y = map(
            Fraction,
            (self.a_x, self.a_y, self.b_x, self.b_y, self.prize_x, self.prize_y),
        )
        b = ((self.a_y * self.prize_x) / self.a_x - self.prize_y) / (
            (self.a_y * self.b_x / self.a_x) - self.b_y
        )
        a = (self.prize_x - self.b_x * b) / self.a_x
        if a.denominator == 1 and b.denominator == 1:
            return (3 * a + b).numerator
        return 0

    def update_prize(self):
        self.prize_x += 10000000000000
        self.prize_y += 10000000000000


def read_data(fname: str):
    data = []
    raw = f.read_file(fname)
    for i in range(0, len(raw), 4):
        data.append(ClawMachine(raw[i : i + 3]))
    return data


def part1(data):
    return sum(i.solve() for i in data)


def part2(data):
    for i in data:
        i.update_prize()
    return sum(i.solve() for i in data)


if __name__ == "__main__":
    claw_machines = read_data("day13.txt")
    print(f"Part 1: {part1(claw_machines)}")
    print(f"Part 2: {part2(claw_machines)}")
