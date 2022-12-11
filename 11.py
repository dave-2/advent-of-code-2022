from __future__ import annotations

import collections
import copy
import io
import math
from typing import Callable
import unittest


class Monkey:

    def __init__(self, items: list[int], operation: Callable[[int], int],
                 test: int, friend_a: int, friend_b: int):
        self.items = collections.deque(items)
        self.operation = operation
        self.test = test
        self.friend_a = friend_a
        self.friend_b = friend_b

    @staticmethod
    def from_string(string: str) -> Monkey:
        lines = string.split('\n')
        items = list(map(int, lines[1][18:].split(', ')))
        operation = Monkey._parse_operation(lines[2][19:])
        test = int(lines[3][21:])
        friend_a = int(lines[4][29:])
        friend_b = int(lines[5][30:])
        return Monkey(items, operation, test, friend_a, friend_b)

    @staticmethod
    def _parse_operation(string: str) -> Callable[[int],int]:
        left, operator, right = string.split(' ')

        def _operation(old: int) -> int:
            a = old if left == 'old' else int(left)
            b = old if right == 'old' else int(right)
            if operator == '+': return a + b
            if operator == '*': return a * b
            raise ValueError(f'Unknown operator: "{operator}"')

        return _operation


def main():
    with open('11.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> list[Monkey]:
    monkeys: list[Monkey] = []

    while True:
        monkey_string = ''.join(file.readline() for _ in range(7))
        if not monkey_string:
            break
        monkeys.append(Monkey.from_string(monkey_string))

    return monkeys


def part_1(data: list[Monkey]) -> int:
    return _monkey_business(data, 20, True)


def part_2(data: list[Monkey]) -> int:
    return _monkey_business(data, 10000, False)


def _monkey_business(data: list[Monkey], rounds: int,
                     worry_relief: bool) -> int:
    monkeys = copy.deepcopy(data)
    inspections_by_monkey = [0] * len(monkeys)

    lcm = math.lcm(*(monkey.test for monkey in monkeys))

    for _ in range(rounds):
        for index, monkey in enumerate(monkeys):
            while monkey.items:
                inspections_by_monkey[index] += 1
                item = monkey.operation(monkey.items.popleft())
                if worry_relief:
                    item //= 3
                item %= lcm
                monkeys[monkey.friend_b if item % monkey.test
                    else monkey.friend_a].items.append(item)

    inspections_by_monkey.sort(reverse=True)
    return inspections_by_monkey[0] * inspections_by_monkey[1]


_TEST_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Test11(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_1(data), 10605)

    def test_part_2(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_2(data), 2713310158)


if __name__ == '__main__':
    main()
