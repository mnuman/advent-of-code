import utils
import math
delimiters = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part1(filename):
    data = utils.read_file(filename)
    score = 0
    for line in data:
        expected_closures = []
        for c in line:
            if c in delimiters.keys():
                expected_closures.append(delimiters[c])
            else:
                if c == expected_closures[-1]:
                    expected_closures.pop(-1)
                else:
                    score += scores[c]
                    break
    return score


def part2(filename):
    data = utils.read_file(filename)
    score = []
    for line in data:
        expected_closures = []
        illegal = False
        line_score = 0
        for c in line:
            if c in delimiters.keys():
                expected_closures.append(delimiters[c])
            else:
                if c == expected_closures[-1]:
                    expected_closures.pop(-1)
                else:
                    illegal = True
        if not illegal:
            expected_closures.reverse()
            for cl in expected_closures:
                line_score = 5 * line_score + completion_score[cl]
            score.append(line_score)
    return sorted(score)[math.floor(len(score)//2)]


if __name__ == '__main__':
    day10_1 = part1("data/day-10.txt")
    print("Day 10 - part 1", day10_1)
    day10_2 = part2("data/day-10.txt")
    print("Day 10 - part 2", day10_2)
