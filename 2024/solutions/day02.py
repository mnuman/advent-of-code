import file_utils as f


def read_data(fname: str) -> list[list[int]]:
    data = f.read_file(filename=fname)
    return [[int(entry) for entry in line.split()] for line in data]


def diff_adjacents(report: list[int]) -> list[int]:
    return [e1 - e2 for e1, e2 in zip(report, report[1:])]


def safe_levels(report: list[int]):
    diffs = diff_adjacents(report)
    return all([1 <= d <= 3 for d in diffs]) or all([-3 <= d <= -1 for d in diffs])


def part1(data: list[list[int]]) -> int:
    result = 0
    for report in data:
        if safe_levels(report):
            result += 1
    return result


def part2(data: list[list[int]]) -> int:
    result = 0
    for report in data:
        if safe_levels(report):
            result += 1
        else:
            # brute force: just because we can - and it's way easier.
            offender_idx = 0
            while offender_idx < len(report):
                dampened_report = report[:offender_idx:] + report[offender_idx + 1 :]
                if safe_levels(dampened_report):
                    result += 1
                    break
                offender_idx += 1
    return result


if __name__ == "__main__":
    data = read_data("day02.txt")
    print(f"Safe readings: {part1(data)}")
    print(f"Safe readings: {part2(data)}")
