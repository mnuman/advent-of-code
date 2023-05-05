import day12


def test_readfile():
    (s, g) = day12.readfile('data/day12-input.txt')
    assert s == '#.#####.##.###...#...#.####..#..#.#....##.###.##...#####.#..##.#..##..#..#.#.#.#....#.####....#..#'
    assert len(g) == 32
    assert g['.####'] == '#'
    assert g['.##..'] == '#'


def test_single_cycle():
    (s, g) = day12.readfile('data/day12-test.txt')
    new_state, leftpot = day12.cycle(initial_state=s, rules=g, cycles=1)
    assert new_state == '#...#....#.....#..#..#..#'
    assert leftpot == 0


def test_10_cycles():
    (s, g) = day12.readfile('data/day12-test.txt')
    new_state, leftpot = day12.cycle(initial_state=s, rules=g, cycles=10)
    assert new_state == '#.#..#...#.##....##..##..##..##'
    assert leftpot == -1


def test_20_cycles():
    (s, g) = day12.readfile('data/day12-test.txt')
    new_state, leftpot = day12.cycle(initial_state=s, rules=g, cycles=20)
    assert new_state == '#....##....#####...#######....#.#..##'
    assert leftpot == -2


def test_calc_20_cycles():
    (s, g) = day12.readfile('data/day12-test.txt')
    new_state, leftpot = day12.cycle(initial_state=s, rules=g, cycles=20)
    assert day12.calc_pot_score(new_state, leftpot) == 325
