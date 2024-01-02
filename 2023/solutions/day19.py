"""
--- Day 19: Aplenty ---

The Elves of Gear Island are thankful for your help and send you on your way. They
even have a hang glider that someone stole from Desert Island; since you're already
going that direction, it would help them a lot if you would use it to get down
there and return it to them.

As you reach the bottom of the relentless avalanche of machine parts, you
discover that they're already forming a formidable heap. Don't worry, though - a
group of Elves is already here organizing the parts, and they have a system.

To start, each part is rated in each of four categories:

    x: Extremely cool looking
    m: Musical (it makes a noise when you hit it)
    a: Aerodynamic
    s: Shiny

Then, each part is sent through a series of workflows that will ultimately
accept or reject the part. Each workflow has a name and contains a list of
rules; each rule specifies a condition and where to send the part if the
condition is true. The first rule that matches the part being considered is
applied immediately, and the part moves on to the destination described by
the rule. (The last rule in each workflow has no condition and always
applies if reached.)

Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}. This workflow is
named ex and contains four rules. If workflow ex were considering a
specific part, it would perform the following steps in order:

    Rule "x>10:one": If the part's x is more than 10, send the part to
    the workflow named one.
    Rule "m<20:two": Otherwise, if the part's m is less than 20, send the
    part to the workflow named two.
    Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is
    immediately rejected (R).
    Rule "A": Otherwise, because no other rules matched the part, the
    part is immediately accepted (A).

If a part is sent to another workflow, it immediately switches to the start
of that workflow instead and never returns. If a part is accepted (sent to A)
or rejected (sent to R), the part immediately stops any further processing.

The system works, but it's not keeping up with the torrent of weird metal shapes.
The Elves ask if you can help sort a few parts and give you the list of workflows
and some part ratings (your puzzle input). For example:

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}

The workflows are listed first, followed by a blank line, then the ratings of
the parts the Elves would like you to sort. All parts begin in the workflow
named in. In this example, the five listed parts go through the following
 workflows:

    {x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
    {x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
    {x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
    {x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
    {x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

Ultimately, three parts are accepted. Adding up the x, m, a, and s rating
for each of the accepted parts gives 7540 for the part with x=787, 4623
for the part with x=2036, and 6951 for the part with x=2127. Adding all
of the ratings for all of the accepted parts gives the sum total of 19114.

Sort through all of the parts you've been given; what do you get if you
add together all of the rating numbers for all of the parts that
ultimately get accepted?

--- Part Two ---

Even with your help, the sorting process still isn't fast enough.

One of the Elves comes up with a new plan: rather than sort parts individually
through all of these workflows, maybe you can figure out in advance which
combinations of ratings will be accepted or rejected.

Each of the four ratings (x, m, a, s) can have an integer value ranging
from a minimum of 1 to a maximum of 4000. Of all possible distinct combinations
of ratings, your job is to figure out which ones will be accepted.

In the above example, there are 167409079868000 distinct combinations of ratings
that will be accepted.

Consider only your list of workflows; the list of part ratings that the
Elves wanted you to sort is no longer relevant. How many distinct combinations
of ratings will be accepted by the Elves' workflows?

"""
from typing import Optional, TypeAlias
from copy import deepcopy
import file_utils as u
import re


Range: TypeAlias = Optional[tuple[int, int]]


def calc_ranges(r: Range, cond: str) -> tuple[Range, Range]:  # type: ignore
    print(f"Range: {r}, condition: {cond}")
    if r is None:
        return None, None
    elif cond == "True":
        return r, None
    else:
        lo, hi = r
        operator, val = cond[1], int(cond[2:])
        match operator:
            case ">":
                if lo <= val <= hi:
                    passed = (val + 1, hi) if val + 1 <= hi else None
                    failed = (lo, val)
                    return passed, failed
            case "<":
                if lo <= val <= hi:
                    passed = (lo, val - 1) if lo <= val - 1 else None
                    failed = (val, hi)
                    return passed, failed
            case _:
                return None, r
        return None, None


def parse_variables(lines: str):
    patt = re.compile(r"\w=\d+")
    return [
        {m.split("=")[0]: int(m.split("=")[1]) for m in re.findall(patt, line)}
        for line in lines.split("\n")
    ]


def parse_workflow(lines: str):
    result = {}
    for line in lines.split("\n"):
        name, conditions = line.split("{")
        c = []
        for condition in conditions[:-1].split(","):
            if ":" in condition:
                cond, outcome = condition.split(":")
                c.append((cond, outcome))
            else:
                c.append(("True", condition))
        result[name] = c
    return result


def evaluate(conditions, vars):
    """Conditions are strings with expressions like "x<1000",
    while vars are dictionaries containing the variable names as keys
    and values ... well, as values.
    """
    for condition, result in conditions:
        # check if all vars are bound for evaluation - if not skip
        if condition[:1] in vars or condition == "True":
            if eval(condition, None, vars):
                return result


def process_flows(start, workflows, vars) -> bool:
    """Determine if part is accepted or rejected by
    successively applying the workflows.
    """
    wf = start
    i = 0
    while i < 10000:
        result = evaluate(workflows[wf], vars)
        if result == "R":
            return False
        elif result == "A":
            return True
        else:
            wf = result
        i += 1
    return False


def part1(fname: str) -> int:
    flows, conditions = u.read_raw_file(fname).split("\n\n")
    vars = parse_variables(conditions)
    wfs = parse_workflow(flows)
    accepted = [var for var in vars if process_flows("in", wfs, var)]
    return sum(val for vars in accepted for val in vars.values())


def test_no_cycles(next_flow, path, flows, depth=0) -> bool:
    if depth > 500:
        print(f"Reached max cycles, bailing out: f{next_flow}, {path}")
        return False
    if next_flow in "AR":
        return True
    else:
        if next_flow in path:
            return True
        return all(
            test_no_cycles(p, path + "," + p, flows, depth + 1)
            for c, p in flows[next_flow]
        )


def wf_range(wf, ranges, flows, matching_ranges):
    if ranges is None or wf == "R":
        return
    elif wf == "A":
        matching_ranges.append(ranges)
        return
    else:
        wf_ranges = deepcopy(ranges)
        for condition, next_wf in flows[wf]:      # process all children
            if condition == "True":               # accept all
                wf_range(next_wf, deepcopy(wf_ranges), flows, matching_ranges)
            else:
                var_name = condition[0]           # extract var
                passed, nonpassed = calc_ranges(  # determine range split
                    wf_ranges[var_name], condition
                )
                if passed is not None:            # to downstream with successful range
                    new_ranges = deepcopy(wf_ranges)    # new copy!
                    new_ranges[var_name] = passed       # modify range
                    wf_range(next_wf, new_ranges, flows, matching_ranges)
                wf_ranges[var_name] = nonpassed   # always continue with non-passed


def part2(fname: str) -> int:
    """This is a flow network with non-overlapping conditions."""
    flows = parse_workflow(u.read_raw_file(fname).split("\n\n")[0])
    range_dict = {k: (1, 4000) for k in "xmas"}
    matching_ranges = []
    wf_range("in", range_dict, flows, matching_ranges)
    s = 0
    for r in matching_ranges:
        p = 1
        for v in r.values():
            p *= v[1] - v[0] + 1
        s += p
    return s


if __name__ == "__main__":
    print(f"Results part1: {part1('day19.txt')}")
    print(f"Results part2: {part2('day19.txt')}")
