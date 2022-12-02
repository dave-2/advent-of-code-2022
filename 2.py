from __future__ import annotations

import enum
import io
import unittest


class Shape(enum.IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def score(self) -> int:
        return self + 1

    def battle(self, opponent: Shape) -> int:
        if self == opponent: return 3
        if self == (opponent + 1) % 3: return 6
        return 0

    @staticmethod
    def from_letter(letter: str) -> Shape:
        if letter == 'A' or letter == 'X': return Shape.ROCK
        if letter == 'B' or letter == 'Y': return Shape.PAPER
        if letter == 'C' or letter == 'Z': return Shape.SCISSORS
        raise ValueError(f'Unknown shape: "{letter}"')

    @staticmethod
    def from_tactic(opponent: Shape, tactic: str) -> Shape:
        if tactic == 'X': return Shape((opponent - 1) % 3)
        if tactic == 'Y': return opponent
        if tactic == 'Z': return Shape((opponent + 1) % 3)
        raise ValueError(f'Unknown shape: "{tactic}"')


Round = tuple[Shape, str]
StrategyGuide = list[Round]


def main():
    with open('2.input') as file:
        guide = parse_input(file)
    print('Part One:', part_1(guide))
    print('Part Two:', part_2(guide))


def parse_input(file: io.TextIOBase) -> StrategyGuide:
    return list(map(parse_line, file))


def parse_line(line: str) -> Round:
    a, b = line.strip().split(' ')
    return Shape.from_letter(a), b


def part_1(guide: StrategyGuide) -> int:
    return sum(score_round(Shape.from_letter(self), opponent)
               for opponent, self in guide)


def part_2(guide: StrategyGuide) -> int:
    return sum(score_round(Shape.from_tactic(opponent, tactic), opponent)
               for opponent, tactic in guide)


def score_round(self: Shape, opponent: Shape):
    return self.battle(opponent) + self.score()


class Test2(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO('A Y\nB X\nC Z\n')
        guide = parse_input(input)
        self.assertEqual(part_1(guide), 15)

    def test_part_2(self):
        input = io.StringIO('A Y\nB X\nC Z\n')
        guide = parse_input(input)
        self.assertEqual(part_2(guide), 12)


if __name__ == '__main__':
    main()
