#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import Counter

def part1(lines):
    phrase_counter = [Counter() for _ in range(len(lines[0]))]
    for line in lines:
        for i, c in enumerate(line):
            phrase_counter[i][c] += 1 
    return ''.join(max(p.items(), key=lambda q: q[1])[0] for p in phrase_counter)

def part2(lines):
    phrase_counter = [Counter() for _ in range(len(lines[0]))]
    for line in lines:
        for i, c in enumerate(line):
            phrase_counter[i][c] += 1 
    return ''.join(min(p.items(), key=lambda q: q[1])[0] for p in phrase_counter)
    

if __name__ == '__main__':
    lines = line_parser(get_input(day=6, year=2016), parse=lambda l: tuple(l), seperator='\n')
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
