"""Confident that your list of box IDs is complete, you're ready to find 
the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same 
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters 
(the second and fourth). However, the IDs fghij and fguij differ by 
exactly one character, the third (h and u). Those must be the correct 
boxes.

What letters are common between the two correct box IDs? (In the example 
above, this is found by removing the differing character from either ID, 
producing fgij.)
"""
import utils


def read(fname):
    boxes = utils.read_file(fname)
    return boxes


def compare(boxes):
    for i in range(0, len(boxes)):
        for j in range(i+1, len(boxes)):
            # print(f"Comparing box {i} and {j}")
            matched, overlap = compare_strings(boxes[i], boxes[j])
            if matched:
                print(boxes[i])
                print(boxes[j])
                print(overlap)
                return


def compare_strings(s1, s2):
    """Brute force compare strings"""
    assert len(s1) == len(s2)
    diffs = 0
    i = 0
    while diffs < 2 and i < len(s1):
        if s1[i] != s2[i]:
            diffs += 1
        i += 1
    if diffs == 1:
        overlaps = [s1[i] for i in range(0, len(s1)) if s1[i] == s2[i]]
        return (True, ''.join(overlaps))
    else:
        return (False, None)


if __name__ == '__main__':
    compare(read('data/day2-input.txt'))
"""
cvgywxqubnuaefmsldjdrpfzyi
cvgywxqubnuaefmslkjdrpfzyi
cvgywxqubnuaefmsljdrpfzyi
"""
