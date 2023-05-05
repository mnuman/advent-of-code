import day04


def test_readfile():
    bingo_numbers, bingo_cards = day04.read_file("data/test-day-04.txt")
    assert isinstance(bingo_numbers, list), 'Bingo numbers should be a list'
    assert len(bingo_numbers) == 27, "Correct number of entries in bingo numbers"
    assert isinstance(bingo_cards, list)
    assert len(bingo_cards) == 3, "Correct number of bingo cards"


def test_decompose_card():
    rows, cols = day04.decompose_card([i for i in range(26)])
    assert len(rows) == 5
    assert len(cols) == 5
    assert rows == [[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14],
                    [15, 16, 17, 18, 19],
                    [20, 21, 22, 23, 24]]
    assert cols == [[0, 5, 10, 15, 20],
                    [1, 6, 11, 16, 21],
                    [2, 7, 12, 17, 22],
                    [3, 8, 13, 18, 23],
                    [4, 9, 14, 19, 24]]


def test_has_bingo():
    bingo_lines = [[0, 1, 2, 3, 4],[0, 5, 10, 15, 20]]
    assert not day04.has_bingo(bingo_lines, []), "No bingo if no numbers have been drawn"
    assert not day04.has_bingo(bingo_lines, [4,3,2,1]), "No bingo if not all numbers have been drawn"
    assert day04.has_bingo(bingo_lines, [i for i in range(5)]), "Bingo if  all numbers have been drawn for a line (row)"
    assert day04.has_bingo(bingo_lines, [i*5 for i in range(5)]), "Bingo if  all numbers have been drawn for a line (column)"


def test_part_1():
    assert day04.part1("data/test-day-04.txt") == 4512, "Test data for part 1 should return 4512"


def test_part_2():
    assert day04.part2("data/test-day-04.txt") == 1924, "Test data for part 2 should return 148*13"
