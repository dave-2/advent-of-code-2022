import functools
import io
import unittest


def main():
    with open('3.input') as file:
        contents = parse_input(file)
    print('Part One:', part_1(contents))
    print('Part Two:', part_2(contents))


def parse_input(file: io.TextIOBase) -> list[str]:
    return [line.strip() for line in file]


def part_1(contents: list[str]) -> int:
    return sum(map(_rucksack_priority, contents))


def _rucksack_priority(rucksack: str) -> int:
    half_length = len(rucksack) // 2
    first = rucksack[:half_length]
    second = rucksack[half_length:]
    shared_item = (set(first) & set(second)).pop()
    return priority(shared_item)


def part_2(contents: list[str]) -> int:
    grouped_rucksacks = zip(*[iter(contents)] * 3)
    return sum(map(_group_priority, grouped_rucksacks))


def _group_priority(group: tuple[str]) -> int:
    group_sets = (set(g) for g in group)
    shared_item = functools.reduce(lambda a, b: a & b, group_sets).pop()
    return priority(shared_item)


def priority(item: str) -> int:
    if item < 'a': return ord(item) - 38
    return ord(item) - 96


class Test3(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO('vJrwpWtwJgWrhcsFMMfFFhFp\n'
                            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
                            'PmmdzqPrVvPwwTWBwg\n'
                            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
                            'ttgJtRGJQctTZtZT\n'
                            'CrZsJsPPZsGzwwsLwLmpwMDw\n')
        contents = parse_input(input)
        self.assertEqual(part_1(contents), 157)

    def test_part_2(self):
        input = io.StringIO('vJrwpWtwJgWrhcsFMMfFFhFp\n'
                            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
                            'PmmdzqPrVvPwwTWBwg\n'
                            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
                            'ttgJtRGJQctTZtZT\n'
                            'CrZsJsPPZsGzwwsLwLmpwMDw\n')
        contents = parse_input(input)
        self.assertEqual(part_2(contents), 70)


if __name__ == '__main__':
    main()
