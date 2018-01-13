#!/usr/bin/env python3

from get_input import get_input, line_parser

def add(loc_a, loc_b, limit=(3,3)):
    loc_c = []
    for a, b, lim in zip(loc_a, loc_b, limit):
        assert 0 <= a + b < lim
        loc_c.append(a+b)
    return tuple(loc_c)

def part1(instructions):
    grid = (('1','2','3'),('4','5','6'),('7','8','9'))
    position = (1,1)
    moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    code = ""
    for instruction in instructions:
        for move in instruction:
            try:
                position = add(moves[move], position)
            except AssertionError:
                continue
        code += grid[position[0]][position[1]]
    return code

def new_add(loc_a, loc_b, limit=3):
    loc_c = []
    for a, b in zip(loc_a, loc_b):
        loc_c.append(a+b)
    assert sum(abs(c) for c in loc_c) < limit
    return tuple(loc_c)

def part2(instructions):
    grid = ((  "1"  ),
            ( "234" ),
            ("56789"),
            ( "ABC" ),
            (  "D"  ))

    position = (-2,0)
    moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    code = ""
    for instruction in instructions:
        for move in instruction:
            try:
                position = new_add(moves[move], position)
            except AssertionError:
                continue
        code += grid[2+position[0]][2-abs(position[0])+position[1]]
    return code

if __name__ == '__main__':
    instructions = line_parser(get_input(day=2, year=2016), parse=tuple)
    print("Part 1: {}".format(part1(instructions)))
    print("Part 2: {}".format(part2(instructions)))
