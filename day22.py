#!/usr/bin/env python3

from get_input import get_input, line_parser
from copy import deepcopy
from itertools import product
from collections import namedtuple
import re

Node = namedtuple('Node', 'x y size used avail p_used'.split())
Point = namedtuple('Point', ['x', 'y'])

def part1(nodes):
    pairs = set()
    for a, b in product(nodes, nodes):
        if a == b or a.used == 0 or a.used > b.avail:
            continue
        pairs.add((a, b))
    return len(pairs)

def part2(nodes, upper=100):
    (max_x, max_y), zero, full_nodes = build(nodes, upper)
    queue = [(0, zero, (max_x, 0))]
    seen = set()
    while queue:
        steps, zero, goal = queue.pop(0)
        if goal == Point(0, 0):
            return steps
        if (zero, goal) in seen:
            continue
        seen.add((zero, goal))
        for p in [Point(zero.x+dx, zero.y+dy) for dx, dy in \
                [(0,1),(0,-1),(1,0),(-1,0)]]:
            if p in full_nodes or \
                not (0 <= p.x <= max_x) or not (0 <= p.y <= max_y):
                continue
            if p == goal:
                queue.append((steps+1, p, zero))
            else:
                queue.append((steps+1, p, goal))

TEST_TEXT = """Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%"""

def test_part2():
    nodes = line_parser(TEST_TEXT, parse=parse, numbered=True)
    assert part2(nodes, upper=25) == 7

def build(nodes, full_limit):
    max_x, max_y = 0, 0
    full_nodes = set()
    for n in nodes:
        max_x, max_y = max(max_x, n.x), max(max_y, n.y)
        if n.used == 0:
            zero = Point(n.x, n.y)
        elif n.used > full_limit:
            full_nodes.add(Point(n.x, n.y))
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

