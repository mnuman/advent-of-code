# test_aoc_template.py
import pathlib
import pytest
import aoc202118 as aoc

def test_simple_node():
    """Test that input is parsed properly."""
    root_node = aoc.parse_tree("[7,8]")
    assert root_node.is_root(), "Is root node"
    assert root_node.height() == 1, "Single node with values has height 1"


def test_parsed_tree():
    """Test that input is parsed properly.
                   n
                 /  \
                /\   4
              / \ 3
             /\  2
           / \ 1
          9  8
    """
    inp = '[[[[[9,8],1],2],3],4]'
    n = aoc.parse_tree(inp)
    assert n.is_root(), "Root node was returned"
    assert isinstance(n.right_child, aoc.ValueNode), "Right child is ValueNode"
    assert n.right_child.value == 4, "Stored value is correct"
    assert str(n) == inp, "Tree matches its representation"
    assert n.find_left_value_node(True) is None, "No left value node for root"

def test_complex_tree():
    """Test that input is parsed properly.
                n
              /  \
             n1   1
            /  \
           6    n2
              / \
             5  n3
               / \
              4  n4
                / \
               3   2
    """
    inp = '[[6,[5,[4,[3,2]]]],1]'
    n = aoc.parse_tree(inp)
    assert n.is_root()
    assert str(n) == inp, "Tree matches its representation"
    assert n.find_left_value_node(True) is None, "No left value node for root"
    n1 = n.left_child
    n2 = n1.right_child
    n3 = n2.right_child
    n4 = n3.right_child
    assert n4.left_child.value == 3
    assert n4.find_left_value_node(True).value == 4, "Finds n3's left child"
    assert n3.find_left_value_node(True).value == 5, "Finds n2's left child"
    assert n2.find_left_value_node(True).value == 6, "Finds n1's left child"
    assert n1.find_left_value_node(True) is None, "No left value child"

def test_find_explode():
    inp = '[[[[[9,8],1],2],3],4]'
    n = aoc.parse_tree(inp)
    node_to_explode = aoc.node_to_explode(n)
    assert node_to_explode is not None, "Node for explosion should be found"
    assert node_to_explode.is_leaf(), "Node to explode must be a leaf node"
    assert str(node_to_explode) == '[9,8]', "Correct node to explode"

def test_action_explode():
    inp = '[[[[[9,8],1],2],3],4]'
    n = aoc.parse_tree(inp)
    assert aoc.action_on_node(n), "Action explode executed"
    assert str(n) == '[[[[0,9],2],3],4]', "Correct tree after explosion"

# this one went astray - mixed up root_node and is_root in the implementation!
def test_explode():
    n = aoc.parse_tree('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')
    aoc.action_on_node(n)
    assert str(n) == '[[[[0,7],4],[15,[0,13]]],[1,1]]'

# failing from test reduce
def test_explode_missing():
    n = aoc.parse_tree('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')
    aoc.action_on_node(n)
    assert str(n) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

def test_find_split():
    inp = '[[[[10,9],2],3],4]'
    n = aoc.parse_tree(inp)
    node_to_split = aoc.node_to_split(n)
    assert node_to_split is not None, "Node to split should be found"
    assert node_to_split.value == 10, "Correct node to split value is returned"
    assert str(node_to_split.parent) == '[10,9]', "Correct node found"

def test_action_split():
    inp = '[[[[17,9],2],3],4]'
    n = aoc.parse_tree(inp)
    assert aoc.action_on_node(n), "Action executed"
    assert str(n) == '[[[[[8,9],9],2],3],4]', "Correct tree after split"

def test_split_missing():
    inp = '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
    n = aoc.parse_tree(inp)
    assert aoc.action_on_node(n), "Action executed"
    assert str(n) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', "Correct tree after split"

def test_add():
    left = aoc.parse_tree('[[[[4,3],4],4],[7,[[8,4],9]]]')
    right = aoc.parse_tree('[1,1]')
    added = left.add(right)
    assert str(added) == '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', "Correct addition"

def test_reduce():
    left = aoc.parse_tree('[[[[4,3],4],4],[7,[[8,4],9]]]')
    right = aoc.parse_tree('[1,1]')
    added = left.add(right)
    print(f"\nInitial: {added}")
    aoc.reduce(added)
    assert str(added) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', "Processing of addition result"

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1)


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2)
