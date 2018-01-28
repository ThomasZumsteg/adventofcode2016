#!/usr/bin/env python3

from get_input import get_input, line_parser
from itertools import cycle
import logging

log = logging.getLogger(__name__)

def part1(n):
    l = 1
    while l < n:
        l *= 2
    return 2 * n - l + 1

def test_part1():
    assert 3 == part1(5)

def josephus(start, k_gen):
    survivor = 0
    for members, kill in zip(range(2, start+1), k_gen):
        if kill - 1 <= survivor:
            survivor = (survivor + 2) % members
        else:
            survivor = (survivor + 1) % members
        # Skip string concatination unless needed, extremely slow
        if log.level <= logging.DEBUG:
            lookup = { survivor: '?', kill: 'k' }
            log.debug('{}: {}: {}'.format(survivor, kill, 
                ' '.join('x' if p not in lookup else lookup[p] 
                    for p in range(1+members))))
    return survivor + 1

def test_josephus():
    assert 3 == josephus(5, cycle([1]))
    assert 2 == josephus(5, ((k // 2) + 1 for k in range(5-1)))
    for i in range(3, 30):
        assert brute(i, cycle([1])) == josephus(i, cycle([1]))
        joseph_gen = lambda n: ((k // 2) + 1 for k in range(n-1))
        brute_gen = lambda n: ((k // 2) + 1 for k in reversed(range(n-1)))
        assert brute(i, brute_gen(i)) == josephus(i, joseph_gen(i))

def brute(n_elves, k_gen, debug=False):
    elves = list(range(1, n_elves+1))
    e = 0
    for kill in k_gen:
        if len(elves) == 1:
            break
        log.debug('{}: {}'.format(kill, elves))
        elves.pop(kill)
        elves.append(elves.pop(0))
    assert len(elves) != 0
    return elves[0]

def test_brute():
    assert 3 == brute(5, cycle([1]))
    assert 2 == brute(5, ((k // 2) + 1 for k in reversed(range(5-1))))
    assert 3 == brute(6, ((k // 2) + 1 for k in reversed(range(6-1))))
    assert 5 == brute(7, ((k // 2) + 1 for k in reversed(range(7-1))))

def part2(n):
    kills = ((k // 2) + 1 for k in range(n-1))
    return josephus(n, kills)

if __name__ == '__main__':
    log.setLevel(logging.INFO)
    lines = int(get_input(day=19, year=2016).strip())
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
