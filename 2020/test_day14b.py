import day14a
import day14b


def test_resval():
    assert day14b.resval('0', '1') == '1'
    assert day14b.resval('1', '1') == '1'
    assert day14b.resval('0', '0') == '0'
    assert day14b.resval('1', '0') == '1'
    assert day14b.resval('', 'X') == ('0', '1')


def test_find_mem_addresses():
    assert day14b.find_mem_addresses(bit_addr="0" * 36, mask="0" * 36) == [0]
    assert day14b.find_mem_addresses(bit_addr="0" * 36,
                                     mask="0" * 35 + 'X') == [0, 1]
    assert day14b.find_mem_addresses(bit_addr="0" * 36,
                                     mask="0" * 30 + 'XXXXXX') == \
           [i for i in range(0, 64)]
    assert day14b.find_mem_addresses(bit_addr="0" * 34 + '11',
                                     mask="0" * 33 + "X00") \
           == [3, 7]


def test_scenario():
    instructions = day14a.parse_instructions("data/test_day14b.txt")
    p = day14b.V2_Processor()
    for i in instructions:
        p.process(i)
    assert p.sum_values() == 208
