#!/usr/bin/env python3

from get_input import get_input
from itertools import count
import re
from hashlib import md5

def hash(val, salt, iters=0):
    h = salt + str(val)
    for _ in range(iters+1):
        h = md5(h.encode()).hexdigest() 
    return h

def test_hash():
    assert "888" in hash(18, 'abc')
    assert "a107ff634856bb300138cac6568c0f24" == hash(0, 'abc', iters=2016)
    assert "222" in hash(5, 'abc', iters=2016)

def key_gen(salt, buff_size=1000, iters=0):
    buff = [hash(i, salt, iters=iters) for i in range(buff_size)]
    for i in count(0):
        h = buff.pop(0)
        buff.append(hash(i + buff_size, salt, iters=iters))
        m = re.search(r'(.)\1{2}', h)
        if m:
            group = m.group(1)
            if any(group * 5 in b for b in buff):
                yield i, h
                continue

def test_key_gen():
    gen = key_gen('abc')
    k, key = next(gen)
    assert k == 39
    assert 'eee' in key
    k, key = next(gen)
    assert k == 92
    assert '999' in key

def test_key_gen2():
    gen = key_gen('abc', iters=2016)
    k, key = next(gen)
    assert k == 10
    assert 'eee' in key

def part1(salt):
    keys = []
    for i, key in key_gen(salt):
        keys.append(key)
        if len(keys) >= 64:
            return i

def test_part1():
    assert 22728 == part1('abc')

def part2(salt):
    keys = []
    for i, key in key_gen(salt, iters=2016):
        keys.append(key)
        if len(keys) >= 64:
            return i

if __name__ == '__main__':
    salt = get_input(day=14, year=2016).strip()
    print("Part 1: {}".format(part1(salt)))
    print("Part 2: {}".format(part2(salt)))
