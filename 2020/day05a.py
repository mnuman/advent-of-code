"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is
yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport
control.
You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
perhaps you can find your seat through process of elimination.
Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified
like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
(numbered 0 through 127). Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63)
or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until
you're left with exactly one row.
For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps.
L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the
seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""
import utils


def seatposition(boarding_pass, row_indicators=7):
    """ Determine the row/col numbers on the boarding pass code by converting to binary representation
    :param boarding_pass: boarding pass code
    :param row_indicators: use this number of positions as row indicators
    :return: (row, col)
    """
    bin_string = ''.join(['0' if c in ['F', 'L'] else '1' for c in boarding_pass])
    return int(bin_string[:row_indicators], 2), int(bin_string[row_indicators:], 2)


def seat_number(position):
    return position[0] * 8 + position[1]


if __name__ == '__main__':
    highest = max([seat_number(seatposition(boarding_pass)) for boarding_pass in utils.read_file('data/day05.txt')])
    print(f'The highest seat number is {highest}')
