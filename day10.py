#!/usr/bin/env python3

from get_input import get_input, line_parser
import re
from copy import deepcopy
from collections import defaultdict

class Runner(object):
    def __init__(self, text):
        self._states = {'bot': defaultdict(set), 'output': defaultdict(set)}
        self.output = self._states['output']
        self._commands = {}
        self._input = []
        self.parse(text)

    def parse(self, text):
        transfer_command = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
        send_to_bot_command = re.compile(r'value (\d+) goes to bot (\d+)')

        for line in text.splitlines():
            m = transfer_command.match(line)
            if m:
                bot, *args = m.groups()
                self._commands[int(bot)] = (line, args[0], int(args[1]),
                        args[2], int(args[3]))

            m = send_to_bot_command.match(line)
            if m:
                self._input.append((line, int(m.group(1)), int(m.group(2))))

    def run(self, output=None):
        while True:
            yield self._states[output]
            bot_keys = list(self._states['bot'].keys())
            for b in bot_keys:
                bot = self._states['bot'][b]
                if len(bot) == 2:
                    line, low_state, low_bin, high_state, high_bin = self._commands[b]
                    # print(line)
                    low_val, high_val = sorted(bot)
                    self._states[low_state][low_bin].add(low_val)
                    self._states[high_state][high_bin].add(high_val)
                    bot.clear()
                    break 
            else:
                try:
                    line, val, b = self._input.pop(0)
                except IndexError:
                    raise StopIteration
                # print(line)
                self._states['bot'][b].add(val)

def part1(runner):
    # comparing value-61 microchips with value-17 microchips 
    runner = deepcopy(runner)
    for bot in runner.run(output='bot'):
        for b, bot in bot.items():
            if 61 in bot and 17 in bot:
                return b

text = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

def test_runner():
    runner = Runner(text.strip())
    for bots in runner.run('bot'):
        print(bots)
    assert runner.output == {0:{5,}, 1:{2,}, 2:{3,}}

def part2(runner):
    runner = deepcopy(runner)
    for output in runner.run(output='output'):
        if len(output[0]) > 0 and len(output[1]) > 0 and len(output[2]) > 0:
            return output[0].pop() * output[1].pop() * output[2].pop()

if __name__ == '__main__':
    runner = Runner(get_input(day=10, year=2016))
    print("Part 1: {}".format(part1(runner)))
    print("Part 2: {}".format(part2(runner)))
