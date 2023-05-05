import utils
import collections

Policy = collections.namedtuple('Policy', 'min_occur max_occur character')

"""Parse the give policy file:
min-max char: password
"""


def parse_policy(policy):
    parts = policy.split()
    min_occur, max_occur = parts[0].split('-')
    character = parts[1][0]
    pwd = parts[2]
    return Policy(int(min_occur), int(max_occur), character), pwd


def verify_password(password, policy):
    i = 0
    for c in password:
        if c == policy.character:
            i += 1
    return policy.min_occur <= i <= policy.max_occur


def find_matches(policy_file):
    matches = 0
    policy_list = utils.read_file(policy_file)
    for p in policy_list:
        pol, password = parse_policy(p)
        if verify_password(password, pol):
            matches += 1
    return matches


if __name__ == "__main__":
    print(find_matches('data/day02a.txt'))