"""
My maths has gone so rusty I decided to bring SymPy.

--- Day 24: Never Tell Me The Odds ---

It seems like something is going wrong with the snow-making process. Instead of
forming snow, the water that's been absorbed into the air seems to be
forming hail!

Maybe there's something you can do to break up the hailstones?

Due to strong, probably-magical winds, the hailstones are all flying through the air
in perfectly linear trajectories. You make a note of each hailstone's position and
velocity (your puzzle input). For example:

19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3

Each line of text corresponds to the position and velocity of a single hailstone.
The positions indicate where the hailstones are right now (at time 0). The
velocities are constant and indicate exactly how far each hailstone will
move in one nanosecond.

Each line of text uses the format px py pz @ vx vy vz. For instance, the
hailstone specified by 20, 19, 15 @ 1, -5, -3 has initial X position 20,
Y position 19, Z position 15, X velocity 1, Y velocity -5, and Z velocity -3.
After one nanosecond, the hailstone would be at 21, 14, 12.

Perhaps you won't have to do anything. How likely are the hailstones to collide
with each other and smash into tiny ice crystals?

To estimate this, consider only the X and Y axes; ignore the Z axis. Looking
forward in time, how many of the hailstones' paths will intersect within a
test area? (The hailstones themselves don't have to collide, just test for
intersections between the paths they will trace.)

In this example, look for intersections that happen with an X and Y position each
at least 7 and at most 27; in your actual data, you'll need to check a much
larger test area. Comparing all pairs of hailstones' future paths produces
the following results:

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 18, 19, 22 @ -1, -1, -2
Hailstones' paths will cross inside the test area (at x=14.333, y=15.333).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 20, 25, 34 @ -2, -2, -4
Hailstones' paths will cross inside the test area (at x=11.667, y=16.667).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=6.2, y=19.4).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for hailstone A.

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 20, 25, 34 @ -2, -2, -4
Hailstones' paths are parallel; they never intersect.

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=-6, y=-5).

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for both hailstones.

Hailstone A: 20, 25, 34 @ -2, -2, -4
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=-2, y=3).

Hailstone A: 20, 25, 34 @ -2, -2, -4
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for hailstone B.

Hailstone A: 12, 31, 28 @ -1, -2, -1
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for both hailstones.

So, in this example, 2 hailstones' future paths cross inside the boundaries of
the test area.

However, you'll need to search a much larger test area if you want to see if any
hailstones might collide. Look for intersections that happen with an X and Y
position each at least 200000000000000 and at most 400000000000000. Disregard
the Z axis entirely.

Considering only the X and Y axes, check all pairs of hailstones' future paths
for intersections. How many of these intersections occur within the test area?

Your puzzle answer was 12783.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Upon further analysis, it doesn't seem like any hailstones will naturally collide.
It's up to you to fix that!

You find a rock on the ground nearby. While it seems extremely unlikely,
if you throw it just right, you should be able to hit every hailstone in a single throw!

You can use the probably-magical winds to reach any integer position you like and to
propel the rock at any integer velocity. Now including the Z axis in your calculations,
if you throw the rock at time 0, where do you need to be so that the rock perfectly
collides with every hailstone? Due to probably-magical inertia, the rock won't
slow down or change direction when it collides with a hailstone.

In the example above, you can achieve this by moving to position 24, 13, 10
and throwing the rock at velocity -3, 1, 2. If you do this, you will hit every
hailstone as follows:

Hailstone: 19, 13, 30 @ -2, 1, -2
Collision time: 5
Collision position: 9, 18, 20

Hailstone: 18, 19, 22 @ -1, -1, -2
Collision time: 3
Collision position: 15, 16, 16

Hailstone: 20, 25, 34 @ -2, -2, -4
Collision time: 4
Collision position: 12, 17, 18

Hailstone: 12, 31, 28 @ -1, -2, -1
Collision time: 6
Collision position: 6, 19, 22

Hailstone: 20, 19, 15 @ 1, -5, -3
Collision time: 1
Collision position: 21, 14, 12

Above, each hailstone is identified by its initial position and its velocity.
Then, the time and position of that hailstone's collision with your rock are given.

After 1 nanosecond, the rock has exactly the same position as one of the hailstones,
obliterating it into ice dust! Another hailstone is smashed to bits two nanoseconds
after that. After a total of 6 nanoseconds, all of the hailstones have been
destroyed.

So, at time 0, the rock needs to be at X position 24, Y position 13, and Z position 10.
Adding these three coordinates together produces 47. (Don't add any coordinates from
the rock's velocity.)

Determine the exact position and velocity the rock needs to have at time 0 so that it
perfectly collides with every hailstone. What do you get if you add up the X, Y, and Z
coordinates of that initial position?

"""
import file_utils as u
from itertools import combinations
from sympy import solve
from sympy.abc import a, b

