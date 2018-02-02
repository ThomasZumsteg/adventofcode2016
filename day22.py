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

def part2(nodes):
    seen = set()
    queue = [(0, build(nodes))]
    while True:
        step, state = queue.pop(0)
        if state in seen:
            continue
        seen.add(state)
        print(step)
        for move in moves(state):
            if complete(move):
                return step + 1
            queue.append((step + 1, move))

def build(nodes):
    max_x = max(n.x for n in nodes)
    max_y = max(n.y for n in nodes)
    state = [[None for _ in range(max_x+1)] for _ in range(max_y+1)]
    for node in nodes:
        state[node.y][node.x] = node
    return tuple(tuple(i for i in row) for row in state)

def moves(state):
    zeros = []
    for row in state:
        for item in row:
            if item.used == 0:
                zeros.append(item)
    assert len(zeros) == 1
    zx, zy = zeros[0].x, zeros[0].y
    for m, n in [(zx+1, zy), (zx-1, zy), (zx, zy+1), (zx, zy-1)]:
        if 0 <= n < len(state) and 0 <= m < len(state[n]) and \
                state[zy][zx].size >= state[n][m].used:
            clone = deepcopy(state)
            zero, move = clone[zy][zx], clone[n][m]
            zero.used, move.used = move.used, 0
            yield clone

def complete(state):
    s = state[0][0]
    return s.x == len(state[0]) and s.y == 0 

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

