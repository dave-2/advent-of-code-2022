import io
from typing import Callable, Iterator, TypeVar
import unittest


def main():
    with open('10.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:')
    print(part_2(data))


def parse_input(file: io.TextIOBase) -> list[str]:
    return list(file)


def part_1(data: list[str]) -> int:
    return sum(_simulate_system(_signal_strengths, data))


def _signal_strengths(cycle: int, x: int) -> int:
    return cycle * x if cycle in (20, 60, 100, 140, 180, 220) else 0


def part_2(data: list[str]) -> str:
    return ''.join(_simulate_system(_draw_pixel, data))


def _draw_pixel(cycle: int, x: int) -> str:
    pixel = '#' if abs(x - (cycle - 1) % 40) <= 1 else '.'
    return pixel + '\n' if cycle % 40 == 0 else pixel


T = TypeVar('T')
def _simulate_system(
        f: Callable[[int, int], T], instructions: list[str]) -> Iterator[T]:
    cycle = 0
    x = 1

    for instruction in instructions:
        cycle += 1
        yield f(cycle, x)
        if not instruction.startswith('addx'):
            continue
        cycle += 1
        yield f(cycle, x)
        x += int(instruction[5:])


_TEST_INPUT = """addx 15\naddx -11\naddx 6\naddx -3\naddx 5
addx -1\naddx -8\naddx 13\naddx 4\nnoop
addx -1\naddx 5\naddx -1\naddx 5\naddx -1
addx 5\naddx -1\naddx 5\naddx -1\naddx -35
addx 1\naddx 24\naddx -19\naddx 1\naddx 16
addx -11\nnoop\nnoop\naddx 21\naddx -15
noop\nnoop\naddx -3\naddx 9\naddx 1
addx -3\naddx 8\naddx 1\naddx 5\nnoop
noop\nnoop\nnoop\nnoop\naddx -36
noop\naddx 1\naddx 7\nnoop\nnoop
noop\naddx 2\naddx 6\nnoop\nnoop
noop\nnoop\nnoop\naddx 1\nnoop
noop\naddx 7\naddx 1\nnoop\naddx -13
addx 13\naddx 7\nnoop\naddx 1\naddx -33
noop\nnoop\nnoop\naddx 2\nnoop
noop\nnoop\naddx 8\nnoop\naddx -1
addx 2\naddx 1\nnoop\naddx 17\naddx -9
addx 1\naddx 1\naddx -3\naddx 11\nnoop
noop\naddx 1\nnoop\naddx 1\nnoop
noop\naddx -13\naddx -19\naddx 1\naddx 3
addx 26\naddx -30\naddx 12\naddx -1\naddx 3
addx 1\nnoop\nnoop\nnoop\naddx -9
addx 18\naddx 1\naddx 2\nnoop\nnoop
addx 9\nnoop\nnoop\nnoop\naddx -1
addx 2\naddx -37\naddx 1\naddx 3\nnoop
addx 15\naddx -21\naddx 22\naddx -6\naddx 1
noop\naddx 2\naddx 1\nnoop\naddx -10
noop\nnoop\naddx 20\naddx 1\naddx 2
addx 2\naddx -6\naddx -11\nnoop\nnoop
noop
"""


class Test10(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_1(data), 13140)

    def test_part_2(self):
        output = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_2(data), output)


if __name__ == '__main__':
    main()
