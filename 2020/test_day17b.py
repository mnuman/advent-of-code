import day17b


def test_scenario_1():
    state = {(0, 0, 0, 0): '.', (1, 0, 0, 0): '#', (2, 0, 0, 0): '.',
             (0, 1, 0, 0): '.', (1, 1, 0, 0): '.', (2, 1, 0, 0): '#',
             (0, 2, 0, 0): '#', (1, 2, 0, 0): '#', (2, 2, 0, 0): '#'}
    assert day17b.cycle(state) == 848


def test_all_neighbours():
    nb = day17b.all_neighbours(0, 0, 0, 0)
    assert len(nb) == 80
    assert (0, 0, 0, 0) not in nb
    assert (1, 1, 1, 1) in nb
    assert (0, -1, 1, 0) in nb
