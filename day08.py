#!/usr/bin/env python3

from copy import deepcopy
from get_input import get_input, line_parser
from itertools import product
import re

def part1(funcs, height=6, width=50):
    screen = [['.' for _ in range(width)] for _ in range(height)]
    for func in funcs:
        func(screen)
    return sum(1 if p == '#' else 0 for row in screen for p in row)

def part2(funcs, height=6, width=50):
    screen = [['.' for _ in range(width)] for _ in range(height)]
    for func in funcs:
        func(screen)
    return '\n' + '\n'.join(''.join(row) for row in screen)

def rect(a, b):
    a, b = int(a), int(b)
    def rect_func(screen):
        for c, r in product(range(a), range(b)):
            screen[r][c] = '#'
    return rect_func

def rotate_row(r, dist):
    r, dist = int(r), int(dist)
    def rotate_row_func(screen):
        row = screen[r] 
        screen[r] = row[len(row)-dist:] + row[:len(row)-dist]
    return rotate_row_func

def test_rotate_row():
    screen = list(list(row) for row  in "1234,5678,90ab".split(','))
    rotate_1 = rotate_row(0, 1)
    rotate_1(screen)
    assert "4123,5678,90ab" == ','.join(''.join(row) for row in screen)
    rotate_2 = rotate_row(1, 2)
    rotate_2(screen)
    assert "4123,7856,90ab" == ','.join(''.join(row) for row in screen)

def rotate_col(c, dist):
    c, dist = int(c), int(dist)
    def rotate_col_func(screen):
        column = [screen[r][c] for r in range(len(screen))]
        for r in range(len(screen)):
            screen[(r+dist)%len(screen)][c] = column[r]
    return rotate_col_func

def test_rotate_col():
    screen = list(list(row) for row  in "1234,5678,90ab".split(','))
    rotate_1 = rotate_col(0, 1)
    rotate_1(screen)
    assert "9234,1678,50ab" == ','.join(''.join(row) for row in screen)
    rotate_2 = rotate_col(1, 2)
    rotate_2(screen)
    assert "9634,1078,52ab" == ','.join(''.join(row) for row in screen)
    rotate_3 = rotate_col(2, 3)
    rotate_3(screen)
    assert "9634,1078,52ab" == ','.join(''.join(row) for row in screen)

FUNCS = {
    re.compile(r'rect (\d+)x(\d+)'): rect,
    re.compile(r'rotate row y=(\d+) by (\d+)'): rotate_row,
    re.compile(r'rotate column x=(\d+) by (\d+)'): rotate_col,
}

def parse(line):
    for regex, func in FUNCS.items():
        m = regex.match(line)
        if m is not None:
            return func(*m.groups())
    raise ValueError("Did not parse " + line)
                
if __name__ == '__main__':
    lines = line_parser(get_input(day=8, year=2016), parse=parse)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
