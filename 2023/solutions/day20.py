"""
--- Day 20: Pulse Propagation ---

With your help, the Elves manage to find the right parts and fix all of the machines.
Now, they just need to send the command to boot up the machines and get the sand
flowing again.

The machines are far apart and wired together with long cables. The cables don't
connect to the machines directly, but rather to communication modules attached
to the machines that perform various initialization tasks and also act as
communication relays.

Modules communicate using pulses. Each pulse is either a high pulse or a low
pulse. When a module sends a pulse, it sends that type of pulse to each module
in its list of destination modules.

There are several different types of modules:

Flip-flop modules (prefix %) are either on or off; they are initially off. If a
flip-flop module receives a high pulse, it is ignored and nothing happens.
However, if a flip-flop module receives a low pulse, it flips between on and off.
If it was off, it turns on and sends a high pulse. If it was on, it turns off
and sends a low pulse.

Conjunction modules (prefix &) remember the type of the most recent pulse
received from each of their connected input modules; they initially default to
remembering a low pulse for each input. When a pulse is received, the
conjunction module first updates its memory for that input. Then, if it remembers
high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

There is a single broadcast module (named broadcaster). When it receives a pulse,
it sends the same pulse to all of its destination modules.

Here at Desert Machine Headquarters, there is a module with a single button on it
called, aptly, the button module. When you push the button, a single low pulse is
sent directly to the broadcaster module.

After pushing the button, you must wait until all pulses have been delivered and
fully handled before pushing it again. Never push the button if modules are still
processing pulses.

Pulses are always processed in the order they are sent. So, if a pulse is sent to
modules a, b, and c, and then module a processes its pulse and sends more pulses,
the pulses sent to modules b and c would have to be handled first.

The module configuration (your puzzle input) lists each module. The name of the
module is preceded by a symbol identifying its type, if any. The name is then
followed by an arrow and a list of its destination modules. For example:

broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

In this module configuration, the broadcaster has three destination modules
named a, b, and c. Each of these modules is a flip-flop module (as indicated by
the % prefix). a outputs to b which outputs to c which outputs to another module named
inv. inv is a conjunction module (as indicated by the & prefix) which, because it
has only one input, acts like an inverter (it sends the opposite of the pulse
type it receives); it outputs to a.

By pushing the button once, the following pulses are sent:

button -low-> broadcaster
broadcaster -low-> a
broadcaster -low-> b
broadcaster -low-> c
a -high-> b
b -high-> c
c -high-> inv
inv -low-> a
a -low-> b
b -low-> c
c -low-> inv
inv -high-> a

After this sequence, the flip-flop modules all end up off, so pushing the
button again repeats the same sequence.

Here's a more interesting example:

broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output

This module configuration includes the broadcaster, two flip-flops (named a and b),
a single-input conjunction module (inv), a multi-input conjunction module (con),
and an untyped module named output (for testing purposes). The multi-input
conjunction module con watches the two flip-flop modules and, if they're both on,
sends a low pulse to the output module.

Here's what happens if you push the button once:

button -low-> broadcaster
broadcaster -low-> a
a -high-> inv
a -high-> con
inv -low-> b
con -high-> output
b -high-> con
con -low-> output

Both flip-flops turn on and a low pulse is sent to output! However, now that
both flip-flops are on and con remembers a high pulse from each of its two
inputs, pushing the button a second time does something different:

button -low-> broadcaster
broadcaster -low-> a
a -low-> inv
a -low-> con
inv -high-> b
con -high-> output

Flip-flop a turns off! Now, con remembers a low pulse from module a, and so it
sends only a high pulse to output.

Push the button a third time:

button -low-> broadcaster
broadcaster -low-> a
a -high-> inv
a -high-> con
inv -low-> b
con -low-> output
b -low-> con
con -high-> output

This time, flip-flop a turns on, then flip-flop b turns off. However, before
b can turn off, the pulse sent to con is handled first, so it briefly
remembers all high pulses for its inputs and sends a low pulse to output.
After that, flip-flop b turns off, which causes con to update its state
and send a high pulse to output.

Finally, with a on and b off, push the button a fourth time:

button -low-> broadcaster
broadcaster -low-> a
a -low-> inv
a -low-> con
inv -high-> b
con -high-> output

This completes the cycle: a turns off, causing con to remember only low pulses
and restoring all modules to their original states.

To get the cables warmed up, the Elves have pushed the button 1000 times. How
many pulses got sent as a result (including the pulses sent by the button itself)?

In the first example, the same thing happens every time the button is pushed:
8 low pulses and 4 high pulses are sent. So, after pushing the button 1000 times,
 8000 low pulses and 4000 high pulses are sent. Multiplying these together
 gives 32000000.

In the second example, after pushing the button 1000 times, 4250 low pulses and
2750 high pulses are sent. Multiplying these together gives 11687500.

Consult your module configuration; determine the number of low pulses and high
pulses that would be sent after pushing the button 1000 times, waiting for all
pulses to be fully handled after each push of the button. What do you get if
you multiply the total number of low pulses sent by the total number of
high pulses sent?

--- Part Two ---

The final machine responsible for moving the sand down to Island Island has
a module attached named rx. The machine turns on when a single low pulse is
sent to rx.

Reset all modules to their default states. Waiting for all pulses to be
fully handled after each button press, what is the fewest number of button
presses required to deliver a single low pulse to the module named rx?
"""
from dataclasses import dataclass
from functools import reduce
from operator import mul
import file_utils as u
from queue import Queue
from enum import Enum


