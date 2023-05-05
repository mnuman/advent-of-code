import utils


def get_data(filename):
    data = utils.read_file(filename)
    return [tuple(line.split(" ")) for line in data]


def adjust_position(current, instruction):
    """Adjust horizontal position, depth and aim based on instruction tuple"""
    horizontal_position, depth, aim = current

    action, quantity = instruction
    match action:
        case "up":
            if aim is None:
                depth -= int(quantity)
            else:
                aim -= int(quantity)
        case "down":
            if aim is None:
                depth += int(quantity)
            else:
                aim += int(quantity)
        case "forward":
            horizontal_position += int(quantity)
            if aim is not None:
                depth += aim * int(quantity)
    return horizontal_position, depth, aim


def process_instructions(start, instructions):
    """Apply all instructions from current pos; return resulting position"""
    current = start
    for instruction in instructions:
        current = adjust_position(current, instruction)
    return current


if __name__ == '__main__':
    day02_1 = process_instructions((0, 0, None), get_data("data/day-02.txt"))
    print("Day 02 - part 1", day02_1[0] * day02_1[1])
    day02_2 = process_instructions((0, 0, 0), get_data("data/day-02.txt"))
    print("Day 02 - part 2", day02_2[0] * day02_2[1])
