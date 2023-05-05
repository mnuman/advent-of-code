import day14a


def test_parse_instructions():
    instructions = day14a.parse_instructions("data/test_day14.txt")
    assert len(instructions) == 4
    assert instructions[0] == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    assert instructions[3] == (8, 0)


def test_resval():
    assert day14a.resval('0', '1') == '1'
    assert day14a.resval('0', '0') == '0'
    assert day14a.resval('0', 'X') == '0'
    assert day14a.resval('1', 'X') == '1'


def test_determine_value():
    processor = day14a.Processor()
    processor.mask = "X" * 36
    assert processor.determine_value(128) == 128
    processor.mask = "000000000000000000000000000000000X11"
    assert processor.determine_value(128) == 3
    assert processor.determine_value(132) == 7


def test_process_instruction():
    processor = day14a.Processor()
    assert processor.mask is None
    processor.process("000000000000000000000000000000000X11")
    assert processor.mask == "000000000000000000000000000000000X11"
    processor.process("X" * 36)
    processor.process((0, 217))
    assert len(processor.mem.keys()) == 1
    assert processor.mem[0] == 217


def test_sum():
    processor = day14a.Processor()
    processor.process("X" * 36)
    processor.process((0, 217))
    processor.process((1, 42))
    assert processor.sum_values() == 259


def test_scenario():
    instructions = day14a.parse_instructions("data/test_day14.txt")
    processor = day14a.Processor()
    [processor.process(i) for i in instructions]
    assert processor.sum_values() == 165
