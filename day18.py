#!/usr/bin/env python3

from get_input import get_input, line_parser

def trap_gen(init):
    state = init[:]
    trap_states = ('^^.', '.^^', '^..', '..^')
    while True:
        yield state
        new_state = ''
        for i in range(len(state)):
            if i == 0:
                state_slice = '.' + state[:2]
            elif i+1 == len(state):
                state_slice = state[-2:] + '.'
            else:
                state_slice = state[i-1:i+2]
            if state_slice in trap_states:
                new_state += '^'
            else:
                new_state += '.'
        state = new_state

def test_trap_gen():
    g = trap_gen('..^^.')
    assert '..^^.' == next(g)
    assert '.^^^^' == next(g)
    assert '^^..^' == next(g)

def part1(traps, rows=40):
    safe_tiles = 0
    for i, row in enumerate(trap_gen(traps)):
        if i >= rows:
            return safe_tiles
        safe_tiles += sum(1 if t == '.' else 0 for t in row)

def test_part1():
    assert 38 == part1('.^^.^.^^^^', rows=10)

def part2(traps):
    return part1(traps, rows=400000)

if __name__ == '__main__':
    traps = get_input(day=18, year=2016).strip()
    print('Part 1: {}'.format(part1(traps)))
    print('Part 2: {}'.format(part2(traps)))
