import file_utils as f
import parse


"""
Notes:
- three bit instructions, followed by three bit opcode
- three registers (A,B,C) capable of holding any integer value
- instruction pointer, incremented by 2 except for jump instructions
- halt if instruction pointer beyond end of program
- operands:
 - 0 to 3: literal value
 - 4 to 6: value of register A,B,C respectively
 - 7 reserved - should not occur in valid programs!

 opcodes:
 - 0: adv, A = A // 2^combo-operand
 - 1: bxl, B = B xor literal-operand
 - 2: bst, B = combo-operand % 8 (i.e. keeping only lowest 3 bits)
 - 3: jnz, if A != 0, jump to instruction pointer + literal-operand
 - 4: bxc, B = B xor C (operand ignored)
 - 5: out, evaluate combo-operand % 8 and output to terminal
 - 6: bdv, B = A // 2^combo-operand
 - 7: cdv, C = A // 2^combo-operand
"""


class ThreeBitMachine:
    def __init__(self, a, b, c, program):
        self.ip = 0
        self.outputs = []
        self.A = a
        self.B = b
        self.C = c
        self.program = program
        self.operations = 0

    def __str__(self):
        return f"ThreeBitMachine(A={self.A}, B={self.B}, C={self.C}, program={self.program})"

    def __repr__(self):
        return f"ThreeBitMachine: A={self.A}, B={self.B}, C={self.C}, program={self.program}, ip={self.ip}, outputs={self.outputs}"

    def execute(self, operation):
        self.operations += 1
        opcode, operand = operation
        match opcode:
            case 0:
                self.A = self.A // 2 ** self.value(operand)
            case 1:
                self.B = self.B ^ self.value(operand, combo=False)
            case 2:
                self.B = self.value(operand) % 8
            case 3:
                if self.A != 0:
                    self.ip = self.value(operand)
                    return
            case 4:
                self.B = self.B ^ self.C
            case 5:
                self.outputs.append(self.value(operand) % 8)
            case 6:
                self.B = self.A // 2 ** self.value(operand)
            case 7:
                self.C = self.A // 2 ** self.value(operand)
            case _:
                raise ValueError(f"Invalid opcode: {opcode}")
        self.ip += 2

    def value(self, operand, combo=True):
        if not combo or operand < 4:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise ValueError(f"Invalid operand: {operand}")

    def run(self):
        while self.ip < len(self.program) and self.operations < 10000:
            self.execute(self.program[self.ip : self.ip + 2])


def read_data(fname: str):
    data = f.read_file(fname)
    a = parse.parse("Register A: {a:d}", data[0]).named["a"]  # type: ignore
    b = parse.parse("Register B: {b:d}", data[1]).named["b"]  # type: ignore
    c = parse.parse("Register C: {c:d}", data[2]).named["c"]  # type: ignore
    program = list(
        map(int, (parse.parse("Program: {pgm}", data[4]).named["pgm"]).split(","))  # type: ignore
    )
    return ThreeBitMachine(a, b, c, program)


def part1(m):
    m.run()
    return ",".join(map(str, m.outputs))


def part2(program):
    """
    Found solution by toying around with the A register and seeing a pattern emerge,
    progressively matching more of the program in its output.
    Changed search range, analyzing which values matched.
    Knew this had to be in the order of 8**15 - 8**16 due to the number of digits in
    the output being (1 + log n / log 8).
    """
    a = 247836855408826
    while a < 8**16:
        a += 2**30  # --> A=247839002892474
        tbm = ThreeBitMachine(a, 0, 0, program)
        tbm.run()
        if tbm.outputs[:17] == program[:17]:
            print(
                f"Trying A={a} - outputs: {tbm.outputs} - operations: {tbm.operations}"
            )
            return a


if __name__ == "__main__":
    m = read_data("day17.txt")
    pgm = m.program.copy()
    print(f"Part 1: {part1(m)}")
    print(f"Part 2: {part2(pgm)}")
