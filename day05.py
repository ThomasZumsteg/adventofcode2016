#!/usr/bin/env python3

from get_input import get_input, line_parser
from itertools import count
import curses
from hashlib import md5

def part1(code):
    password = ''
    for index in count():
        digest = md5('{}{}'.format(code, index).encode('ascii')).hexdigest()
        if digest[:5] == '00000':
            password += digest[5]
            if len(password) >= 8:
                return password

def part2(code):
    password = ' ' * 8
    for index in count():
        digest = md5('{}{}'.format(code, index).encode('ascii')).hexdigest()
        if digest[:5] == '00000':
            location, digit = digest[5:7]
            if '0' <= location < '8' and password[int(location)] is ' ':
                password[int(location)] = digit
                if all(p is not ' ' for p in password):
                    return ''.join(password)

def parse(line):
    return line 

if __name__ == '__main__':
    code = get_input(day=5, year=2016).strip()
    print("Part 1: {}".format(part1(code)))
    print("Part 2: {}".format(part2(code)))
