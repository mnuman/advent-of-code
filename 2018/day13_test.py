import day13


def test_cart_turn_move_right_backslash():
    # cart is moving to the right, should move down on backslash
    c = day13.Cart(0, 0, 0, 1)
    c.change_direction('\\')
    assert c.movecol == 0
    assert c.moverow == 1


def test_cart_turn_move_left_backslash():
    # cart is moving to the left, should move up on backslash
    c = day13.Cart(0, 0, 0, -1)
    c.change_direction('\\')
    assert c.movecol == 0
    assert c.moverow == -1


def test_cart_turn_move_up_backslash():
    # cart is moving up, should move left on backslash
    c = day13.Cart(0, 0, -1, 0)
    c.change_direction('\\')
    assert c.movecol == -1
    assert c.moverow == 0


def test_cart_turn_move_down_backslash():
    # cart is moving down, should move right on backslash
    c = day13.Cart(0, 0, 1, 0)
    c.change_direction('\\')
    assert c.movecol == 1
    assert c.moverow == 0


def test_cart_turn_move_left_slash():
    # cart is moving to the left, should move down on slash
    c = day13.Cart(0, 0, 0, -1)
    c.change_direction('/')
    assert c.movecol == 0
    assert c.moverow == 1


def test_cart_turn_move_right_slash():
    # cart is moving to the right, should move up on slash
    c = day13.Cart(0, 0, 0, 1)
    c.change_direction('/')
    assert c.movecol == 0
    assert c.moverow == -1


def test_cart_turn_move_up_slash():
    # cart is moving up, should move right on slash
    c = day13.Cart(0, 0, -1, 0)
    c.change_direction('/')
    assert c.movecol == 1
    assert c.moverow == 0


def test_cart_turn_move_down_slash():
    # cart is moving down, should move left on slash
    c = day13.Cart(0, 0, 1, 0)
    c.change_direction('/')
    assert c.movecol == -1
    assert c.moverow == 0


def test_cart_moving_right_intersection():
    # cart is moving to the right and encounters an intersection
    # should turn left: up
    c = day13.Cart(0, 0, 0, 1)
    # turn left == up
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == -1

    # second time is UNCHANGED
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == -1

    # turn right == original == right
    c.change_direction('+')
    assert c.movecol == 1
    assert c.moverow == 0

    # fourth time is turn left = up again!
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == -1


def test_cart_moving_left_intersection():
    # cart is moving to the left and encounters an intersection
    # should turn left: down
    c = day13.Cart(0, 0, 0, -1)
    # turn left == up
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == 1

    # second time is UNCHANGED
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == 1

    # turn right == original == left
    c.change_direction('+')
    assert c.movecol == -1
    assert c.moverow == 0


def test_cart_moving_up_intersection():
    # cart is moving to the up and encounters an intersection
    # should turn left: left
    c = day13.Cart(0, 0, -1, 0)
    # turn left == up
    c.change_direction('+')
    assert c.movecol == -1
    assert c.moverow == 0

    # second time is UNCHANGED
    c.change_direction('+')
    assert c.movecol == -1
    assert c.moverow == 0

    # turn right == original == up
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == -1


def test_cart_moving_down_intersection():
    # cart is moving down and encounters an intersection
    # should turn left: move right
    c = day13.Cart(0, 0, 1, 0)
    # turn left == up
    c.change_direction('+')
    assert c.movecol == 1
    assert c.moverow == 0

    # second time is UNCHANGED
    c.change_direction('+')
    assert c.movecol == 1
    assert c.moverow == 0

    # turn right == original == down
    c.change_direction('+')
    assert c.movecol == 0
    assert c.moverow == 1


def test_track():
    carts = [day13.Cart(5, 0, 0, 0), day13.Cart(
        3, 8, 0, 0), day13.Cart(3, 1, 0, 0)]
    t = day13.Track(None, carts)
    sorted_carts = t.order_carts()
    assert len(sorted_carts) == 3
    # Have all carts been sorted on smallest row, smalles col within row?
    assert sorted_carts[0].row == 3 and sorted_carts[0].col == 1
    assert sorted_carts[1].row == 3 and sorted_carts[1].col == 8
    assert sorted_carts[2].row == 5 and sorted_carts[2].col == 0


def test_track_move():
    trackLines, carts = day13.readfile('data/day13-test.txt')
    track = day13.Track(trackLines, carts)
    assert len(carts) == 2
    assert carts[0].row == 0 and carts[0].col == 2
    assert carts[1].row == 3 and carts[1].col == 9
    track.tick()
    assert carts[0].row == 0 and carts[0].col == 3  # moved right
    assert carts[1].row == 4 and carts[1].col == 9  # moved down
    assert carts[1].moverow == 0 and carts[1].movecol == 1  # turn left
    track.tick()
    assert carts[0].row == 0 and carts[0].col == 4  # moved right
    assert carts[1].row == 4 and carts[1].col == 10  # moved LEFT


def test_day13():
    collided = day13.day13(fname='data/day13-test.txt')
    print(
        f'Collision at col(x)={collided[0].col} and row(y)={collided[0].row}')
    # cart 1 at collision location
    assert collided[0].row == 3 and collided[0].col == 7
    # # cart 2 at collision location
    assert collided[1].row == 3 and collided[1].col == 7
    # but carts are heading in different directions ...
    assert collided[0].moverow != collided[1].moverow or collided[0].movecol != collided[1].movecol


def test_day_13_2():
    carts = day13.day13_2('data/day13-2-test.txt')
    assert len(carts) == 1
    assert carts[0].row == 4 and carts[0].col == 6
