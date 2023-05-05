import day08a


def test_fetch_instructions():
    ops = day08a.fetch_instructions("data/test_day08.txt")
    assert len(ops) == 9
    assert ops[0] == ("nop", 0)
    assert ops[8] == ("acc", 6)


def test_get_instruction():
    p = [("nop", 0), ("nop", 1)]
    executor = day08a.Program(p)
    assert executor.get_instruction() == ("nop", 0)


def test_stop_always():
    def stop_always(instructions, program_counter):
        return True

    # no code executed - accumulator is still 0, program counter = 0, list of executed numbers empty
    p = [("nop", 0), ("nop", 1)]
    executor = day08a.Program(p)
    assert executor.execute(stop_always, 10) == (0, 0, [])


def test_stop_first():
    def stop_first(instructions, program_counter):
        return program_counter > 0

    # single instruction nop 0 executed, acc = 0, pc = 1, list = [0]
    p = [("nop", 0), ("nop", 1)]
    executor = day08a.Program(p)
    assert executor.execute(stop_first, 10) == (0, 1, [0])


def test_stop_jmp():
    def stop_first(instructions, program_counter):
        return program_counter > 0

    # single instruction jmp 2 executed, acc = 0, pc = 2, list = [0]
    p = [("jmp", 2), ("nop", 1), ("nop", 2)]
    executor = day08a.Program(p)
    assert executor.execute(stop_first, 10) == (0, 2, [0])


def test_stop_acc():
    def stop(instructions, program_counter):
        return program_counter > 1

    # single instruction nop 0 executed, acc = 0, pc = 1, list = [0]
    p = [("acc", 7), ("nop", 1), ("nop", 2)]
    executor = day08a.Program(p)
    assert executor.execute(stop, 10) == (7, 2, [0, 1])


def test_scenario():
    pgm = day08a.fetch_instructions("data/test_day08.txt")
    executor = day08a.Program(pgm)
    assert executor.execute(day08a.stop_on_loop) == (5, 1, [0, 1, 2, 6, 7, 3, 4])


def test_stop_on_loop():
    assert not day08a.stop_on_loop([], 0)
    assert not day08a.stop_on_loop([1, 2, 3], 0)
    assert day08a.stop_on_loop([1, 2, 3], 1)
