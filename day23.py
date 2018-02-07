#!/usr/bin/env python3

from get_input import get_input, line_parser
import re
import inspect
from functools import wraps

def part1(program):
    while 0 <= program.f_pointer < len(program):
        print(program)
        program.step()
    return program.a

TEST_LINES = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

def test_part1():
    program = Assembunny.parse(TEST_LINES)
    assert 3 == part1(program)

def part2(lines):
    pass

class Register(object):
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def get(self):
        try:
            return int(self.value)
        except ValueError:
            return getattr(self.state, self.value)

    def set(self, value):
        return setattr(self.state, self.value, value)

    def __getitem__(self, key):
        return getattr(self.state, self.value)[key]

class Command(object):
    def __repr__(self):
        return "{}{}".format(self.func.__name__, self.args)

    def __init__(self, func, regex, args):
        # print("__init__({}, {}, {})".format(func, regex, args))
        self.func = func
        self.regex = regex
        self.args = args

    def __call__(self, state):
        i = 0
        args = []
        for a in inspect.signature(self.func).parameters.keys():
            if i < len(self.args):
                a = self.args[i]
                i += 1
            args.append(Register(state, a))
        return self.func(*args)

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

    def __repr__(self):
        regestry = {k: v for k, v in self.__dict__.items() if type(v) is int and k != 'f_pointer'}
        return '< {} {} - {}>'.format(self.f_pointer, self.program[self.f_pointer], regestry)

    def __init__(self, program, registers, f_pointer=0):
        self.f_pointer = f_pointer
        self.program = program
        for r, v in registers.items():
            assert not hasattr(self, r)
            setattr(self, r, 0)

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
                    program.append(func(*m.groups()))
                    break
        registers = {}
        for step in program:
            for r in step.args:
                try:
                    int(r)
                except ValueError:
                    registers[r] = 0
        return Assembunny(program, registers)

    @Command.command(r'cpy (\S+) (\S+)', commands)
    def cpy(x, y):
        y.set(x.get())

    @Command.command(r'dec (\S+)', commands)
    def dec(x):
        x.set(x.get() - 1)

    @Command.command(r'inc (\S+)', commands)
    def inc(x):
        x.set(x.get() + 1)

    @Command.command(r'jnz (\S+) (\S+)', commands)
    def jnz(x, y, f_pointer):
        if x.get() != 0:
            f_pointer.set(y.get() - 1 + f_pointer.get())

    @Command.command(r'tgl (\S+)', commands)
    def tgl(a, program, f_pointer):
        mapping = {
            Assembunny.inc: Assembunny.dec,
            Assembunny.dec: Assembunny.inc,
            Assembunny.tgl: Assembunny.inc,
            Assembunny.jnz: Assembunny.cpy,
            Assembunny.cpy: Assembunny.jnz,
            }
        print(mapping)
        p = f_pointer.get() + a.get()
        instruction = program[p]
        program[p] = mapping[instruction.func](instruction.args)

if __name__ == '__main__':
    assembunny = Assembunny.parse(get_input(day=23, year=2016))
    print("Part 1: {}".format(part1(assembunny)))
    print("Part 2: {}".format(part2(assembunny)))
