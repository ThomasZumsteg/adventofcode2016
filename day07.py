#!/usr/bin/env python3

from get_input import get_input, line_parser
import re

def has_abba(word):
    for i in range(3, len(word)):
        outside_pair = word[i-3] == word[i]
        inside_pair = word[i-2] == word[i-1]
        not_same_pair = word[i-2] == word[i-3]
        if not not_same_pair and outside_pair and inside_pair:
            return True
    return False

def test_has_abba():
    assert has_abba('abba')
    assert has_abba('abbaa')
    assert has_abba('ccccabbaa')
    assert not has_abba('cccc')
    assert not has_abba('rustbucket')
    assert not has_abba('python')
    assert not has_abba('')
    assert not has_abba('nur')

def part1(line):
    count = 0
    for nets, hypers in lines:
        if all(not has_abba(h) for h in hypers) and any(has_abba(n) for n in nets):
            count += 1
    return count

def find_abas(line):
    abas = []
    for i in range(2, len(line)):
        if line[i] == line[i-2] and line[i] != line[i-1]:
            abas.append(line[i-1] + line[i] + line[i-1])
    return abas

def test_find_aba():
    assert [] == find_abas('abcde')
    assert ['bab'] == find_abas('aba')
    assert [] == find_abas('aaae')
    assert ['bab'] == find_abas('eabae')
    assert ['bab', 'aba', 'bab', 'aba'] == find_abas('ababab')


def part2(lines):
    count = 0
    for nets, hypers in lines:
        babs = [i for net in nets for i in find_abas(net)]
        for bab in babs:
            if any(bab in hyper for hyper in hypers):
                count += 1
                break
    return count
        
def parse(line):
    matches = re.findall(r'\w+', line)
    return ([matches[n] for n in range(0, len(matches), 2)],
        [matches[n] for n in range(1, len(matches), 2)])

if __name__ == '__main__':
    lines = line_parser(get_input(day=7, year=2016), parse=parse)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

