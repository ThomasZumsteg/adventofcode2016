#!/usr/bin/env python3

from get_input import get_input
from itertools import product
from copy import deepcopy
import sys
import re

def safe(floor):
    chips = [c[0] for c in floor if c[1] == 'chip']
    generators = [g[0] for g in floor if g[1] == 'generator']
    return len(generators) == 0 or all(c in generators for c in chips)

def test_safe():
    assert safe([])
    assert safe([('curium', 'chip')])
    assert safe([('plutonium', 'generator')])
    assert safe([('curium', 'chip'), ('potato', 'chip')])
    assert safe([('plutonium', 'generator'), ('snow', 'generator')])
    assert not safe([('curium', 'chip'), ('plutonium', 'generator')])
    assert safe([('curium', 'chip'), ('curium', 'generator')])
    assert safe([('curium', 'chip'), ('curium', 'generator'),
        ('plutonium', 'generator')])
    assert not safe([('curium', 'chip'), ('curium', 'generator'),
        ('promethium', 'chip'), ('plutonium', 'generator')])

def new_states(e, floors):
    old = [list(floor) for floor in floors]

    for f in (e+1, e-1):
        if not (0 <= f < len(floors)):
            continue
        for i in range(len(old[e])):
            for j in range(i+1, len(old[e])):
                new = deepcopy(old)
                new[f].append(new[e].pop(j))
                new[f].append(new[e].pop(i))
                yield f, tuple(frozenset(f) for f in new)
            new = deepcopy(old)
            new[f].append(new[e].pop(i))
            yield f, tuple(frozenset(f) for f in new)

def part1(inital_floors, start=0, prefix='P1'):
    seen = set()
    queue = [((start, inital_floors), 0)]
    while queue:
        (elevator, floors), steps = queue.pop(0)
        state = tuple(tuple(sorted(item[1] for item in floor)) for floor in floors)
        # print(state)
        if (elevator, state) in seen:
            continue
        if all(len(f) == 0 for f in floors[:-1]):
            return steps
        seen.add((elevator, state))
        # for f, floor in enumerate(floors):
        #     print("{:12} {:1}: {}".format(
        #         "{:2} {:2}/{:6}".format(prefix, steps, len(queue)) if f == 0 else '',
        #         'E' if f == elevator else ' ',
        #         ','.join('-'.join(i[:3] for i in item) for item in floor)))

        for move, new_floors in new_states(elevator, floors):
            if all(safe(f) for f in new_floors):
                queue.append(((move, new_floors), steps+1))

text = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""

def test_part1():
    setup = parse(text.strip())
    assert 11 == part1(setup)

def part2(inital_floors, prefix=''):
    floors = [set(f) for f in inital_floors]
    floors[0].update((('elerium', 'generator'), ('elerium', 'chip')))
    floors[0].update((('dilithium', 'generator'), ('dilithium', 'chip')))
    floors = tuple(frozenset(f) for f in floors)
    return part1(floors, prefix=prefix)
    

def parse(text):
    floors = []
    generator = re.compile(r'(\w+) generator')
    chips = re.compile(r'(\w+)-compatible microchip')
    for floor in text.splitlines():
        floors.append(set())
        for regex, suffix in ((generator, 'generator'), (chips, 'chip')):
            floors[-1].update((m, suffix) for m in regex.findall(floor))
    return tuple(frozenset(f) for f in floors)

if __name__ == '__main__':
    floors = parse(get_input(year=2016, day=11).strip())
    print("Part 1: {}".format(part1(floors)))
    print("Part 2: {}".format(part2(floors)))
