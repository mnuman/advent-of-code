"""
--- Part Two ---

To completely determine whether you have enough adapters, you'll need to
figure out how many
different ways they can be arranged. Every arrangement needs to connect the
charging outlet to
your device. The previous rules about when adapters can successfully connect
still apply.

The first example above (the one that starts with 16, 10, 15) supports the
following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

(The charging outlet and your device's built-in adapter are shown in
parentheses.) Given the
adapters from the first example, the total number of arrangements that
connect the charging
outlet to your device is 8.

The second example above (the one that starts with 28, 33, 18) has many
arrangements. Here are a
few:

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)

In total, this set of adapters can connect the charging outlet to your device
in 19208 distinct
arrangements.

You glance back down at your bag and try to remember why you brought so many
adapters; there must
be more than a trillion valid ways to arrange them! Surely, there must be an
efficient way to
count the arrangements.

What is the total number of distinct ways you can arrange the adapters to
connect the charging
outlet to your device?
"""

import utils


def build_next_dict(source_adapters):
    """Determine the list of next-elements (values) for given adapter (key)"""
    result = {}
    for adapter in [0, *source_adapters]:
        next_adapters = [next_adapter for next_adapter in source_adapters
                         if 1 <= next_adapter - adapter <= 3]
        result[adapter] = sorted(next_adapters)
    return result


def build_tree(leaf_values_dict, next_value_dict):
    """ Key of the leaf_values_dictionary is the current node value,
    the value in the dictionary is the current number of paths to this node.
    """
    new_leave_values = {}
    for cv in leaf_values_dict.keys():
        for nv in next_value_dict[cv]:
            if nv in new_leave_values:
                new_leave_values[nv] += leaf_values_dict[cv]
            else:
                new_leave_values[nv] = leaf_values_dict[cv]
    return new_leave_values


def counts_paths(source_adapters):
    next_values = build_next_dict(source_adapters)
    max_value = max(source_adapters)
    leaf_values = {0: 1}
    i = 0
    while not (max_value in leaf_values and len(leaf_values.keys()) == 1):
        new_leaf_values = build_tree(leaf_values, next_values)
        # add already finished paths to the new nodes
        if max_value in leaf_values:
            if max_value in new_leaf_values:
                new_leaf_values[max_value] += leaf_values[max_value]
            else:
                new_leaf_values[max_value] = leaf_values[max_value]
        leaf_values = new_leaf_values
        print(f"Current iteration {i}")
        i += 1
    return leaf_values[max_value]


if __name__ == "__main__":
    adapters = utils.read_file("data/day10.txt", convert=int)
    print(counts_paths(adapters))
