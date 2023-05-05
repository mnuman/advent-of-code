from collections import Counter

import day06


def test_read_file():
    fish_data = day06.read_file("data/test-day-06.txt")
    assert fish_data.total() == 5, "Five fish initially"
    assert sorted(fish_data.keys()) == [1, 2, 3, 4], "Correct keys are present"


def test_calculate_next_generation():
    c = Counter()
    for i in range(1, 8):
        c[i] = i
    next_gen = day06.calculate_next_generation(c)
    assert next_gen.total() == 1 + 2 + 3 + 4 + 5 + 6 + 7
    assert next_gen[0] == 1, "One about to spawn"
    assert next_gen[8] == 0, "No new spawn yet"
    assert next_gen[6] == 7, "Seven fish aged one day"


def test_18_days():
    current_generation = day06.read_file("data/test-day-06.txt")
    for i in range(18):
        next_generation = day06.calculate_next_generation(current_generation)
        current_generation = next_generation
    assert current_generation.total() == 26, "Need 26 fish after 18 days"


def test_part1():
    after_80_generations = day06.part1("data/test-day-06.txt")
    assert after_80_generations == 5934, "After 80 days we should have 5934 fish"

def test_part2():
    after_256_generations = day06.part2("data/test-day-06.txt")
    assert after_256_generations == 26984457539, "After 256 days we should have 26984457539 fish"

