from day17 import *


def test_next_position_velocity():
    current_pos = coordinates(0, 0)
    current_velocity = coordinates(0, 0)
    next_position, next_velocity = next_position_velocity(current_pos, current_velocity)
    assert next_position == coordinates(0, 0) and next_velocity == coordinates(0, -1)

    current_velocity = coordinates(6, 3)
    next_position, next_velocity = next_position_velocity(current_pos, current_velocity)
    assert next_position == coordinates(6, 3) and next_velocity == coordinates(5, 2)
    next_position, next_velocity = next_position_velocity(next_position, next_velocity)
    assert next_position == coordinates(11, 5) and next_velocity == coordinates(4, 1)
    next_position, next_velocity = next_position_velocity(next_position, next_velocity)
    assert next_position == coordinates(15, 6) and next_velocity == coordinates(3, 0)


def test_calculate_trajectory():
    trajectory = calculate_trajectory(coordinates(7, 2), 20, 30, -10, -5)
    assert 20 <= trajectory[-1].x <= 30 and -10 <= trajectory[-1].y <= -5


def test_part1():
    all_trajectories = part1(20, 30, -10, -5)
    assert all([position_in_target_area(t[-1], 20, 30, -10, -5) for t in all_trajectories])
    assert highest_y(all_trajectories).y == 45


def test_part2():
    all_velocities = part2(20, 30, -10, -5)
    assert len(all_velocities) == 112
