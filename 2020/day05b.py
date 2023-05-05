"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this
aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
"""
import day05a
import utils

if __name__ == '__main__':
    seats = [day05a.seat_number(day05a.seatposition(boarding_pass)) for boarding_pass in
             utils.read_file('data/day05.txt')]
    # your seat is not in the very front or back - should be just one result
    missing_seats = []
    for seat_number in range(min(seats), max(seats) + 1):
        if seat_number not in seats:
            missing_seats.append(seat_number)

    print(f"Missing seats: {missing_seats}")
