"""Module hosting miscellaneous utility functions for my
attempts of advent of code 2021"""


def toint(s):
    """Inline conversion function from string to integer"""
    return int(s)


def read_file(filename, separator=None, convert=None):
    """Parse input file, return a list of stripped lines; if separator is
       specified, break up the individual lines on the separator as well
    """
    with open(filename) as f:  # pylint: disable=C0103
        content = f.readlines()
    if separator is None:
        if convert is None:
            result = [line.strip() for line in content]
        else:
            result = [convert(line.strip()) for line in content]
    else:
        if convert is None:
            result = [
                field for line in content
                for field in line.strip().split(separator)]
        else:
            result = [
                convert(field) for line in content
                for field in line.strip().split(separator)]
    return result


def binary_to_int(binary_number: str) -> int:
    """Convert a binary number represented as a string to its integer value"""
    return int(binary_number, 2)


def hello():
    print("hello")
