import io
import unittest


def main():
    with open('6.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> str:
    return file.read()


def part_1(data: str) -> int:
    range_size = 4
    for index in range(range_size, len(data)):
        if len(set(data[index - range_size:index])) == range_size:
            return index
    raise ValueError(f'Signal contains no start-of-packet marker: "{data}"')


def part_2(data: str) -> int:
    range_size = 14
    for index in range(range_size, len(data)):
        if len(set(data[index - range_size:index])) == range_size:
            return index
    raise ValueError(f'Signal contains no start-of-message marker: "{data}"')


class Test6(unittest.TestCase):

    def test_part_1_example_1(self):
        input = io.StringIO('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(part_1(parse_input(input)), 7)

    def test_part_1_example_2(self):
        input = io.StringIO('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(part_1(parse_input(input)), 5)

    def test_part_1_example_3(self):
        input = io.StringIO('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(part_1(parse_input(input)), 6)

    def test_part_1_example_4(self):
        input = io.StringIO('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(part_1(parse_input(input)), 10)

    def test_part_1_example_5(self):
        input = io.StringIO('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(part_1(parse_input(input)), 11)

    def test_part_2_example_1(self):
        input = io.StringIO('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(part_2(parse_input(input)), 19)

    def test_part_2_example_2(self):
        input = io.StringIO('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(part_2(parse_input(input)), 23)

    def test_part_2_example_3(self):
        input = io.StringIO('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(part_2(parse_input(input)), 23)

    def test_part_2_example_4(self):
        input = io.StringIO('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(part_2(parse_input(input)), 29)

    def test_part_2_example_5(self):
        input = io.StringIO('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(part_2(parse_input(input)), 26)


if __name__ == '__main__':
    main()
