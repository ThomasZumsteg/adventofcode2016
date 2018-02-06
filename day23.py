#!/usr/bin/env python3

from get_input import get_input, line_parser
import re
from functools import wraps

def part1(program):
    while 0 <= program.f_pointer < len(program):
        program.step()

def part2(lines):
    pass

class Integer(object):
    def __init__(self, value):
        self.value = int(value)

    def get(self):
        return self.value

class Command(object):
    def __init__(self, func, regex, register):
        print("__init__({}, {}, {})".format(func, regex, register))
        self.func = func
        self.regex = regex
        self.register = register 

    def __call__(self, state):
        return self.func(*args, **kwargs)

    @staticmethod
    def command(regex, storage=None):
        def wrapped(func):
            @wraps(func)
            def instruction(*args):
                return Command(func, regex, args)
            if storage is not None:
                storage[regex] = instruction 
            return instruction
        return wrapped

class Assembunny(object):
    commands = {}

    def __init__(self, program, registers, f_pointer=0):
        self.f_pointer = f_pointer
        self.program = program
        self.registers = registers

    def step(self):
        self.program[self.f_pointer](self)
        self.f_pointer += 1

    def __len__(self):
        return len(self.program)

    @staticmethod
    def parse(text):
        program = []
        for line in text.splitlines():
            for regex, func in Assembunny.commands.items():
                m = re.match(regex, line)
                if m is not None:
                    print(func)
                    program.append(func(*m.groups()))
                    break
        registers = {}
        for step in program:
            for r in step.register:
                registers[r] = 0
        return Assembunny(program, registers)

    @Command.command(r'cpy (\S+) (\S+)', commands)
    def cpy(x, y):
        y.set(x.get())

    @Command.command(r'dec (\S+)', commands)
    def dec(x, value=1):
        inc(x, value=-1)

    @Command.command(r'inc (\S+)', commands)
    def inc(x, value=1):
        x.set(x.get() + value)

    @Command.command(r'jnz (\S+) (\S+)', commands)
    def jnz(x, y):
        if x.get() != 0:
            self.f_pointer += y.get() - 1

    @Command.command(r'tgl (\S+)', commands)
    def tgl(a):
        mapping = {
            inc: dec,
            dec: inc,
            tgl: inc,
            jnz: cpy,
            cpy: jnz,
            }
        p = self.f_pointer + a.get()
        instruction = self.program[p]
        self.program[p] = mapping[instruction](instruction.args)

if __name__ == '__main__':
    assembunny = Assembunny.parse(get_input(day=23, year=2016))
    print("Part 1: {}".format(part1(assembunny)))
    print("Part 2: {}".format(part2(assembunny)))
