#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(triangles):
    count = 0
    for t in triangles:
        a, b, c = sorted(t)
        if a + b > c:
            count += 1
    return count

def group_by(items, n):
    group = []
    for i, item in enumerate(items, 1):
        group.append(item)
        if i % n == 0:
            yield tuple(group)
            group.clear()

def part2(triangles):
    count = 0
    for groups in group_by(triangles, 3):
        for group in zip(*groups):
            a, b, c = sorted(group)
            if a + b > c:
                count += 1
    return count

def parse(line):
    return tuple(int(n) for n in line.split())

if __name__ == '__main__':
    triangles = line_parser(get_input(day=3, year=2016), parse=parse)
    print("Part 1: {}".format(part1(triangles)))
    print("Part 2: {}".format(part2(triangles)))
