class SnailFishNumber:
    def __init__(self, left, right):
        self.left, self.right = left, right

    def value(self):
        def value_helper(x):
            return x if isinstance(x, int) else x.value()

        return 3 * value_helper(self.left) + 2 * value_helper(self.right)


if __name__ == '__main__':
    part_1 = None
    print("Day 18 - part 1", part_1)
    part_2 = None
    print("Day 18 - part 2", part_2)
