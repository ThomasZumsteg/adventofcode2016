#!/usr/bin/env python3

from get_input import get_input, line_parser
from day23 import Assembunny, Command
from copy import deepcopy
from itertools import count

class Assembunny_v2(Assembunny):
    @Command.command(r'out (\S+)', Assembunny.commands)
    def out(a):
        return a.get()


def part1(program):
    for i in count(1):
        seen = set()
        p = deepcopy(program)
        p.a = i
        seq = []
        while 0 <= p.f_pointer < len(p):
            output = p.step()

            if output is not None:
                if output not in (0, 1) or (seq != [] and output == seq[-1]):
                    print("Testing {}: {}, {}".format(i, seq, output))
                    break
                seq.append(output)
                if p in seen:
                    return i
                seen.add(p)

def part2(program):
    return "Merry Christmas"

if __name__ == '__main__':
    program = Assembunny_v2.parse(get_input(day=25, year=2016))
    print('Part 1: {}'.format(part1(program)))
    print('Part 2: {}'.format(part2(program)))

"""
cpy a d
cpy 4 c
    cpy 643 b
        inc d
        dec b
        jnz b -2
    dec c
    jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
            cpy 2 c
    jnz b 2
        jnz 1 6
    dec b
dec c
jnz c -4
inc a
jnz 1 -7
        cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
                jnz a -19
            jnz 1 -21
"""
