#!/usr/bin/env python3

from get_input import get_input, line_parser
import re
from collections import Counter

def part1(sectors):
    total = 0
    for name, id_num, checksum in sectors:
        counts = Counter(c for c in name if c != '-')
        key = sorted(counts.items(), key=lambda v: (-v[1], v[0]))
        check = ''.join(k[0] for k in key[:5])
        if check == checksum:
            total += id_num
    return total

def part2(sectors):
    for name, shift, _ in sectors:
        word = ''
        for c in name:
            if c == '-':
                word += ' '
            else:
                word += chr(((ord(c) - 97 + shift) % 26) + 97)
        if 'northpole' in word:
            return shift

def parse(line):
    m = re.match(r'([a-z-]+)-(\d+)\[([a-z]{5})\]$', line)
    name, id_num, checksum = m.groups()
    return (name, int(id_num), checksum)

if __name__ == '__main__':
    sectors = line_parser(get_input(day=4, year=2016), parse=parse)
    print("Part 1: {}".format(part1(sectors)))
    print("Part 2: {}".format(part2(sectors)))
