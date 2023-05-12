# aoc_template.py
import pathlib
import sys
from typing import Union, List
from dataclasses import dataclass
import math

@dataclass
class ValueNode:
    value: int
    parent: 'Node' = None

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def height() -> int:
        return 0

@dataclass
class Node:
    parent: Union['Node', None] = None
    left_child: Union['Node', ValueNode] = None
    right_child: Union['Node', ValueNode] = None

    def is_root(self) -> bool:
        return self.parent is None

    def is_leaf(self) -> bool:
        return isinstance(self.left_child, ValueNode) and isinstance(self.right_child, ValueNode)

    def height(self) -> int:
        return 1 + max(self.left_child.height(), self.right_child.height())

    def depth(self) -> int:
        return 1 if self.is_root() else 1 + self.parent.depth()

    def root_node(self) -> 'Node':
        return self if self.is_root() else self.parent.root_node()

    def __str__(self) -> str:
        return f"[{self.left_child},{self.right_child}]"

    def find_left_value_node(self, start=True) -> Union[ValueNode, None]:
        """Find the first left node that is a value node"""
        if self.is_root() and not isinstance(self.left_child, ValueNode):
            return None                                                 # root node's left child is not ValueNode
        if isinstance(self.left_child, ValueNode) and not start:
            return self.left_child                                      # not start node with left child ValueNode
        return self.parent.find_left_value_node(False)                  # recursively up the tree!

    def find_right_value_node(self, start=True) -> Union[ValueNode, None]:
        """Find the first right node that is a value node"""
        if self.is_root() and not isinstance(self.right_child, ValueNode):
            return None                                                 # root node's right child is not ValueNode
        if isinstance(self.right_child, ValueNode) and not start:
            return self.right_child                                     # not start node with right child ValueNode
        return self.parent.find_right_value_node(False)                 # recursively up the tree!

    def add(self, other: 'Node') -> 'Node':
        new_root = Node(left_child=self, right_child=other)
        self.parent, other.parent = new_root, new_root
        return new_root


def get_nodes(s: Node, nodelist=None) -> List[Node]:
    if nodelist is None:
        nodelist = []
    if isinstance(s, Node):
        nodelist.append(s)
        get_nodes(s.left_child, nodelist)
        get_nodes(s.right_child, nodelist)
    return nodelist

def node_to_explode(root: Node) -> Union[Node, None]:
    nodelist = get_nodes(root)
    for node in nodelist:
        if node.depth() > 4:
            print(f"Exploding node {node}")
            return node
    print("No node to explode")
    return None

def node_to_split(root: Node) -> Union[ValueNode, None]:
    for node in get_nodes(root):
        for n in (node.left_child, node.right_child):
            if isinstance(n, ValueNode) and n.value >= 10:
                print(f"Splitting node {n} - parent node {n.parent}")
                return n

def action_on_node(n: Node) -> bool:
    ne = node_to_explode(n)
    if ne is not None:          # explode?
        left_val, right_val = ne.left_child.value, ne.right_child.value
        left_value_node, right_value_node = ne.find_left_value_node(), ne.find_right_value_node()
        if left_value_node is not None:
            left_value_node.value += left_val
        if right_value_node is not None:
            right_value_node.value += right_val
        zero_node = ValueNode(value=0, parent=ne.parent)
        if ne.parent.left_child == ne:          # assign the new zero node to the correct child
            ne.parent.left_child = zero_node
        else:
            ne.parent.right_child = zero_node
        ne.parent = None        # detach the original node
        print(f"Current tree: {n}")
        return True
    else:                       # no node to explode: then split?
        ns = node_to_split(n)
        if ns is not None:
            split_node = Node(parent=ns.parent)
            split_node.left_child = ValueNode(parent=split_node, value=math.floor(ns.value/2))
            split_node.right_child = ValueNode(parent=split_node, value=math.ceil(ns.value/2))
            if ns.parent.left_child == ns:                  # put new node in correct place in tree
                ns.parent.left_child = split_node
            else:
                ns.parent.right_child = split_node
            ns.parent = None                                # detach the old node (this was a ValueNode)
            print(f"Current tree: {n}")
            return True
    return False                # nothing to do!

def reduce(n: Node):
    """no return value required - we still have the node reference"""
    while action_on_node(n):        # loop as long as there is work to do
        pass                        # no action needs to be taken - that is in the while condition already

def __parse_list__(subtree: List[int]) -> Union[Node, ValueNode]:
    left_node = ValueNode(subtree[0]) if isinstance(subtree[0], int) else __parse_list__(subtree[0])
    right_node = ValueNode(subtree[1]) if isinstance(subtree[1], int) else __parse_list__(subtree[1])
    node = Node(left_child=left_node, right_child=right_node)
    left_node.parent, right_node.parent = node, node
    return node


def parse_tree(subtree_as_string: str) -> Node:
    return __parse_list__(subtree=eval(subtree_as_string))


def parse(puzzle_input):
    """Parse input."""
    return None


def part1(data):
    """Solve part 1."""
    return None


def part2(data):
    """Solve part 2."""
    return None


def solve(my_input):
    """Solve the puzzle for the given input."""
    data = parse(my_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
