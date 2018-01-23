#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import namedtuple
from hashlib import md5
from copy import copy

class MazeState(object):
    def __init__(self, prefix, x=0, y=0, path=''):
        self.prefix = prefix
        self.path = path
        self.x = x
        self.y = y

    def __repr__(self):
        return 'MazeState(prefix={}, x={}, y={}, path={})'.format(
                self.prefix, self.x, self.y, self.path)

    @property
    def hex(self):
        return md5((self.prefix + self.path).encode()).hexdigest()

    def directions(self):
        dirs = ( ('U', (0, -1)), ('D', (0, 1)), ('L', (-1, 0)), ('R', (1, 0)) )
        directions = {}
        for c, (d, (dx, dy)) in zip(self.hex, dirs):
            if c in "bcdef":
                yield MazeState(
                        self.prefix, 
                        x = self.x + dx,
                        y = self.y + dy,
                        path = self.path + d)

def part1(prefix):
    queue = [MazeState(prefix)]
    while queue:
        state = queue.pop(0)
        if state.x == 3 and state.y == 3:
            return state.path
        for step in state.directions():
            if 0 <= step.x < 4 and 0 <= step.y < 4:
                queue.append(step)

def test_part1():
    assert 'DDRRRD' == part1('ihgpwlah')
    assert 'DDUDRLRRUDRD' == part1('kglvqrro')
    assert 'DRURDRUDDLLDLUURRDULRLDUUDDDRR' == part1('ulqzkmiv')

def part2(prefix):
    queue = [MazeState(prefix)]
    longest = None
    while queue:
        state = queue.pop(0)
        if state.x == 3 and state.y == 3:
            longest = state
            continue
        for step in state.directions():
            if 0 <= step.x < 4 and 0 <= step.y < 4:
                queue.append(step)
    return len(longest.path)

if __name__ == '__main__':
    prefix = get_input(day=17, year=2016).strip()
    print('Part 1: {}'.format(part1(prefix)))
    print('Part 2: {}'.format(part2(prefix)))
