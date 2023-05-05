import utils
"""
--- Day 4: Repose Record ---
You've sneaked into another supply closet - this time, it's across from
the prototype suit manufacturing lab. You need to sneak inside and fix
the issues with the suit, but there's a guard stationed outside the lab,
so this is as close as you can safely get.

As you search the closet for anything that might help, you discover that
you're not the first person to want to sneak in. Covering the walls,
someone has spent an hour starting every midnight for the past few
months secretly observing this guard post! They've been writing down
the ID of the one guard on duty that night - the Elves seem to have
decided that one guard was enough for the overnight shift - as well
as when they fall asleep or wake up while at their post (your puzzle input).

For example, consider the following records, which have already been
organized into chronological order:

[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
Timestamps are written using year-month-day hour:minute format. The
guard falling asleep or waking up is always the one whose shift most
recently started. Because all asleep/awake times are during the midnight
hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant
for those events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
The columns are Date, which shows the month-day portion of the relevant day;
ID, which shows the guard on duty that day; and Minute, which shows the
minutes during which the guard was asleep within the midnight hour. (The Minute
column's header shows the minute's ten's digit in the first row and the one's
digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they
count as awake on the minute they wake up. For example, because Guard #10
wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific
time, you might be able to trick that guard into working tonight so you
can have the best chance of sneaking in. You have two strategies for
choosing the best guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What
minute does that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total
of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
(10+10+10). Guard #10 was asleep most during minute 24 (on two days,
whereas any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your
entries are in the order you found them. You'll need to organize
them before they can be analyzed.

What is the ID of the guard you chose multiplied by the minute
you chose? (In the above example, the answer would be 10 * 24 = 240.)
"""

""" Part2:
Strategy 2: Of all guards, which guard is most frequently asleep on 
the same minute?

In the example above, Guard #99 spent minute 45 asleep more than 
any other guard or minute - three times in total. (In all other 
cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you 
chose? (In the above example, the answer would be 99 * 45 = 4455.)
"""


def splitfields(line):
    """ Parse the read line into constituent fields/encodings:
        0000000000111111111122222222
        0123456789012345678901234567
        [1518-10-29 00:52] falls asleep
        [1518-06-01 23:53] Guard  #101 begins shift
        [1518-07-31 00:35] wakes up
"""
    datum = line[1:11]
    tijd = line[12:17]
    event = line[19:]
    if event == 'falls asleep':
        action = 'S'
    elif event == 'wakes up':
        action = 'W'
    else:
        # simply extract the guards number.
        action = event[7:].split(' ')[0]
    return (datum, tijd, action)


def prepare_data(fname):
    events = []
    with open(fname, 'r') as datafile:
        data = datafile.readlines()
    for l in data:
        events.append(splitfields(l.strip()))
    return sorted(events)


def sleeper(s, e):
    return ('.' * s + '#' * (e - s) + '.' * (60 - e))[:60]


def parse_data(events):
    """Parse events for wake/sleep per guard"""
    guard = None
    guard_sleep_times = {}
    for e in events:
        if e[2] == 'S':
            start = int(e[1][-2:])
        elif e[2] == 'W':
            end = int(e[1][-2:])
            if guard in guard_sleep_times:
                guard_sleep_times[guard].append(sleeper(start, end))
            else:
                guard_sleep_times[guard] = [sleeper(start, end)]
        else:
            guard = e[2]  # update guard number!
    return guard_sleep_times


def select_most_minutes(data):
    """Return the guard who is asleep on the most minutes"""
    result = []
    for guard in data:
        total_minutes = 0
        for sleep_section in data[guard]:
            total_minutes += sum([1 for c in sleep_section if c == '#'])
        result.append((total_minutes, guard))
    return sorted(result, reverse=True)[0][1]


def select_minute(data, guard):
    minutes = [0] * 60
    for sleep_section in data[guard]:
        for i in range(0, 60):
            if sleep_section[i] == '#':
                minutes[i] += 1
    maxmin, maxval = 0, 0
    for i in range(0, 60):
        if minutes[i] > maxval:
            maxmin = i
            maxval = minutes[i]
    return maxmin, maxval


def sleepiest_minute_same_guard(data):
    sleepiest = {}
    for guard in data:
        sleepiest_minute = [0]*60
        for sleep_section in data[guard]:
            for i in range(0, 60):
                if sleep_section[i] == '#':
                    sleepiest_minute[i] += 1
        sleepiest[guard] = sleepiest_minute
    # oops ... indented this one level too much to give the wrong answer!
    return sleepiest


def find_sleepiest_minute(sleep_dict):
    g = None
    m = 0
    v = 0
    for guard in sleep_dict:
        for minute in range(0, 60):
            if sleep_dict[guard][minute] >= v:
                v = sleep_dict[guard][minute]
                g = guard
                m = minute
    return (g, m, v)


if __name__ == '__main__':
    raw_data = prepare_data('data/day4-input.txt')
    data = parse_data(raw_data)
    sleepiest = sleepiest_minute_same_guard(data)
    # print(sleepiest['3557'])
    # print(data['3557'])
    g, m, v = find_sleepiest_minute(sleepiest)
    # Guard 1901 spent minutes 47 most times asleep: 19 - answer = 89347
    print(
        f'Guard {g} spent minutes {m} most times asleep: {v} - answer = {int(g)*m}')
    # sleepiest_guard = select_most_minutes(data)
    # maxmin, maxval = select_minute(data, sleepiest_guard)
    # print(
    #     f'Sleepiest guard {sleepiest_guard}, slept {maxval} times in minute {maxmin}: result {int(sleepiest_guard) * maxmin}')
    # # Solution: Sleepiest guard 3457, slept 14 times in minute 40: result 138280
