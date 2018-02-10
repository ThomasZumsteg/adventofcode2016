#!/usr/bin/env python3

from get_input import get_input, line_parser

def state_generator(initial_state):
    queue = [(0, initial_state)]
    seen = set()
    while queue:
        steps, state = queue.pop(0)

        if state in seen:
            continue
        seen.add(state)

        new_state = yield steps, state
        while new_state is not None:
            queue.append((steps+1, new_state))
            new_state = yield

def part1(lines, start, all_digits):
    gen = state_generator((start, frozenset('0')))
    for steps, ((r, c), digits) in gen:
        if digits == all_digits:
            return steps
        for i, j in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            new_digits = set(digits)
            if lines[i][j] == '#':
                continue
            elif lines[i][j].isdigit():
                new_digits.add(lines[i][j])
            gen.send(((i,j), frozenset(new_digits)))

TEST_MAZE= [
    "###########",
    "#0.1.....2#",
    "#.#######.#",
    "#4.......3#",
    "###########",
    ]

def test_part1():
    assert 14 == part1(*parse(TEST_MAZE))

def part2(lines, start, all_digits):
    gen = state_generator((start, frozenset('0')))
    for steps, ((r, c), digits) in gen:
        if digits == all_digits and lines[r][c] == '0':
            return steps
        for i, j in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            new_digits = set(digits)
            if lines[i][j] == '#':
                continue
            elif lines[i][j].isdigit():
                new_digits.add(lines[i][j])
            gen.send(((i,j), frozenset(new_digits)))

def parse(text):
    all_digits = set()
    lines = []
    for r, row in enumerate(text.splitlines()):
        row = row.strip()
        lines.append(row)
        for c, char in enumerate(row):
            if char == '0':
                start = (r, c)
            if char.isdigit():
                all_digits.add(char)
    return tuple(lines), start, frozenset(all_digits)

if __name__ == '__main__':
    args = parse(get_input(day=24, year=2016))
    print("Part 1: {}".format(part1(*args)))
    print("Part 2: {}".format(part2(*args)))
