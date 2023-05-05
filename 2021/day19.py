import utils


def readfile(filename):
    data = utils.read_file(filename)
    all_scanners = []
    scanner = set()
    for line in data:
        if line.startswith("---"):
            pass
        elif line == '':
            if len(scanner) > 0:
                all_scanners.append(scanner)
            scanner = set()
        else:
            x, y, z = line.split(",")
            scanner.add((x, y, z))
    else:
        all_scanners.append(scanner)
    return all_scanners


def differences(scanners):
    """
    Scanners are unaware of their position and their orientation; however, they can position the beacons relative to
    their own position. Using the difference between the beacons, it should be possible to find scanners with
    overlapping regions that have 12 or more identical beacons.
    """
    differences = set()
    origin = scanner[0]
    for scanner_number in range(1, len(scanners)):

if __name__ == '__main__':
    part_1 = None
    print("Day 19 - part 1", part_1)
    part_2 = None
    print("Day 18 - part 2", part_2)
