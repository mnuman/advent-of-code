from collections import namedtuple

coordinates = namedtuple('coordinates', ['x', 'y'])


def next_position_velocity(current_pos, current_velocity):
    next_position = coordinates(current_pos.x + current_velocity.x, current_pos.y + current_velocity.y)
    next_velocity = coordinates(
        0 if current_velocity.x == 0 else current_velocity.x - 1 if current_velocity.x > 0 else current_velocity.x + 1,
        current_velocity.y - 1)
    return next_position, next_velocity


def position_in_target_area(position, min_x, max_x, min_y, max_y):
    return min_x <= position.x <= max_x and min_y <= position.y <= max_y


def calculate_trajectory(initial_velocity, min_x, max_x, min_y, max_y):
    trajectory = [coordinates(0, 0)]
    velocity = initial_velocity
    hit_target = False
    while not hit_target:
        position, velocity = next_position_velocity(trajectory[-1], velocity)
        if position.y < min_y:  # if below target, we're never going to make it back as y is steadily decreasing
            trajectory = None
            break
        trajectory.append(position)
        hit_target = position_in_target_area(position, min_x, max_x, min_y, max_y)
    return trajectory


# let's brute force the velocities for part-1
def part1(min_x, max_x, min_y, max_y):
    all_trajectories = []
    for vel_x in range(30):
        for vel_y in range(80):
            t = calculate_trajectory(coordinates(vel_x, vel_y), min_x, max_x, min_y, max_y)
            if t is not None:
                all_trajectories.append(t)
    return all_trajectories


def highest_y(trajectories):
    return max([sorted(t, reverse=True, key=lambda p: p.y)[0] for t in trajectories])


def part2(min_x, max_x, min_y, max_y):
    """
    The velocity in x-direction must be > 0 to reach the target in x-direction and decreases to 0.
    t=0: x=0
    t=1: x=vx0, vx=vx0-1
    t=2: x=vx0+vx0-1, vx=vx0-2
    :
    t=n: x = n*vx0 - (1+2+...+n-1) = n(vx0 - (n-1)/2)
    """
    all_x_velocities = set(
        [v for v in range(1, max_x + 1) for n in range(1, 2 * v + 3) if min_x <= n * (v - (n - 1) / 2) <= max_x])
    candidates, results = 0, 0
    for velocity_x in all_x_velocities:
        for velocity_y in range(min_y, 500):
            candidates += 1
            if candidates % 250 == 0:
                print(f"Calculating {velocity_x, velocity_y}")
            if calculate_trajectory(coordinates(velocity_x, velocity_y), min_x, max_x, min_y, max_y):
                results += 1
    return results


if __name__ == '__main__':
    part_1 = highest_y(part1(241, 275, -75, -49))
    print("Day 17 - part 1", part_1)
    part_2 = part2(241, 275, -75, -49)
    print("Day 17 - part 2", part_2)
