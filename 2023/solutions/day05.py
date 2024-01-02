"""
--- Day 5: If You Give A Seed A Fertilizer --- You take the boat and find the
gardener right where you were told he would be: managing a giant "garden" that
looks more to you like a farm. "A water source? Island Island is the water
source!" You point out that Snow Island isn't receiving any water. "Oh, we had
to stop the water because we ran out of sand to filter it with! Can't make snow
with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned
off the water a few days... weeks... oh no." His face sinks into a look of
horrified realization. "I've been so busy making sure everyone here has food
that I completely forgot to check why we stopped getting more sand! There's a
ferry leaving soon that is headed over in that direction - it's much faster than
your boat. Could you please go check it out?" You barely have time to agree to
this request when he brings up another. "While you wait for the ferry, maybe you
can help us with our food production problem. The latest Island Island Almanac
just arrived and we're having trouble making sense of it." The almanac (your
puzzle input) lists all of the seeds that need to be planted. It also lists what
type of soil to use with each kind of seed, what type of fertilizer to use with
each kind of soil, what type of water to use with each kind of fertilizer, and
so on. Every type of seed, soil, fertilizer and so on is identified with a
number, but numbers are reused by each category - that is, soil 123 and
fertilizer 123 aren't necessarily related to each other. For example:

seeds: 79 14 55 13

seed-to-soil map: 50 98 2 52 50 48

soil-to-fertilizer map: 0 15 37 37 52 2 39 0 15

fertilizer-to-water map: 49 53 8 0 11 42 42 0 7 57 7 4

water-to-light map: 88 18 7 18 25 70

light-to-temperature map: 45 77 23 81 45 19 68 64 13

temperature-to-humidity map: 0 69 1 1 0 69

humidity-to-location map: 60 56 37 56 93 4

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55,
and 13. The rest of the almanac contains a list of maps which describe how to
convert numbers from a source category into numbers in a destination category.
That is, the section that starts with seed-to-soil map: describes how to convert
a seed number (the source) to a soil number (the destination). This lets the
gardener and his team know which soil to use with which seeds, which water to
use with which fertilizer, and so on. Rather than list every source number and
its corresponding destination number one by one, the maps describe entire ranges
of numbers that can be converted. Each line within a map contains three numbers:
the destination range start, the source range start, and the range length.
Consider again the example seed-to-soil map:

50 98 2 52 50 48

The first line has a destination range start of 50, a source range start of 98,
and a range length of 2. This line means that the source range starts at 98 and
contains two values: 98 and 99. The destination range is the same length, but it
starts at 50, so its two values are 50 and 51. With this information, you know
that seed number 98 corresponds to soil number 50 and that seed number 99
corresponds to soil number 51. The second line means that the source range
starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a
destination range starting at 52 and also containing 48 values: 52, 53, ..., 98,
99. So, seed number 53 corresponds to soil number 55. Any source numbers that
aren't mapped correspond to the same destination number. So, seed number 10
corresponds to soil number 10. So, the entire list of seed numbers and their
corresponding soil numbers looks like this:

seed  soil 0     0 1     1 ...   ... 48    48 49    49 50    52 51    53 ...
... 96    98 97    99 98    50 99    51

With this map, you can look up the soil number required for each initial seed
number:

    Seed number 79 corresponds to soil number 81. Seed number 14 corresponds to
    soil number 14. Seed number 55 corresponds to soil number 57. Seed number 13
    corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so they'd
like to know the closest location that needs a seed. Using these maps, find the
lowest location number that corresponds to any of the initial seeds. To do this,
you'll need to convert each seed number through other categories until you can
find its corresponding location number. In this example, the corresponding types
are:

    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78,
    humidity 78, location 82. Seed 14, soil 14, fertilizer 53, water 49, light
    42, temperature 42, humidity 43, location 43. Seed 55, soil 57, fertilizer
    57, water 53, light 46, temperature 82, humidity 82, location 86. Seed 13,
    soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35,
    location 35.

So, the lowest location number in this example is 35. What is the lowest
location number that corresponds to any of the initial seed numbers? Your puzzle
answer was 157211394. The first half of this puzzle is complete! It provides one
gold star: * --- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading
the almanac, it looks like the seeds: line actually describes ranges of seed
numbers. The values on the initial seeds: line come in pairs. Within each pair,
the first value is the start of the range and the second value is the length of
the range. So, in the first line of the example above: seeds: 79 14 55 13 This
line describes two ranges of seed numbers to be planted in the garden. The first
range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
The second range starts with seed number 55 and contains 13 values: 55, 56, ...,
66, 67. Now, rather than considering four seed numbers, you need to consider a
total of 27 seed numbers. In the above example, the lowest location number can
be obtained from seed number 82, which corresponds to soil 84, fertilizer 84,
water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest
location number is 46. Consider all of the initial seed numbers listed in the
ranges on the first line of the almanac. What is the lowest location number that
corresponds to any of the initial seed numbers?
"""
from dataclasses import dataclass
from typing import Generator, Optional
import file_utils as u


@dataclass(frozen=True)
class ValueRange:
    start: int
    end: int


