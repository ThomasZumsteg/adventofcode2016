#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(lines):
    func_pointer = 0
    registers = {r: 0 for r in "abcd"}
    while 0 <= func_pointer < len(commands):
        registers, func_pointer = commands[func_pointer][1](registers, func_pointer)

def part2(lines):
    pass

class Command(object):
    @staticmethod
    def command(func):
        pass

class Assembunny(object):
    def __init__(self, program, f_pointer=0, **kwargs):
        self.f_pointer = f_pointer
        self.program = program

    @staticmethod
    def parse(text):
        for line in text.splitlines():
            for 
            print(line)

    @Command.command(r'cpy (\S+) (\S+)')
    def cpy(x, y):
        y.set(x.get())

    @Command.command(r'dec (\S+)')
    def dec(x):
        x.set(x.get() - 1)

    @Command.command(r'inc (\S+)')
    def inc(x):
        x.set(x.get() + 1)

    @Command.command(r'jnz (\S+) (\S+)')
    def jnz(x, y):
        return y.get() if x.get() != 0 else 1

if __name__ == '__main__':
    assembunny = Assembunny.parse(get_input(day=23, year=2016))
    print("Part 1: {}".format(part1(assembunny)))
    print("Part 2: {}".format(part2(assembunny)))