counter = 0


def parse_line(line: str):
    pos, dir = line.split("@")
    return tuple(map(int, pos.split(","))), tuple(map(int, dir.split(",")))


def intersect(h1, h2, min_coord, max_coord):
    global counter
    counter += 1
    if counter % 500 == 0:
        print(f"Iteration {counter}")
    (x1, y1, _), (dx1, dy1, _) = h1
    (x2, y2, _), (dx2, dy2, _) = h2

    solution = solve([x1 + a * dx1 - x2 - b * dx2, y1 + a * dy1 - y2 - b * dy2])
    if len(solution) != 2:
        return False
    x, y = x1 + solution[a] * dx1, y1 + solution[a] * dy1
    return (
        solution[a] > 0
        and solution[b] > 0
        and min_coord <= x <= max_coord
        and min_coord <= y <= max_coord
    )


def count_intersections(hails, min_coord, max_coord):
    """
    Intersections of two lines l1 = (x1,y1) + a(u1,v1) and l2 = (x2,y2) + b(u2,v2)
    means that:
    [u1    -u2] [a] = [x2-x1]
    [v1    -v2] [b] = [y2-y1]

    The matrix must be invertible, hence its determinant v1*u2-u1*v2
    must be unequal to zero.
    Next:
    [a]         1     [-v2   -v1]   [x2-x1]          1     [-v2*(x2-x1)-v1*(y2-y1)]
        =  ----------             *          =   ----------
    [b]   v1*u2-u1*v2 [u2    u1]    [y2-y1]    v1*u2-u1*v2 [u2*(x2-x1)+u1*(y2-y1)]
    """
    return sum(
        [
            1
            for h1, h2 in combinations(hails, 2)
            if intersect(h1, h2, min_coord, max_coord)
        ]
    )


"""
[x1 + a * dx1 - x2 - b * dx2, y1 + a * dy1 - y2 - b * dy2]
"""


def rock(hails):
    from sympy.abc import a, b, c, r, s, t, u, v, w

    (x1, y1, z1), (dx1, dy1, dz1) = hails[0]
    (x2, y2, z2), (dx2, dy2, dz2) = hails[1]
    (x3, y3, z3), (dx3, dy3, dz3) = hails[2]
    sol = solve(
        [
            x1 + a * dx1 - r - a * u,
            y1 + a * dy1 - s - a * v,
            z1 + a * dz1 - t - a * w,
            x2 + b * dx2 - r - b * u,
            y2 + b * dy2 - s - b * v,
            z2 + b * dz2 - t - b * w,
            x3 + c * dx3 - r - c * u,
            y3 + c * dy3 - s - c * v,
            z3 + c * dz3 - t - c * w,
        ]
    )

    return None if len(sol) != 1 else sol[0][r] + sol[0][s] + sol[0][t]


def part1(fname: str, min_coord, max_coord) -> int:
    hails = [parse_line(line) for line in u.read_file(fname)]
    return count_intersections(hails, min_coord, max_coord)


def part2(fname: str) -> int:
    hails = [parse_line(line) for line in u.read_file(fname)]
    return rock(hails)


if __name__ == "__main__":
    # print(
    #     f"Results part1: {part1('day24.txt', 200_000_000_000_000,
    #  400_000_000_000_000)}"
    # )
    print(f"Results part2: {part2('day24.txt')}")