class Range:
    def __init__(self, start: int, length: int, destination: int):
        self.start: int = start
        self.end: int = start + length - 1
        self.destination: int = destination

    def in_range(self, val) -> Optional[int]:
        return val - self.start + self.destination \
            if self.start <= val <= self.end else None

    def is_candidate(self, s: int, e: int) -> bool:
        """Is this a candidate for mapping? """
        return not (self.end < s or self.start > e)

    def project_range(self, s: int, e: int) -> tuple[int, int]:
        assert self.is_candidate(s, e)
        return (
            self.destination - self.start + s,
            self.destination - self.start + min(e, self.end)
        )


def select_mapping(mappings: list[Range], s: int, e: int) -> Optional[Range]:
    """Select the mapping that applies to the given range and has the smallest
    source start value"""
    candidates: list[Range] = [m for m in mappings if m.is_candidate(s, e)]
    candidates.sort(key=lambda x: x.start)
    return candidates[0] if len(candidates) > 0 else None


def parse_file(lines: list[str]) -> tuple[list[int], dict[str, list[Range]]]:
    seeds: list[int] = []
    almanac: dict[str, list[Range]] = dict()
    current_list = list()
    for line in lines:
        parts = line.split()
        match parts:
            case ["seeds:", *values]:
                seeds = [int(v) for v in values]
            case [mapname, "map:"]:
                current_list = list()
                almanac[mapname] = current_list
            case [target, start, number_of_elements]:
                current_list.append(
                    Range(int(start), int(number_of_elements), int(target)))
    return seeds, almanac


def parse_file_v2(lines: list[str]) -> tuple[list[ValueRange], dict[str, list[Range]]]:
    """Similar to the first version, but now the seeds are also ranges"""
    seeds: list[ValueRange] = []
    almanac: dict[str, list[Range]] = dict()
    current_list = list()
    for i, line in enumerate(lines):
        parts = line.split()
        match parts:
            case ["seeds:", *values]:
                seeds = [
                    ValueRange(int(values[2*i]),
                               int(values[2*i]) + int(values[2*i+1]) - 1)
                    for i in range(int(len(values)/2))]
            case [mapname, "map:"]:
                current_list = list()
                almanac[mapname] = current_list
            case [target, start, number_of_elements]:
                current_list.append(
                    Range(int(start), int(number_of_elements), int(target)))

    # sort lists by increasing start position
    for k in almanac:
        almanac[k].sort(key=lambda x: x.start)
    seeds.sort(key=lambda x: x.start)

    return seeds, almanac


def lookup(almanac, name: str, value: int) -> int:
    for r in almanac[name]:
        target_value: Optional[int] = r.in_range(value)
        if target_value is not None:
            return target_value
    return value


def part1(fname: str) -> int:
    lines = u.read_file(fname)
    seeds, almanac = parse_file(lines)

    soils: Generator[int, None, None] = (
        lookup(almanac, "seed-to-soil", s) for s in seeds)
    fertilizers: Generator[int, None, None] = (
        lookup(almanac, "soil-to-fertilizer", s) for s in soils)
    waters: Generator[int, None, None] = (
        lookup(almanac, "fertilizer-to-water", s) for s in fertilizers)
    lights: Generator[int, None, None] = (
        lookup(almanac, "water-to-light", s) for s in waters)
    temperatures: Generator[int, None, None] = (
        lookup(almanac, "light-to-temperature", s) for s in lights)
    humidities: Generator[int, None, None] = (
        lookup(almanac, "temperature-to-humidity", s) for s in temperatures)
    locations: Generator[int, None, None] = (
        lookup(almanac, "humidity-to-location", s) for s in humidities)
    return min(locations)


def transform(range: ValueRange, mappings: list[Range]) -> list[ValueRange]:
    """Use the supplied mapping to map an input range to a list of output ranges"""
    current_pos = range.start
    result: list[ValueRange] = []
    done: bool = False
    while not done:
        done = True
        # mapping to be applied is candidate with smallest start
        m = select_mapping(mappings, current_pos, range.end)
        if m is not None:
            done = False
            if m.start > current_pos:
                result.append(ValueRange(current_pos, m.start - 1))
                current_pos = m.start
            start_match, end_match = m.project_range(current_pos, range.end)
            result.append(ValueRange(start_match, end_match))
            current_pos += end_match - start_match + 1
        else:
            done = True
        done = done or current_pos > range.end
    # left-over mapping
    if current_pos < range.end:
        result.append(ValueRange(current_pos, range.end))
    result.sort(key=lambda x: x.start)
    return result


def part2(fname: str) -> int:
    lines = u.read_file(fname)
    seeds, almanac = parse_file_v2(lines)
    maps: list[str] = [
        "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
        "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    inputs = seeds
    for m in maps:
        mapping = almanac[m]
        outputs = []
        for i in inputs:
            outputs += transform(i, mapping)
        outputs.sort(key=lambda x: x.start)
        inputs = outputs
    return inputs[0].start


if __name__ == "__main__":
    print(f"Result for part1 : {part1("day05.txt")}")
    print(f"Result for part2 : {part2("day05.txt")}")
