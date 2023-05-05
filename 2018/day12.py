"""
--- Day 12: Subterranean Sustainability ---
The year 518 is significantly more underground than your history books implied. Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of small pots as far as you can see to your left and right. A few of them contain plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are numbered -1, -2, -3, and so on; to the right, 1, 2, 3.... Your puzzle input contains a list of pots from 0 to the right and whether they do (#) or do not (.) currently contain a plant, the initial state. (No other pots currently contain plants.) For example, an initial state of #..##.... indicates that pots 0, 3, and 4 currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone has been trying to figure out how these plants spread to nearby pots. Based on the notes, for each generation of plants, a given pot has or does not have a plant based on whether that pot (and the two pots on either side of it) had a plant in the last generation. These are written as LLCRR => N, where L are pots to the left, C is the current pot being considered, R are the pots to the right, and N is whether the current pot will have a plant in the next generation. For example:

A note like ..#.. => . means that a pot that contains a plant but with no plants within two pots of it will not have a plant in it during the next generation.
# .## => . means that an empty pot with two plants on each side of it will remain empty in the next generation.
A note like
A note like .##.# => # means that a pot has a plant in a given generation if, in the previous generation, there were plants in that pot, the one immediately to the left, and the one two pots to the right, but not in the ones immediately to the right and two to the left.
It's not clear what these plants are for, but you're sure it's important, so you'd like to make sure the current configuration of plants is sustainable by determining what will happen after 20 generations.

For example, given the following input:

initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
For brevity, in this example, only the combinations which do produce a plant are listed. (Your input includes all possible combinations.) Then, the next 20 generations will look like this:

                 1         2         3
       0         0         0         0
 0: ...#..#.#..##......###...###...........
 1: ...#...#....#.....#..#..#..#...........
 2: ...##..##...##....#..#..#..##..........
 3: ..#.#...#..#.#....#..#..#...#..........
 4: ...#.#..#...#.#...#..#..##..##.........
 5: ....#...##...#.#..#..#...#...#.........
 6: ....##.#.#....#...#..##..##..##........
 7: ...#..###.#...##..#...#...#...#........
 8: ...#....##.#.#.#..##..##..##..##.......
 9: ...##..#..#####....#...#...#...#.......
10: ..#.#..#...#.##....##..##..##..##......
11: ...#...##...#.#...#.#...#...#...#......
12: ...##.#.#....#.#...#.#..##..##..##.....
13: ..#..###.#....#.#...#....#...#...#.....
14: ..#....##.#....#.#..##...##..##..##....
15: ..##..#..#.#....#....#..#.#...#...#....
16: .#.#..#...#.#...##...#...#.#..##..##...
17: ..#...##...#.#.#.#...##...#....#...#...
18: ..##.#.#....#####.#.#.#...##...##..##..
19: .#..###.#..#.#.#######.#.#.#..#.#...#..
20: .#....##....#####...#######....#.#..##.
The generation is shown along the left, where 0 is the initial state. The pot numbers are shown along the top, where 0 labels the center pot, negative-numbered pots extend to the left, and positive pots extend toward the right. Remember, the initial state begins at pot 0, which is not the leftmost pot used in this example.

# .., the one in pot 4 matched the rule looking for .#.#., pot 9 matched .##.., and so on.
After one generation, only seven plants remain. The one in pot 0 matched the rule looking for ..

# contain plants, the furthest left of which is pot -2, and the furthest right of which is pot 34. 
# Adding up all the numbers of plant-containing pots after the 20th generation produces 325.
In this example, after 20 generations, the pots shown as

After 20 generations, what is the sum of the numbers of all pots which contain a plant?
"""
import re
initial_state_matcher = re.compile(r'^initial state: ([#\.]+)$')
next_gen_matcher = re.compile(r'^([#\.]{5}) => ([#\.])$')
empty_left_pots = re.compile(r'^(\.+)')


def readfile(filename):
    """ Read the file and parse its contents. The first line should contain the initial state
    , subsequent lines contain the generators patterns for the next generation
    """
    generations = {}
    with open(filename, 'r') as f:
        l = f.readlines()
    init = initial_state_matcher.match(l[0].strip())
    if init is not None:
        state = init.groups()[0]
    for line in l:
        m = next_gen_matcher.match(line.strip())
        if m is not None:
            # print(m.groups())
            generations[m.groups()[0]] = m.groups()[1]
    return (state, generations)


def cycle(initial_state, rules, cycles):
    """Perform generation of new cycles, give an initial state.
       For generation, need to prefix and postfix the state with some
       blanks.
       """
    all_states = [initial_state]
    c = 0
    state = initial_state  # start with initial state
    leftpot = 0
    while cycles > 0:
        c += 1
        # augment state with some empty pots on either side
        state = '.......' + state + '.......'
        leftpot -= 7
        new_state = []
        cycles -= 1
        # determine every next state
        for i in range(2, len(state)-2):
            pattern = state[i - 2:i + 3]
            new_state.append(rules.get(pattern, '.'))

        # omit all empty pots on either side since they do not add any value
        state = ''.join(new_state)
        # determine the empty pots where gonna shave off from the left ...
        m = empty_left_pots.match(state)
        if m is not None:
            # print(m.groups()[0])
            # since we're not considering the first two positions!
            leftpot += len(m.groups()[0]) + 2
        state = state.lstrip('.').rstrip('.')
        if state not in all_states:
            all_states.append(state)
        else:
            print(
                f'Encountered initial state at cycles: {cycles} with # states: {len(all_states)} and leftpot: {leftpot}, c = {c}')
            print(all_states.index(state))
            print(leftpot), print(state), print(len(state))
    # print(leftpot)
    return (state, leftpot)


def calc_pot_score(state, leftpot=0):
    """ Determine the score, but take into account the offset of the leftpot"""
    return sum([i + leftpot for i in range(len(state)) if state[i] == '#'])


def day12():
    (s, g) = readfile('data/day12-input.txt')
    new_state, leftpot = cycle(initial_state=s, rules=g, cycles=20)
    print(calc_pot_score(new_state, leftpot))


def day12_2():
    (s, g) = readfile('data/day12-input.txt')
    new_state, leftpot = cycle(initial_state=s, rules=g, cycles=1000)
    print(calc_pot_score(new_state, leftpot))


# day12()
# 4200
""" --- Part Two ---
You realize that 20 generations aren't enough. After all, these plants 
will need to last another 1500 years to even reach your timeline, not 
to mention your future.

After fifty billion (50000000000) generations, what is the sum of the 
numbers of all pots which contain a plant?
"""
# day12_2()
# generation will reach a steady state after generating 185 states (so there are 186 distinct states)
# the state is all '#' (length = 194).
# after 1000 cycles of generation: leftpot = 900.
# hence after 50,000,000,000 cycles, leftpot = 49,999,999,900 and state is still '#'*194
print(calc_pot_score('#'*194, 49999999900))
# 9699999999321
