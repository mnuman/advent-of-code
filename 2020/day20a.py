"""
--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you south. You can
even see a desert in the distance! Since you have some spare time, you might
as well see if there was anything interesting in the image the Mythical
Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually
contains many small images created by the satellite's camera array. The
camera array consists of many cameras; rather than produce a single square
image, they produce many smaller square image tiles that need to be
reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a
random unique ID number. The tiles (your puzzle input) arrived in a random
order.

Worse yet, the camera array appears to be malfunctioning: each image tile has
been rotated and flipped to a random orientation. Your first task is to
reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes
a border that should line up exactly with its adjacent tiles. All tiles have
this border, and the border lines up exactly when the tiles are both oriented
correctly. Tiles at the edge of the image also have this border, but the
outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

By rotating, flipping, and rearranging them, you can find a square
arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....

For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171

To check that you've assembled the image correctly, multiply the IDs of the
four corner tiles together. If you do this with the assembled tiles from the
example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together
the IDs of the four corner tiles?

Approach:
 - determine the tiles
 - extract the edge patterns of each tile
 - for each tile's edges, calculate the hash of the pattern and its reverse
 - assume that corners only fit to two other pieces. as we have hashed both
   the edge and its reverse, this implies four matching hashes per corner
   piece. find and multiply.
"""
import hashlib

import utils


def read_tiles(filename):
    raw_lines = utils.read_file(filename)
    tiles = {}
    idx = 0
    while idx < len(raw_lines):
        tile_number = int(raw_lines[idx][-5:-1])
        tiles[tile_number] = [raw_lines[idx + i] for i in range(1, 11)]
        idx += 12
    return tiles


def fingerprint_tiles(tiles):
    """Determine the unique? fingerprints of each tile, e.g. the hash of its
    edges. Since we also need to flip, we must also consider the edge pattern
    reversed!"""
    return {tile_number: calc_hash(tiles[tile_number])
            for tile_number in tiles}


def calc_hash(tile):
    edges = tile[0], tile[-1], ''.join(line[0] for line in tile), ''.join(
        line[-1] for line in tile)
    fp = []
    for edge in edges:
        for e in (edge, edge[-1::-1]):
            fp.append(hashlib.sha256(e.encode('utf-8')).hexdigest())
    return set(fp)


def tiles_per_hash(finger_prints):
    # collect the tiles per fingerprint
    result = {}
    for tile in finger_prints:
        for fp in finger_prints[tile]:
            if fp in result:
                result[fp].append(tile)
            else:
                result[fp] = [tile]
    return result


if __name__ == "__main__":
    all_tiles = read_tiles("data/day20.txt")
    fp = fingerprint_tiles(all_tiles)
    hashes = tiles_per_hash(fp)

    overlaps = {}
    for h in hashes:
        for tile in hashes[h]:
            if tile in overlaps:
                overlaps[tile] += len(hashes[h]) - 1
            else:
                overlaps[tile] = len(hashes[h]) - 1
    prod = 1
    for o in overlaps:
        if overlaps[o] == 4:
            print(f"Edge found: {o}")
            prod *= o
    print(f"Result {prod}")
