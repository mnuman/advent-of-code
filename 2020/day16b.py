"""
Now that you've identified which tickets contain invalid values, discard
those tickets entirely. Use the remaining valid tickets to determine which
field is which.

Using the valid ranges for each field, determine what order the fields appear
on the tickets. The order is consistent between all tickets: if seat is the
third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must be
row, the second position must be class, and the third position must be seat;
you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your
ticket that start with the word departure. What do you get if you multiply
those six values together?
"""
import re

import day16a
import utils


def read_file(filename):
    lines = utils.read_file(filename)
    rules = {}
    tickets = []
    i = 0
    while len(lines[i]) > 0:
        m = re.match(r"^([\w\s]+):\s(\d*)-(\d*)\sor\s(\d*)-(\d*)$", lines[i])
        rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))),
                             (int(m.group(4)), int(m.group(5)))]
        i += 1
    i += 2
    my_ticket = [int(n) for n in lines[i].split(',')]
    i += 3

    while i < len(lines):
        tickets.append([int(n) for n in lines[i].split(',')])
        i += 1

    return rules, my_ticket, tickets


class TicketValidator(day16a.TicketValidator):

    def drop_invalid_tickets(self):
        valid_tickets = []
        for t in self.nearby_tickets:
            for n in t:
                if not self.check_in_any_range(n):
                    break
            else:
                valid_tickets.append(t)
        self.nearby_tickets = valid_tickets

    def match_rules_to_ticket_order(self):
        """Generates all possible assignments of rules to columns, dictionary
        key is the column numner, its value is the list of possible rules
        """
        number_of_columns = len(self.my_ticket)
        rule_column = {}
        for column_number in range(0, number_of_columns):
            for rule_name in self.rules:
                # all col values must satisfy any of the rule criteria
                if all([any([s <= ticket[column_number] <= e for s, e in
                             self.rules[rule_name]]) for ticket in
                        self.nearby_tickets]):
                    if column_number in rule_column:
                        rule_column[column_number].append(rule_name)
                    else:
                        rule_column[column_number] = [rule_name]
        assigned_columns = {}
        while len(assigned_columns) < number_of_columns:
            # maps keys to number of options
            keys = {k: len(rule_column[k]) for k in rule_column}
            # pick keys that are already determined (single options)
            determined_keys = [k for k in keys if keys[k] == 1]
            # assign key-column to assigned set and remove from options for
            # all columns
            for dk in determined_keys:
                assigned_rule = rule_column[dk][0]
                assigned_columns[dk] = assigned_rule
                # remove the assigned option for all columns
                for col_no in rule_column:
                    col_options = rule_column[col_no]
                    if assigned_rule in col_options:
                        rule_column[col_no].remove(assigned_rule)
        return assigned_columns


if __name__ == "__main__":
    tv = TicketValidator("data/day16.txt")
    tv.drop_invalid_tickets()
    combination = tv.match_rules_to_ticket_order()
    prod = 1
    relevant_columns = [c for c in combination if
                        'departure' in combination[c]]
    for col_number in relevant_columns:
        prod *= tv.my_ticket[col_number]
        print(
            f"Found col {col_number}, rule {combination[col_number]}, "
            f"product is now {prod}, factor is {tv.my_ticket[col_number]}")
    print(f"Final answer: {prod}")
