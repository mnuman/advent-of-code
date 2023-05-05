import day17a


def test_read_initial_state():
    current_state = day17a.read_initial_state("data/test_day17.txt")
    assert len(current_state) == 9
    assert current_state[(0, 0, 0)] == day17a.INACTIVE_STATE
    assert current_state[(0, 1, 0)] == day17a.ACTIVE_STATE


def test_expand_calculation_boundaries():
    state = {(0, 0, 0): '.', (0, 1, 0): '#', (0, 2, 0): '.', (1, 0, 0): '.',
             (1, 1, 0): '.', (1, 2, 0): '#', (2, 0, 0): '#', (2, 1, 0): '#',
             (2, 2, 0): '#'}
    result = day17a.expand_calculation_boundaries(state)
    assert len(result) == 3
    assert result[0] == (-1, 3)
    assert result[1] == (-1, 3)
    assert result[2] == (-1, 1)


def test_get_current_state():
    state = {(0, 0, 0): '.', (0, 1, 0): '#', (0, 2, 0): '.', (1, 0, 0): '.',
             (1, 1, 0): '.', (1, 2, 0): '#', (2, 0, 0): '#', (2, 1, 0): '#',
             (2, 2, 0): '#'}
    assert day17a.get_current_cell_state(state, 0, 0,
                                         0) == day17a.INACTIVE_STATE
    assert day17a.get_current_cell_state(state, 9, 9,
                                         9) == day17a.INACTIVE_STATE
    assert day17a.get_current_cell_state(state, 2, 2, 0) == day17a.ACTIVE_STATE


def test_next_cell_state():
    state = {(0, 0, 0): '.', (0, 1, 0): '#', (0, 2, 0): '.', (1, 0, 0): '.',
             (1, 1, 0): '.', (1, 2, 0): '#', (2, 0, 0): '#', (2, 1, 0): '#',
             (2, 2, 0): '#'}
    assert day17a.next_cell_state(state, 0, 0, 0) == day17a.INACTIVE_STATE


def test_calculate_next_state():
    state = {(0, 0, 0): '.', (1, 0, 0): '#', (2, 0, 0): '.', (0, 1, 0): '.',
             (1, 1, 0): '.', (2, 1, 0): '#', (0, 2, 0): '#', (1, 2, 0): '#',
             (2, 2, 0): '#'}
    new_state = day17a.calculate_next_state(state)
    assert len(new_state) == 11


def test_all_neighbours():
    nb = day17a.all_neighbours(0, 0, 0)
    assert len(nb) == 26
    assert (0, 0, 0) not in nb
    assert (1, 1, 1) in nb
    assert (0, -1, 1) in nb


def test_scenario_1():
    state = {(0, 0, 0): '.', (1, 0, 0): '#', (2, 0, 0): '.', (0, 1, 0): '.',
             (1, 1, 0): '.', (2, 1, 0): '#', (0, 2, 0): '#', (1, 2, 0): '#',
             (2, 2, 0): '#'}
    assert day17a.cycle(state) == 112
