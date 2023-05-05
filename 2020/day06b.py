"""As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which
everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c,
    they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""
import day06a


def separate_answers(group):
    """ Separate the answers for each group into different elements"""
    separated_answers = []
    for member in group:
        separated_answers.append([answer for answer in member])
    return separated_answers


def intersect_answers(list_of_member_answers):
    """ Not a very idiomatic implementation, brute force iteration"""
    shared_answers = ''
    if len(list_of_member_answers) > 1:
        for answer in list_of_member_answers[0]:
            answer_all_members = True
            for other_member_answers in list_of_member_answers[1:]:
                answer_all_members = answer_all_members and answer in other_member_answers
            if answer_all_members:
                shared_answers += answer
    else:
        shared_answers = ''.join(list_of_member_answers[0])
    return ''.join(shared_answers)


if __name__ == '__main__':
    groups = day06a.group_answers("data/day06.txt")
    separated_answers = separate_answers(groups)
    sum_group_identical_answers = sum([len(intersect_answers(group)) for group in separated_answers])
    print(
        f"Sum of number of questions answered identically for all members in the group: {sum_group_identical_answers}")
