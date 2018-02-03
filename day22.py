#!/usr/bin/env python3

from get_input import get_input, line_parser
from copy import deepcopy
from itertools import product
from collections import namedtuple
import re

class Node(object):
    def __init__(self, x, y, size, used, *args):
        self.inital = (x, y)
        self.x = x
        self.y = y
        self.size = size
        self.used = used

    @property
    def avail(self):
        return self.size - self.used

def part1(nodes):
    pairs = set()
    for a, b in product(nodes, nodes):
        if a == b or a.used == 0 or a.used > b.avail:
            continue
        pairs.add((a, b))
    return len(pairs)

def part2(nodes, upper=100):
    print(build(nodes, upper))
    # queue = [(0, zero, state)]
    # seen = set()
    # while queue:
    #     steps, (zx, zy), state = queue.pop(0)
    #     if state in seen:
    #         continue
    #     for mx, my in [(zx+1, zy), (zx-1, zy), 
    #             (zx, zy+1), (zx, zy-1)]:
    #         if not (0 <= my < len(state)) 

    #     print(row)

def build(nodes, full_limit):
    max_x, max_y = 0, 0
    full_nodes = set()
    for n in nodes:
        max_x, max_y = max(max_x, n.x), max(max_y, n.y)
        if n.used == 0:
            zero = (n.x, n.y)
        elif n.used > full_limit:
            full_nodes.add((n.x, n.y))
    return (max_x, max_y), zero, full_nodes

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

