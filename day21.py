#!/usr/bin/env python3

from get_input import get_input, line_parser
import functools
import re

def part1(steps, start='abcdefgh'):
    pwd = start
    for step in steps:
        pwd = step(pwd)
    return pwd

def test_part1():
    lines = [
        ("swap position 4 with position 0", "ebcda"),
        ("swap letter d with letter b", "edcba"),
        ("reverse positions 0 through 4", "abcde"),
        ("rotate left 1 step", "bcdea"),
        ("move position 1 to position 4", "bdeac"),
        ("move position 3 to position 0", "abdec"),
        ("rotate based on position of letter b", "ecabd"),
        ("rotate based on position of letter d", "decab"),
    ]
    pwd = "abcde"
    for line, step in lines:
        print('{}: {}'.format(line, step))
        for regex, func in FUNCS.items():
            m = re.match(regex, line)
            if m:
                print('{}: {}'.format(func, m.groups()))
                assert step == func(pwd, *m.groups())
                pwd = step
                break
        else:
            assert False

def part2(steps, start='fbgdceah'):
    pwd = start
    for step in reversed(steps):
        pwd = step(pwd, reverse=True)
    return pwd

def test_part2():
    lines = [
        ("rotate based on position of letter d", "ecabd"),
        ("rotate based on position of letter b", "abdec"),
        ("move position 3 to position 0", "bdeac"),
        ("move position 1 to position 4", "bcdea"),
        ("rotate left 1 step", "abcde"),
        ("reverse positions 0 through 4","edcba"),
        ("swap letter d with letter b",  "ebcda"),
        ("swap position 4 with position 0","abcde"),
    ]
    pwd =  "decab"
    for line, step in lines:
        print('{}: {}'.format(line, step))
        f = parse(line)
        assert step == f(pwd, reverse=True)
        pwd = step

def parse(line):
    def pwd_func(func, *args, **kwargs):
        @functools.wraps(func)
        def wrapper(pwd, reverse=False):
            if reverse and func == rotate_pos:
                swaps = {'left': 'right', 'right': 'left'}
                args[0] = swaps[args[0]]
            elif reverse and func == rotate:
                kwargs['direction'] = 'left'
            return func(pwd, *args, **kwargs)
        return wrapper
    for regex, func in FUNCS.items():
        m = re.match(regex, line)
        if m is not None:
            return pwd_func(func, *m.groups())
    assert False

def move(pwd, start, end):
    letters = list(pwd)
    start, end = int(start), int(end)
    letters.insert(end, letters.pop(start))
    return  ''.join(letters)

def test_move():
    assert 'ba' == move('ab', 0, 1)

def reverse(pwd, start, end):
    letters = list(pwd)
    start, end = int(start), int(end)
    letters[start:end+1] = reversed(letters[start:end+1])
    return ''.join(letters)

def test_reverse():
    assert 'cba' == reverse('abc', 0, 2)
    assert 'adcbe' == reverse('abcde', 1, 3)

def rotate_pos(pwd, direction, steps):
    steps = int(steps) % len(pwd)
    if direction == 'right':
        steps = -steps
    return pwd[steps:] + pwd[:steps]

def test_rotate_pos():
    assert 'dabc' == rotate_pos('abcd', 'right', 1)
    assert 'bcda' == rotate_pos('abcd', 'left', 1)
    assert 'abcd' == rotate_pos('abcd', 'left', 4)
    assert 'abcd' == rotate_pos('abcd', 'right', 4)

def rotate(pwd, letter, direction='right'):
    index = pwd.index(letter)
    if direction == 'right':
        index += 1 if index < 4 else 2
    elif direction == 'left':
        index = 0
    return rotate_pos(pwd, direction, index)

def swap(pwd, a, b):
    return swap_pos(pwd, pwd.index(a), pwd.index(b))

def swap_pos(pwd, i, j):
    letters = list(pwd) 
    i, j = int(i), int(j)
    letters[i], letters[j] = letters[j], letters[i]
    return ''.join(letters)

def test_swap_pos():
    assert "cba" == swap_pos('abc', 0, 2)

FUNCS =  {
    r'move position (\d+) to position (\d+)': move,
    r'reverse positions (\d+) through (\d+)': reverse, 
    r'rotate based on position of letter (.)': rotate,
    r'rotate (left|right) (\d+) steps?': rotate_pos,
    r'swap letter (.) with letter (.)': swap, 
    r'swap position (\d+) with position (\d+)': swap_pos, 
    }

if __name__ == '__main__':
    lines = line_parser(get_input(day=21, year=2016), parse=parse)
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
