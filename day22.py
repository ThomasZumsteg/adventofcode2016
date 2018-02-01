#!/usr/bin/env python3

from get_input import get_input, line_parser
from copy import deepcopy
from itertools import product
from collections import namedtuple
import re

Node = namedtuple('Node', 'x y size used avail p_used'.split())

def part1(nodes):
    pairs = set()
    for a, b in product(nodes, nodes):
        if a == b or a.used == 0 or a.used > b.avail:
            continue
        print(a, b)
        pairs.add((a, b))
    return len(pairs)

def part2(nodes):
    pass

def parse(line, i):
    if i < 2:
        return
    regex = r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%'
    args = (int(g) for g in re.match(regex, line).groups())
    return Node(*args)

if __name__ == '__main__':
    nodes = line_parser(get_input(day=22, year=2016), parse=parse, numbered=True)
    print("Part 1: {}".format(part1(nodes)))
    print("Part 2: {}".format(part2(nodes)))


