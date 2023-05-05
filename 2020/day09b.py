"""
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you
must find a contiguous set of at least two numbers in your list which sum to the invalid number
from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from
step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous
range; in this example, these are 15 and 47, producing 62.

"""
import day09a


def find_sum(xm_list, target_idx):
    """ Find which contiguous set of numbers adds up to the number at target_idx"""
    target = xm_list[target_idx]
    for contiguous_size in range(2, target_idx):  # size of contiguous_set
        for start_idx in range(0, target_idx - contiguous_size):
            if target == sum(xm_list[start_idx:start_idx + contiguous_size]):
                hitlist = xm_list[start_idx:start_idx + contiguous_size]
                return hitlist, sum(hitlist), min(hitlist) + max(hitlist)


if __name__ == "__main__":
    xmas_list = day09a.parse_xmas_list("data/day09.txt")
    first_mismatch = day09a.first_non_sum(xmas_list)
    print(f"The first number to not be the sum of the 25 previous is "
          f"{first_mismatch[0]} at position {first_mismatch[1]} i.e python idx "
          f"{first_mismatch[1] - 1}")
    result = find_sum(xmas_list, first_mismatch[1] - 1)
    print(f"This is the sum of {result[0]} because this range sums up to {result[1]}, the sum of "
          f"the minimum and maximum numbers in this range is {result[2]}")
