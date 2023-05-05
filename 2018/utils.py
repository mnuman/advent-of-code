"""Module hosting miscellaneous utility functions for my
attempts of advent of code 2018"""


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
                field for line in content for field in line.strip().split(separator)]
        else:
            result = [
                int(field) for line in content for field in line.strip().split(separator)]
    return result
