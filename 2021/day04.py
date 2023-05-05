from typing import Tuple

import utils

BingoNumbers = list[int]
BingoCard = list[list[int]]
BingoCards = list[BingoCard]


def read_file(filename: str) -> Tuple[BingoNumbers, BingoCards]:
    """Read bingo file:
       First line is sequence of numbers drawn.
       Separated by empty lines are the 5x5 bingo cards, e.g. first card line 2-6, second 8-12, third 14-18, ...
    """
    data = utils.read_file(filename)
    bingo_numbers = [int(item) for item in data[0].split(",")]
    number_of_bingo_cards = (len(data) - 1) // 6
    bingo_cards = []
    for idx in range(number_of_bingo_cards):
        bingo_cards.append(
            [int(number_on_card) for line in data[2 + idx * 6:7 + idx * 6] for number_on_card in line.split()])
    return bingo_numbers, bingo_cards


def bingo_card_full(bingo_cards: BingoCards, bingo_numbers_drawn: BingoNumbers) -> BingoCard:
    """Return winning bingo cards"""
    winners = []
    for bingo_card in bingo_cards:
        rows, cols = decompose_card(bingo_card)
        if has_bingo(rows+cols, bingo_numbers_drawn):
            winners.append(bingo_card)
    return winners[0] if len(winners) > 0 else None


def has_bingo(lines: list[list[int]], bingo_numbers_drawn: BingoNumbers) -> bool:
    """Do we have any line for which ALL numbers are drawn?"""
    return len(lines) > 0 and len(bingo_numbers_drawn) > 0 and \
           any(all(number in bingo_numbers_drawn for number in line) for line in lines)


def decompose_card(bingo_card: BingoCard) -> Tuple[list[int], list[int]]:
    """Decompose a bingo card in a list of rows and a list of columns"""
    rows = [bingo_card[i * 5:(i + 1) * 5] for i in range(5)]
    cols = [[bingo_card[i], bingo_card[5 + i], bingo_card[10 + i], bingo_card[15 + i], bingo_card[20 + i]] for i in
            range(5)]
    return rows, cols


def last_bingo_card_full(bingo_cards: BingoCards, bingo_numbers_drawn: BingoNumbers) -> BingoCard:
    """Return bingo card that wins LAST"""
    last_card_to_win = None
    for bingo_card in bingo_cards:
        rows, cols = decompose_card(bingo_card)
        if has_bingo(rows+cols, bingo_numbers_drawn):
            if len(bingo_cards) == 1:
                last_card_to_win = bingo_card
            bingo_cards.remove(bingo_card)
    return last_card_to_win


def part1(filename):
    bingo_numbers, bingo_cards = read_file(filename)
    numbers_drawn = []
    for bingo_round in range(len(bingo_numbers)):
        numbers_drawn = bingo_numbers[:bingo_round]
        winning_card = bingo_card_full(bingo_cards, numbers_drawn)
        if winning_card is not None:
            break
    numbers_not_drawn = sum([number for number in winning_card if number not in numbers_drawn])
    return numbers_drawn[-1] * numbers_not_drawn


def part2(filename):
    bingo_numbers, bingo_cards = read_file(filename)
    numbers_drawn = []
    for bingo_round in range(len(bingo_numbers)):
        numbers_drawn = bingo_numbers[:bingo_round]
        last_card_to_win = last_bingo_card_full(bingo_cards, numbers_drawn)
        if last_card_to_win is not None:
            break
    numbers_not_drawn = sum([number for number in last_card_to_win if number not in numbers_drawn])
    return numbers_drawn[-1] * numbers_not_drawn


if __name__ == '__main__':
    day04_1 = part1("data/day-04.txt")
    print("Day 04 - part 1", day04_1)
    day04_2 = part2("data/day-04.txt")
    print("Day 04 - part 2", day04_2)
