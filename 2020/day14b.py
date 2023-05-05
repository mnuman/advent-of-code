"""
--- Part Two ---

For some reason, the sea port's computer system still can't communicate with
your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all.
Instead, it acts as a memory address decoder. Immediately before a value is
written to memory, each bit in the bitmask modifies the corresponding bit of
the destination memory address in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is
    overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates
unpredictably. In practice, this means the floating bits will take on all
possible values, potentially causing many memory addresses to be written all
at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1

When this program goes to write to memory address 42, it first applies the
bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X

After applying the mask, four bits are overwritten, three of which are
different, and two of which are floating. Floating bits take on every
possible combination of values; with two floating bits, four actual memory
addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)

Next, the program is about to write to memory address 26 with a different
bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX

This results in an address with three floating bits, causing writes to eight
memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)

The entire 36-bit address space still begins initialized to the value 0 at
every address, and you still need the sum of all values left in memory at the
end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder
chip. What is the sum of all values left in memory after it completes?

"""
import day14a


def resval(b, m):
    if m == '1':
        return m
    elif m == '0':
        return b
    else:
        return '0', '1'


def find_mem_addresses(bit_addr, mask):
    current = ['']
    for (b, m) in zip(bit_addr, mask):
        result_bits = resval(b, m)
        new = []
        for a in current:
            for b in result_bits:
                new.append(a + b)
        current = new
    return [int(a, 2) for a in current]


class V2_Processor(day14a.Processor):
    def process(self, instruction):
        if isinstance(instruction, str):
            self.mask = instruction
        else:
            self.set_mem(address=instruction[0], value=instruction[1])

    def set_mem(self, address, value):
        bit_addr = "{0:0>36b}".format(address)
        for address in find_mem_addresses(bit_addr, self.mask):
            self.mem[address] = value

    def determine_value(self, value):
        bit_value = "{0:0>36b}".format(value)
        # iterate over multiple lists simultaneously, use corresponding elements
        return int(
            ''.join([resval(b, m) for (b, m) in zip(bit_value, self.mask)]), 2)

    def sum_values(self):
        return sum(self.mem.values())


if __name__ == "__main__":
    instructions = day14a.parse_instructions("data/day14.txt")
    p = V2_Processor()
    for i in instructions:
        p.process(i)
    print(f"The resulting sum is: {p.sum_values()}")
