#!/usr/bin/env python3

from get_input import get_input

def wall(pos, number):
    c, r = pos
    digits = c*c + 3*c + 2*c*r + r + r*r + number
    binary = format(digits, 'b')
    return sum(1 if d == '1' else 0 for d in binary) % 2 == 1

TEXT = """.#.####.##
..#..#...#
#....##...
###.#.###.
.##..#..#.
..##....#.
#...##.###"""

def test_wall():
    number = 10
    text = [list(line) for line in TEXT.splitlines()]
    print(text)
    for r in range(6):
        for c in range(10):
            assert (text[r][c] == '#') == wall((c, r), number)

def part1(number, start=(1,1), end=(31,39)):
    seen = set()
    queue = [(start, 0)]
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) in seen:
            continue
        seen.add((x,y))
        if (x, y) == end:
            return steps
        for (c,r) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= c and 0 <= r and not wall((c, r), number):
                queue.append(((c,r), steps + 1))

def test_part1():
    assert 11 == part1(10, end=(7, 4))

def part2(number, start=(1,1)):
    seen = set()
    queue = [(start, 0)]
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) in seen:
            continue
        seen.add((x,y))
        for (c,r) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= c and 0 <= r and not wall((c, r), number) and steps < 50:
                queue.append(((c,r), steps + 1))
    return len(seen)

if __name__ == '__main__':
    number = int(get_input(day=13, year=2016))
    print("Part 1: {}".format(part1(number)))
    print("Part 2: {}".format(part2(number)))
