import copy
import io
import re
from typing import NamedTuple
import unittest


Stacks = list[list[str]]
class Step(NamedTuple):
    quantity: int
    a: int
    b: int
Procedure = list[Step]


def main():
    with open('5.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> tuple[Stacks, Procedure]:
    return _parse_stacks(file), _parse_procedure(file)


def _parse_stacks(file: io.TextIOBase) -> Stacks:
    # Read file until we hit an empty line.
    lines: list[str] = []
    for line in file:
        if line == '\n':
            break
        lines.append(line)

    # Determine number of stacks of crates.
    line = lines.pop()
    stack_count = int(line[-5:])

    # Parse starting stacks of crates.
    stacks: Stacks = [[] for _ in range(stack_count)]
    for line in reversed(lines):
        for i in range(0, len(line), 4):
            letter = line[i + 1:i + 2]
            if letter != ' ':
                stacks[i // 4].append(letter)

    return stacks


def _parse_procedure(file: io.TextIOBase) -> Procedure:
    procedure: Procedure = []
    for line in file:
        match = re.fullmatch(r'move (?P<quantity>\d+) '
                             r'from (?P<a>\d+) to (?P<b>\d+)\n', line)
        if not match:
            continue
        quantity = int(match.group('quantity'))
        a = int(match.group('a')) - 1
        b = int(match.group('b')) - 1
        procedure.append(Step(quantity, a, b))

    return procedure


def part_1(data: tuple[Stacks, Procedure]) -> str:
    stacks, procedure = data
    stacks = copy.deepcopy(stacks)

    for quantity, a, b in procedure:
        for _ in range(quantity):
            stacks[b].append(stacks[a].pop())

    return ''.join(stack[-1] for stack in stacks)


def part_2(data: tuple[Stacks, Procedure]) -> str:
    stacks, procedure = data
    stacks = copy.deepcopy(stacks)

    for quantity, a, b in procedure:
        stacks[b].extend(stacks[a][-quantity:])
        stacks[a] = stacks[a][:-quantity]

    return ''.join(stack[-1] for stack in stacks)


_TEST_INPUT = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class Test5(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_1(data), 'CMZ')

    def test_part_2(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_2(data), 'MCD')


if __name__ == '__main__':
    main()
