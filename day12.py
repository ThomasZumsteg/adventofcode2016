#!/usr/bin/env python3

from get_input import get_input, line_parser
import re

def part1(commands):
    func_pointer = 0
    registers = {register: 0 for register in "abcd"}
    while 0 <= func_pointer < len(commands):
        registers, func_pointer = commands[func_pointer][1](registers, func_pointer)
    return registers['a']

def part2(commands):
    func_pointer = 0
    registers = {register: 0 for register in "abcd"}
    registers['c'] = 1
    while 0 <= func_pointer < len(commands):
        # print('{:2}: {:12}: {}'.format(func_pointer, commands[func_pointer][0], registers))
        registers, func_pointer = commands[func_pointer][1](registers, func_pointer)
    return registers['a']

def parse(line):
    pass

class RegWrapper(object):
    def __repr__(self):
        return self._val

    def __init__(self, val):
        self._val = val

    def populate(self, regestry):
        return Reg(self._val, regestry)

class Reg(object):
    def __repr__(self):
        try:
            return '{}: {}'.format(self._value, self._regestry[self._value])
        except KeyError:
            return self._value

    def __init__(self, value, regestry):
        self._regestry = regestry
        try:
            self._value = int(value)
        except ValueError:
            self._value = value

    def set(self, val):
        try:
            self._regestry[self._value] = val
        except KeyError as e:
            raise ValueError("{} not in the regestry".format(self._value)) from e

    def get(self):
        try:
            return self._regestry[self._value]
        except KeyError:
            return self._value

def command(func):
    def wrapper(*registers):
        registers = tuple(RegWrapper(r) for r in registers)
        def system_call(regestry, pointer):
            args = (r.populate(regestry) for r in registers)
            ret_val = func(*args)
            pointer += ret_val or 1
            return (regestry, pointer)
        return system_call
    return wrapper

@command
def cpy(x, y):
    y.set(x.get())

@command
def inc(x):
    x.set(x.get() + 1)

@command
def dec(x):
    x.set(x.get() - 1)

@command
def jnz(x, y):
    return y.get() if x.get() != 0 else 1

def parse(line):
    assembunny = {
        re.compile(r'cpy (\S+) (\S+)'): cpy,
        re.compile(r'inc (\S+)'): inc,
        re.compile(r'dec (\S+)'): dec,
        re.compile(r'jnz (\S+) (\S+)'): jnz
        }
    for code, func in assembunny.items():
        m = code.match(line)
        if m:
            return (line, func(*m.groups()))
    raise ValueError("Not a valid line {}".format(line))

if __name__ == '__main__':
    commands = line_parser(get_input(day=12, year=2016), parse=parse)
    print('Part 1: {}'.format(part1(commands)))
    print('Part 2: {}'.format(part2(commands)))

