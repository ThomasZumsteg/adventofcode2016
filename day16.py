#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(line, space=272):
    curve = line[:]
    while len(curve) < space:
        curve = expand(curve)
    return ''.join(checksum(curve[:space]))

def checksum(items):
    while len(items) % 2 == 0:
        check = []
        for a, b in ((items[i], items[i+1]) for i in range(0, len(items), 2)):
            check.append('1' if a == b else '0')
        items = check
    return items

def test_checksum():
    assert list('1') == checksum('11')
    assert list('1') == checksum('00')
    assert list('0') == checksum('10')
    assert list('0') == checksum('01')
    assert list('100') == checksum('110010110100')

def expand(curve):
    new_curve = list(curve)
    new_curve.append('0')
    replace = {'0': '1', '1': '0'}
    for d in reversed(curve):
        new_curve.append(replace[d])
    return new_curve

def test_expand():
    assert list('100') == expand('1')
    assert list('001') == expand('0')
    assert list('11111000000') == expand('11111')
    assert list('1111000010100101011110000') == expand('111100001010')

def part2(line, space=35651584):
    return part1(line, space=space)

if __name__ == '__main__':
    line = get_input(day=16, year=2016).strip()
    print('Part 1: {}'.format(part1(line)))
    print('Part 2: {}'.format(part2(line)))
