import day20a


def test_read_tiles():
    tiles = day20a.read_tiles("data/test_day20.txt")
    assert len(tiles) == 9


def test_calc_hash():
    tile = ['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#',
            '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..',
            '###...#.#.', '..###..###']
    finger_prints = day20a.calc_hash(tile)
    assert len(finger_prints) == 8


def test_fingerprint_tiles():
    # verify all tiles are present, all with 8 fingerprints
    tiles = day20a.read_tiles("data/test_day20.txt")
    fp_tiles = day20a.fingerprint_tiles(tiles)
    assert len(fp_tiles) == 9
    assert all(len(fp_tiles[i]) == 8 for i in fp_tiles)


def test_tiles_per_hash():
    fp = {1: ['a', 'b', 'c'], 2: ['a', 'd']}
    r = day20a.tiles_per_hash(fp)
    assert len(r) == 4
    assert set(r.keys()) == set(['a', 'b', 'c', 'd'])
    assert r['a'] == [1, 2]
