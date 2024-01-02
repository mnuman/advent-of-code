from day01 import extract_number, extract_number_or_spelled_out_number
import file_utils as u


def test_extract_number():
    extracted_numbers = [
        extract_number(line) for line in u.read_file(filename="test_day01_1.txt")
    ]
    assert extracted_numbers == [12, 38, 15, 77]


def test_extract_number_v2():
    extracted_numbers = [
        extract_number_or_spelled_out_number(line)
        for line in u.read_file(filename="test_day01_2.txt")
    ]
    assert extracted_numbers == [29, 83, 13, 24, 42, 14, 76]
    # special case for overlapping patterns
    assert (
        extract_number_or_spelled_out_number("sevenine") == 79
    ), "Overlapped not handled correctly!"
