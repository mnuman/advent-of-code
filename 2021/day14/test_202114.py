# test_aoc_template.py
import sys
import os
import pytest
import aoc202114 as aoc      # replace aoc_template with the code file (e.g. 202101)
sys.path.extend(os.path.normpath(os.path.join(os.getcwd(), '../aocutils')))
import day14.fileutils


@pytest.fixture
def example1():
    puzzle_input = day14.fileutils.read_file("example1.txt")
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = day14.fileutils.read_file("example2.txt")
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == 'NNCB', "Incorrect starting material"
    assert len(example1[1]) == 16, "Incorrect number of inserts"
    assert example1[1]["CH"] == "B", "Incorrect mapping for pair CH"

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 1588, "Incorrect result"

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 2188189693529

