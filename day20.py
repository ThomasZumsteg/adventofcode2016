#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(addresses):
    lowest = 0
    for start, end in sorted(addresses):
        if start <= lowest <= end:
            lowest = end + 1
    return lowest

def part2(addresses):
    allowed_addresses = 0
    head = 0
    for start, end in sorted(addresses):
        if head < start:
            allowed_addresses += start - head
        head = max(end + 1, head)
    return 2**32 - head + allowed_addresses

def parse(line):
    return tuple(int(n) for n in line.split('-'))

if __name__ == '__main__':
    addresses = line_parser(get_input(day=20, year=2016), parse=parse)
    print('Part 1: {}'.format(part1(addresses)))
    print('Part 2: {}'.format(part2(addresses)))
