#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import defaultdict

def part1(directions):
    position = (0, 0)
    heading = (0, 1)
    turn = {
        'R': lambda m: (-m[1], m[0]),
        'L': lambda m: (m[1], -m[0]),
        }
    for t, d in directions:
        heading = turn[t](heading)
        position = tuple(p + h * d for p, h in zip(position, heading))
    return sum(abs(p) for p in position)

def part2(directions):
    position = (0, 0)
    heading = (0, 1)
    visited = set()
    turn = {
        'R': lambda m: (-m[1], m[0]),
        'L': lambda m: (m[1], -m[0]),
        }
    for t, d in directions:
        heading = turn[t](heading)
        for _ in range(d):
            if position in visited:
                break
            visited.add(position)
            position = tuple(p + h for p, h in zip(position, heading))
    return sum(abs(p) for p in position)

def parse(line):
    turn = line[0]
    steps = int(line[1:])
    return (turn, steps)

if __name__ == '__main__':
    directions = line_parser(get_input(day=1, year=2016), parse=parse, seperator=", ")
    print("Part 1: {}".format(part1(directions)))
    print("Part 2: {}".format(part2(directions)))
