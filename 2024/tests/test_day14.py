import day14


def test_read_data():
    data = day14.read_data("test_day14.txt")
    assert len(data) == 12, "Incorrect number of robots"
    robot = data[0]
    assert (
        robot.px == 0 and robot.py == 4 and robot.vx == 3 and robot.vy == -3
    ), "Incorrect robot"


def test_robot_position():
    day14.Robot.wide = 11
    day14.Robot.tall = 7
    robot = day14.Robot({"px": 2, "py": 4, "vx": 2, "vy": -3})
    positions = [(4, 1), (6, 5), (8, 2), (10, 6), (1, 3)]
    for i in range(5):
        robot.position(1)
        assert (
            robot.px == positions[i][0] and robot.py == positions[i][1]
        ), f"Incorrect position after {i+1} seconds"


def test_part1():
    data = day14.read_data("test_day14.txt")
    assert day14.part1(data, tall=7, wide=11) == 12
