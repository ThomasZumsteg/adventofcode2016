#!/usr/bin/env python3

from get_input import get_input
import re

def part1(text):
    chars = 0
    for i, group in parse(text, recurse=False):
        chars += i * len(group)
    return chars

def part2(text):
    chars = 0
    queue = parse(text, recurse=True)
    while queue:
        i, group = queue.pop()
        if type(group) is str:
            chars += i * len(group)
        else:
            for (j, sub_group) in group:
                queue.append((i * j, sub_group))
    return chars

def parse(text, recurse=False):
    groups = []
    group = ''
    i = 0
    while i < len(text):
        m = re.match(r'^\((\d+)x(\d+)\)', text[i:])
        if m is None:
            group += text[i]
            i += 1
        else:
            if group is not '':
                groups.append((1, group))
                group = ''
            i += m.end(0)
            chars, repeat = (int(g) for g in m.groups())
            if recurse:
                groups.append((repeat, parse(text[i:i+chars], recurse=True)))
            else:
                groups.append((repeat, text[i:i+chars]))
            i += chars
    if group is not '':
        groups.append((1, group))
    return groups

def test_decompress_len():
    assert part2("(3x3)XYZ") == 9

if __name__ == '__main__':
    lines = get_input(day=9, year=2016).strip()
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
