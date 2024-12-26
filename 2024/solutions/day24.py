from collections import Counter
from copy import deepcopy
import file_utils as f


class Circuit:
    values = {}

    def __init__(self, op1, operation, op2):
        self.op1 = op1
        self.operation = operation
        self.op2 = op2

    def operands(self):
        return self.op1, self.op2

    def val(self):
        assert (
            self.op1 in self.values and self.op2 in self.values
        ), "Operands not in values"
        val_1 = self.values[self.op1]
        val_2 = self.values[self.op2]
        if self.operation == "AND":
            return val_1 & val_2
        elif self.operation == "OR":
            return val_1 | val_2
        elif self.operation == "XOR":
            return val_1 ^ val_2
        else:
            return ValueError("Invalid operator provided")


def read_data(fname: str):
    inputs = {}
    combinations = {}
    for line in f.read_file(fname):
        if ":" in line:
            key, value = line.split(":")
            inputs[key] = int(value)
        elif "->" in line:
            tokens = line.split(" ")
            combinations[tokens[-1]] = Circuit(*tokens[:3])  # type: ignore

    return inputs, combinations


def get_bits(values, prefix):
    return "".join(
        str(values[k]) for k in reversed([k for k in values.keys() if k[0] == prefix])
    )


def categorize_circuits(circuits):
    result = Counter()
    for k, c in circuits.items():
        if c.op1[0] not in "xy" and c.op2[0] not in "xy":
            idx = (c.operation, circuits[c.op1].operation, circuits[c.op2].operation)
            result[idx] += 1
    keys = sorted(result.keys(), key=lambda x: result[x], reverse=True)
    for k in keys:
        operation, input1, input2 = k
        print(f"{operation}={input1} {input2}: {result[k]}")


def mismatching_inputs(circuits):
    def is_z_mismatch(key, operation):
        return key[0] == "z" and operation != "XOR"

    def is_xor_mismatch(key, op1, op2):
        return operation == "XOR" and not (
            key[0] in "xyz" or op1[0] in "xyz" or op2[0] in "xyz"
        )

    def is_and_mismatch(key, op1, op2):
        if operation == "AND" and "x00" not in (op1, op2):
            return any(
                (key == subop1 or key == subop2) and subop != "OR"
                for subop1, subop, subop2, _ in sub_circuits
            )
        return False

    def is_xor_sub_mismatch(key):
        if operation == "XOR":
            return any(
                (key == subop1 or key == subop2) and subop == "OR"
                for subop1, subop, subop2, _ in sub_circuits
            )
        return False

    mismatches = set()
    sub_circuits = [(c.op1, c.operation, c.op2, k) for k, c in circuits.items()]

    for key, circuit in circuits.items():
        operation, op1, op2 = circuit.operation, circuit.op1, circuit.op2
        if (
            is_z_mismatch(key, operation)
            or is_xor_mismatch(key, op1, op2)
            or is_and_mismatch(key, op1, op2)
            or is_xor_sub_mismatch(key)
        ):
            mismatches.add(key)

    return ",".join(sorted(e for e in mismatches if e not in ("z00", "z45")))


def part1(data):
    """Brute force iterating over all unassigned circuits until all outputs are assigned"""
    values, circuits = data
    Circuit.values = values
    all_outputs = set(filter(lambda x: x[0] == "z", circuits.keys()))
    while not all(o in values for o in all_outputs):
        circuits_up_for_eval = (
            (k, c)
            for k, c in circuits.items()
            if k not in values and all(op in values for op in c.operands())
        )
        for key, circuit in circuits_up_for_eval:
            values[key] = circuit.val()
    return int(get_bits(values, "z"), 2)


def part2(data):
    # This is a Ripple Carry Adder circuit
    # https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
    # https://www.ece.uvic.ca/~fayez/courses/ceng465/lab_465/project1/adders.pdf
    values, circuits = data
    # categorize_circuits(circuits)
    return mismatching_inputs(circuits)


def read_relations(fname: str):
    relations = []
    for line in f.read_file(fname):
        if "->" in line:
            tokens = line.split(" ")
            relations.append((tokens[0], tokens[1], tokens[2], tokens[4]))
    return relations


def generate_graphviz(relations, output_file="graph.dot"):
    with open(output_file, "w") as f:
        f.write("digraph G {\n")
        for op1, operator, op2, result in relations:
            f.write(f'    "{op1}" -> "{result}" [label="{operator}"];\n')
            f.write(f'    "{op2}" -> "{result}" [label="{operator}"];\n')
        f.write("}\n")


if __name__ == "__main__":
    data = read_data("day24.txt")
    print(f"Part 1: {part1(deepcopy(data))}")
    print(f"Part 2: {part2(deepcopy(data))}")
    # relations = read_relations("day24.txt")
    # generate_graphviz(relations, "graph.dot")