class Pulse(Enum):
    LO = 0
    HI = 1


@dataclass
class Message:
    sender: str
    recipient: str
    content: Pulse
    idx: int


class Component:
    def __init__(self, name: str, queue: Queue, destinations: list[str]):
        self.name = name
        self.queue = queue
        self.destinations = destinations

    def process(self, message):
        self.send(message.content, message.idx)

    def send(self, outbound_content, idx):
        for d in self.destinations:
            self.queue.put(Message(self.name, d, outbound_content, idx))

    def input(self, rcpt):
        pass


class BroadCaster(Component):
    pass


class FlipFlop(Component):
    def __init__(self, name: str, queue: Queue, destinations: list[str]):
        self.on = False
        super().__init__(name, queue, destinations)

    def process(self, message):
        if message.content == Pulse.LO:
            new_content = Pulse.LO if self.on else Pulse.HI
            self.send(new_content, message.idx)
            self.on = not self.on


class Conjunction(Component):
    def __init__(self, name: str, queue: Queue, destinations: list[str]):
        super().__init__(name, queue, destinations)
        self.state = {}
        self.freq = {}

    def process(self, message):
        self.state[message.sender] = message.content
        component_state = set(self.state[k] for k in self.state.keys())
        if len(component_state) == 1 and component_state.pop() == Pulse.HI:
            self.send(Pulse.LO, message.idx)
        else:
            self.send(Pulse.HI, message.idx)
        if self.name == 'hj' and message.content == Pulse.HI:
            if message.sender not in self.freq:
                self.freq[message.sender] = message.idx
            print(f"{message.sender} - HI - {message.idx}")


    def input(self, rcpt):
        self.state[rcpt] = Pulse.LO


class MessageQueue(Queue):
    def __init__(self, maxsize=0):
        super(MessageQueue, self).__init__(maxsize)
        self.lo_counter: int = 0
        self.hi_counter: int = 0

    def put(self, item, block=True, timeout=None):
        # print(f"{item.sender},{item.recipient},{item.content}")
        if item.content == Pulse.LO:
            self.lo_counter += 1
        else:
            self.hi_counter += 1
        super().put(item, block, timeout)

    def result(self) -> int:
        return self.hi_counter * self.lo_counter


def parse_config(fname: str, q: Queue):
    config = {}
    for line in u.read_file(fname):
        c, d = line.split(" -> ")
        destinations = [dest.strip() for dest in d.split(",")]
        component = c[1:].strip() if c[0] in "%&" else c.strip()
        match c[0]:
            case "b":
                config[component] = BroadCaster(component, q, destinations)
            case "%":
                config[component] = FlipFlop(component, q, destinations)
            case "&":
                config[component] = Conjunction(component, q, destinations)
    # initialize all objects irrespective of type
    for name, obj in config.items():
        for d in obj.destinations:
            if d in config:
                config[d].input(name)
    return config


def process_messages(queue, configuration):
    while queue.qsize() > 0:
        msg = queue.get()
        if msg.sender in ("ks", "jf", "qs", "zk") and msg.content == Pulse.HI:
            print(f"{msg.sender} sent message to {msg.recipient} - {msg.content}")
        if msg.recipient in configuration:
            dest = configuration[msg.recipient]
            dest.process(msg)


def part1(fname: str) -> int:
    q = MessageQueue()
    cfg = parse_config(fname, q)
    for i in range(1000):
        q.put(Message("button", "broadcaster", Pulse.LO, i))
        process_messages(q, cfg)
    return q.result()


def part2(fname: str) -> int:
    q = MessageQueue()
    cfg = parse_config(fname, q)
    for i in range(1,10000):
        q.put(Message("button", "broadcaster", Pulse.LO, i))
        process_messages(q, cfg)
    print(f"Repeat cycles: {cfg['hj'].freq}")
    return reduce(mul, cfg['hj'].freq.values())


if __name__ == "__main__":
    # print(f"Results part1: {part1('day20.txt')}")
    print(f"Results part2: {part2('day20.txt')}")
