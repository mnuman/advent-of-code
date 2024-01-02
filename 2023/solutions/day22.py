"""
--- Day 22: Sand Slabs ---

Enough sand has fallen; it can finally filter water for Snow Island.

Well, almost.

The sand has been falling as large compacted bricks of sand, piling up to form an
impressive stack here near the edge of Island Island. In order to make use of
the sand to filter water, some of the bricks will need to be broken apart - nay,
disintegrated - back into freely flowing sand.

The stack is tall enough that you'll have to be careful about choosing which bricks
to disintegrate; if you disintegrate the wrong brick, large portions of the stack
could topple, which sounds pretty dangerous.

The Elves responsible for water filtering operations took a snapshot of the bricks
while they were still falling (your puzzle input) which should let you work out
which bricks are safe to disintegrate. For example:

1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9

Each line of text in the snapshot represents the position of a single brick at
the time the snapshot was taken. The position is given as two x,y,z coordinates -
one for each end of the brick - separated by a tilde (~). Each brick is made up
of a single straight line of cubes, and the Elves were even careful to choose a
time for the snapshot that had all of the free-falling bricks at integer positions
above the ground, so the whole snapshot is aligned to a three-dimensional cube
grid.

A line like 2,2,2~2,2,2 means that both ends of the brick are at the same
coordinate - in other words, that the brick is a single cube.

Lines like 0,0,10~1,0,10 or 0,0,10~0,1,10 both represent bricks that are two
cubes in volume, both oriented horizontally. The first brick extends in the x
direction, while the second brick extends in the y direction.

A line like 0,0,1~0,0,10 represents a ten-cube brick which is oriented vertically.
One end of the brick is the cube located at 0,0,1, while the other end of the brick
is located directly above it at 0,0,10.

The ground is at z=0 and is perfectly flat; the lowest z value a brick can have is
therefore 1. So, 5,5,1~5,6,1 and 0,2,1~0,2,5 are both resting on the ground,
but 3,3,2~3,3,3 was above the ground at the time of the snapshot.

Because the snapshot was taken while the bricks were still falling, some bricks will
still be in the air; you'll need to start by figuring out where they will end up.
Bricks are magically stabilized, so they never rotate, even in weird situations
like where a long horizontal brick is only supported on one end. Two bricks cannot
occupy the same position, so a falling brick will come to rest upon the first other
brick it encounters.

Here is the same example again, this time with each brick given a letter so it
can be marked in diagrams:

1,0,1~1,2,1   <- A
0,0,2~2,0,2   <- B
0,2,3~2,2,3   <- C
0,0,4~0,2,4   <- D
2,0,5~2,2,5   <- E
0,1,6~2,1,6   <- F
1,1,8~1,1,9   <- G

At the time of the snapshot, from the side so the x axis goes left to right, these
bricks are arranged like this:

 x
012
.G. 9
.G. 8
... 7
FFF 6
..E 5 z
D.. 4
CCC 3
BBB 2
.A. 1
--- 0

Rotating the perspective 90 degrees so the y axis now goes left to right, the same
bricks are arranged like this:

 y
012
.G. 9
.G. 8
... 7
.F. 6
EEE 5 z
DDD 4
..C 3
B.. 2
AAA 1
--- 0

Once all of the bricks fall downward as far as they can go, the stack looks like this,
where ? means bricks are hidden behind other bricks at that location:

 x
012
.G. 6
.G. 5
FFF 4
D.E 3 z
??? 2
.A. 1
--- 0

Again from the side:

 y
012
.G. 6
.G. 5
.F. 4
??? 3 z
B.C 2
AAA 1
--- 0

Now that all of the bricks have settled, it becomes easier to tell which bricks are
supporting which other bricks:

    Brick A is the only brick supporting bricks B and C.
    Brick B is one of two bricks supporting brick D and brick E.
    Brick C is the other brick supporting brick D and brick E.
    Brick D supports brick F.
    Brick E also supports brick F.
    Brick F supports brick G.
    Brick G isn't supporting any bricks.

Your first task is to figure out which bricks are safe to disintegrate. A brick can be
safely disintegrated if, after removing it, no other bricks would fall further
directly downward. Don't actually disintegrate any bricks - just determine what
would happen if, for each brick, only that brick were disintegrated. Bricks can
be disintegrated even if they're completely surrounded by other bricks; you can
squeeze between bricks if you need to.

In this example, the bricks can be disintegrated as follows:

    Brick A cannot be disintegrated safely; if it were disintegrated, bricks B and C
    would both fall.
    Brick B can be disintegrated; the bricks above it (D and E) would still be
    supported by brick C.
    Brick C can be disintegrated; the bricks above it (D and E) would still be
    supported by brick B.
    Brick D can be disintegrated; the brick above it (F) would still be supported
    by brick E.
    Brick E can be disintegrated; the brick above it (F) would still be supported
    by brick D.
    Brick F cannot be disintegrated; the brick above it (G) would fall.
    Brick G can be disintegrated; it does not support any other bricks.

So, in this example, 5 bricks can be safely disintegrated.

Figure how the blocks will settle based on the snapshot. Once they've settled, consider
disintegrating a single brick; how many bricks could be safely chosen as the one to get
disintegrated?

--- Part Two ---

Disintegrating bricks one at a time isn't going to be fast enough. While it might sound
dangerous, what you really need is a chain reaction.

You'll need to figure out the best brick to disintegrate. For each brick, determine
how many other bricks would fall if that brick were disintegrated.

Using the same example as above:

    Disintegrating brick A would cause all 6 other bricks to fall.
    Disintegrating brick F would cause only 1 other brick, G, to fall.

Disintegrating any other brick would cause no other bricks to fall. So, in this
example, the sum of the number of other bricks that would fall as a result of
disintegrating each brick is 7.

For each brick, determine how many other bricks would fall if that brick were
disintegrated. What is the sum of the number of other bricks that would fall?

"""
from collections import defaultdict
import file_utils as u
from uuid import uuid4


