import file_utils as f
from copy import deepcopy


def read_data(fname: str):
    data = f.read_file(fname)
    diskmap = []
    files = {}
    freespace = []
    idx = 0
    for i, block_count in enumerate([c for c in data[0]]):
        file_marker = i // 2 if i % 2 == 0 else None
        for i in range(int(block_count)):
            diskmap.append(file_marker)
        block_range = (idx, idx + int(block_count))
        if file_marker is not None:
            files[file_marker] = block_range
        else:
            freespace.append(block_range)
        idx += int(block_count)
    return diskmap, files, freespace


def part1(diskmap):
    data = deepcopy(diskmap)
    idx = 0
    back_idx = len(data) - 1
    while idx < len(data) and back_idx > idx:
        if data[idx] is None:
            while back_idx > idx and data[back_idx] is None:
                back_idx -= 1
            if back_idx > idx:
                data[idx], data[back_idx] = data[back_idx], data[idx]
                back_idx -= 1
            else:
                break
        idx += 1
    return sum(i * int(f) for i, f in enumerate(data) if f is not None)


def find_file_to_move(files, empty_space):
    files = [
        k
        for k, v in files.items()
        if v[1] - v[0] <= empty_space[1] - empty_space[0] and v[0] >= empty_space[0]
    ]
    return files[-1] if files else None


def part2(files, freespace):
    freespace.reverse()
    while freespace:
        empty_space = freespace.pop()
        while empty_space[0] < empty_space[1]:
            file_to_be_moved = find_file_to_move(files, empty_space)
            if file_to_be_moved is not None:
                # print(f"Moving file {file_to_be_moved} to {empty_space}")
                file_start, file_end = files[file_to_be_moved]
                files[file_to_be_moved] = (
                    empty_space[0],
                    empty_space[0] + file_end - file_start,
                )
            empty_space = (empty_space[0] + file_end - file_start, empty_space[1])
    return sum(k * b for k, v in files.items() for b in range(v[0], v[1]))


if __name__ == "__main__":
    data, files, freespace = read_data("day09.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(files, freespace)}")
