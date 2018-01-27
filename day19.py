#!/usr/bin/env python3

from get_input import get_input, line_parser
from itertools import cycle

def part1(n):
    l = 1
    while l < n:
        l *= 2
    return 2 * n - l + 1

def test_part1():
    assert 3 == part1(5)

# ?
# ? k
# x k ?
# ? x k x
# x ? k x x
# x x ? k x x
# x x x k ? x x
# x x x x k x ? x

# ?
# ? k
# x k ?
# ? k x x
# x k ? x x
# x k x x ? x
# x k x x x x ?
# ? k x x x x x x
# x k ? x x x x x x

# ?
# ? k
# x k ?
# ? k x x
# x k ? x x
# x k x ? x x
# x k x x x ? x
# ? k x x x x x x
# x k ? x x x x x x

def josephus(start, k_gen):
    survivor = 0
    for n, k in zip(range(1, start+1), k_gen):
        if survivor == k:
            survivor += 1
        lookup = { survivor: '?', k: 'k' }
        print('{}: {}: {}'.format(survivor, k, ' '.join('x' if p not in lookup else lookup[p] for p in range(n))))
        if k + 1 < survivor:
            survivor = (survivor + 2) % n
        else:
            survivor = (survivor + 1) % n
    return survivor + 1

def test_josephus():
    assert 3 == josephus(9, cycle([1]))
    for n in range(2, 20):
        j = josephus(n, cycle([1]))
        assert part1(n) == j
        assert n == josephus(n, cycle([0]))

def brute2(n_elves, debug=False):
    elves = list(range(1, n_elves+1))
    e = 0
    while len(elves) > 1:
        r = (e + len(elves) // 2) % len(elves)
        if debug:
            print('{:2},'.format(elves.pop(r)), end='')
        else:
            elves.pop(r)
        if r > e:
            e = (e + 1) % len(elves)
    if debug:
        print('{:2}'.format(elves[0]))
    return elves[0]

def part2(n):
    kills = [(k // 2) + 1 for k in range(n-1)]
    return josephus(n, kills)

def test_part2():
    assert 1 == brute2(2)
    assert 3 == brute2(3)
    assert 1 == part2(4)
    assert 1 == brute2(4)
    assert 2 == brute2(5)

if __name__ == '__main__':
    lines = int(get_input(day=19, year=2016).strip())
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

# 1 2 3 4
# 1 2   4
# 1 2    
# 1

# 1 2 3 4 5
# 1 2   4 5
# 1 2   4  
#   2   4  
#   2      

# 1 2 3 4 5 6
# 1 2 3   5 6
# 1 2 3     6
#   2 3     6
#     3     6
#     3

# 1 2 3 4 5 6 7
# 1 2 3   5 6 7
# 1 2 3   5   7
# 1 2 3   5
# 1   3   5
# 1       5
#         5

# 1 2 3 4 5 6 7 8
# 1 2 3 4   6 7 8
# 1 2 3 4     7 8
# 1 2 3 4     7  
#   2 3 4     7  
#   2   4     7  
#   2         7  
#             7  