class Block:
    def __init__(self, input: str, idx=None):
        self.name = "Block-" + str(idx) if idx is not None else str(uuid4())
        s, e = input.split("~")
        self.start_x, self.start_y, self.start_z = list(map(int, s.split(",")))
        self.end_x, self.end_y, self.end_z = list(map(int, e.split(",")))
        self.xy: set[tuple[int, int]] = {
            (x, y)
            for x in range(self.start_x, self.end_x + 1)
            for y in range(self.start_y, self.end_y + 1)
        }

    def drop(self, new_z: int):
        self.start_z, self.end_z = new_z, new_z + self.end_z - self.start_z


def sort_z(lst: list[Block], descending=False) -> list[Block]:
    s = -1 if descending else 1
    return sorted(lst, key=lambda b: s * b.start_z)


def calculate_overlaps(block_list: list[Block]) -> dict[Block, list[Block]]:
    """
    1. loop over the blocks in descending height order
    2. consider all blocks with lower height, so only higher index in descending
       height order
    3. an overlap is found when their xy projection share a coordinate pair
    """
    z_sorted_list = sort_z(block_list, descending=True)
    return {
        hi: sort_z(
            [
                lo
                for lo in z_sorted_list[idx + 1 :]
                if lo.end_z < hi.start_z and not hi.xy.isdisjoint(lo.xy)
            ],
            descending=True,
        )
        for idx, hi in enumerate(z_sorted_list)
    }


def settle(brick_supports: dict[Block, list[Block]]) -> None:
    for block in sort_z(list(brick_supports.keys())):
        supports = brick_supports[block]
        # this block must rest on its supports, hence its z needs to be the
        # highest of the overlap's ends + 1, or simply 1 if it does not
        # have any overlapping supports
        new_z = 1 if len(supports) == 0 else 1 + max(b.end_z for b in supports)
        block.drop(new_z)


def calc_support(
    xy_overlaps: dict[Block, list[Block]]
) -> tuple[dict[Block, list[Block]], dict[Block, list[Block]]]:
    physically_supported_by = {
        k: [v for v in values if v.end_z + 1 == k.start_z]
        for k, values in xy_overlaps.items()
    }
    physical_supports = defaultdict(list)
    for k, v in physically_supported_by.items():
        for val in v:
            physical_supports[val] += [k]
    return physically_supported_by, physical_supports


def part1(fname: str) -> int:
    bricks: list[Block] = [
        Block(line, idx) for idx, line in enumerate(u.read_file(fname))
    ]
    xy_overlaps = calculate_overlaps(bricks)
    settle(xy_overlaps)
    physically_supported_by, physical_supports = calc_support(xy_overlaps)

    # for k, v in physically_supported_by.items():
    #     print(f"{k.name} - {[val.name for val in v]}")

    # for k, v in physical_supports.items():
    #     print(f"{k.name} - {[val.name for val in v]}")

    supports_none = [
        key.name
        for key in physically_supported_by.keys()
        if key not in physical_supports.keys()
    ]
    supports_multi_supported_blocks = [
        key.name
        for key, val in physical_supports.items()
        if all([len(physically_supported_by[v]) > 1 for v in val])
    ]
    return len(set(supports_none + supports_multi_supported_blocks))


# cache one way or another
def desintegrate(desintegrated, physically_supported_by, physical_supports) -> int:
    partially_supported_by = []
    for des in desintegrated:
        partially_supported_by += physical_supports[des]
    falling = {         # set - filter out dupes!
        ps
        for ps in partially_supported_by
        if all(s in desintegrated for s in physically_supported_by[ps])
    }
    return (
        0
        if len(falling) == 0
        else len(falling)
        + desintegrate(tuple(falling), physically_supported_by, physical_supports)
    )


def chainreaction(xy_overlaps: dict[Block, list[Block]]) -> int:
    physically_supported_by, physical_supports = calc_support(xy_overlaps)
    """
    1. block-0 disintegrates
    2. physical-supports[block-0] = block-1, block-2
    3. physical-supports
         block-1 = block-3 + block-4
         block-2 = block-3 + block-4
         block-3 supported by block-1, block-2: all falling -> falls
         block-3 supported by block-1, block-2: all falling -> falls
    """
    s = 0
    for d in physically_supported_by.keys():
        x = desintegrate(tuple([d]), physically_supported_by, physical_supports)
        print(f"{d.name}: {x}")
        s += x
    return s


def part2(fname: str) -> int:
    bricks: list[Block] = [
        Block(line, idx) for idx, line in enumerate(u.read_file(fname))
    ]
    print("Read")
    xy_overlaps = calculate_overlaps(bricks)
    settle(xy_overlaps)
    print("Settled")
    return chainreaction(xy_overlaps)


if __name__ == "__main__":
    print(f"Results part1: {part1('day22.txt')}")
    print(f"Results part2: {part2('day22.txt')}")
