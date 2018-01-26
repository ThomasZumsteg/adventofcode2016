#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(n):
    l = 1
    while l < n:
        l *= 2
    return 2 * n - l + 1

def test_part1():
    assert 3 == part1(5)

def brute2(n_elves, debug=False):
    elves = list(range(1, n_elves+1))
    e = 0
    while len(elves) > 1:
        r = (e + len(elves) // 2) % len(elves)
        if debug:
            print('{:2},'.format(elves.pop(r)), end='')
        else:
            elves.pop(r)
        if r > e:
            e = (e + 1) % len(elves)
    if debug:
        print('{:2}'.format(elves[0]))
    return elves[0]

def part2(n):
    pass

def test_part2():
    for i in range(1, 40):
        brute2(i, debug=True)
    assert False

if __name__ == '__main__':
    lines = int(get_input(day=19, year=2016).strip())
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

