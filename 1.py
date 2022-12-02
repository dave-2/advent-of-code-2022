import io
import unittest


def main():
    with open('1.input') as file:
        calories = parse_input(file)
    print('Part One:', part_1(calories))
    print('Part Two:', part_2(calories))


def parse_input(file: io.TextIOBase) -> list[list[int]]:
    all_calories: list[list[int]] = []
    current_calories: list[int] = []

    for line in file:
        if line == '\n':
            all_calories.append(current_calories)
            current_calories = []
            continue
        current_calories.append(int(line))
    all_calories.append(current_calories)

    return all_calories


def part_1(calories: list[list[int]]) -> int:
    return max(map(sum, calories))


def part_2(calories: list[list[int]]) -> int:
    return sum(sorted(map(sum, calories), reverse=True)[:3])


class Test1(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO('1000\n2000\n3000\n\n4000\n\n5000\n'
                            '6000\n\n7000\n8000\n9000\n\n10000\n')
        guide = parse_input(input)
        self.assertEqual(part_1(guide), 24000)

    def test_part_2(self):
        input = io.StringIO('1000\n2000\n3000\n\n4000\n\n5000\n'
                            '6000\n\n7000\n8000\n9000\n\n10000\n')
        guide = parse_input(input)
        self.assertEqual(part_2(guide), 45000)


if __name__ == '__main__':
    main()
