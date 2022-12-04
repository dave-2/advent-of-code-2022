import io
import unittest


Range = tuple[int, int]
Assignments = list[tuple[Range, Range]]


def main():
    with open('4.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> Assignments:
    assignments: Assignments = []
    for line in file:
        first, second = line.split(',')
        a, b = first.split('-')
        c, d = second.split('-')
        assignments.append(((int(a), int(b)), (int(c), int(d))))

    return assignments


def part_1(data: Assignments) -> int:
    return sum(1 if a >= c and b <= d or a <= c and b >= d else 0
               for (a, b), (c, d) in data)


def part_2(data: Assignments) -> int:
    return sum(1 if a <= d and b >= c else 0 for (a, b), (c, d) in data)


class Test4(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO('2-4,6-8\n2-3,4-5\n5-7,7-9\n'
                            '2-8,3-7\n6-6,4-6\n2-6,4-8\n')
        data = parse_input(input)
        self.assertEqual(part_1(data), 2)

    def test_part_2(self):
        input = io.StringIO('2-4,6-8\n2-3,4-5\n5-7,7-9\n'
                            '2-8,3-7\n6-6,4-6\n2-6,4-8\n')
        data = parse_input(input)
        self.assertEqual(part_2(data), 4)


if __name__ == '__main__':
    main()
