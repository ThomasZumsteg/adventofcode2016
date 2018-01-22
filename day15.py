#!/usr/bin/env python3

from get_input import get_input, line_parser
from itertools import count
import re

def part1(disks):
    for time in count(0):
        for disk, holes, start in disks:
            if (time + disk + start) % holes != 0:
                break
        else:
            return time

def test_part1():
    disks = ((1, 5, 4), (2, 2, 1))
    assert 5 == part1(disks)

def part2(disks):
    return part1(disks + [(len(disks)+1, 11, 0)])

def parse(line):
    frmt = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'
    return tuple(int(g) for g in re.match(frmt, line).groups())

if __name__ == '__main__':
    disks = line_parser(get_input(day=15, year=2016), parse=parse)
    print("Part 1: {}".format(part1(disks)))
    print("Part 2: {}".format(part2(disks)))
