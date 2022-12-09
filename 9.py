import io
import unittest


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


def main():
    with open('9.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> list[tuple[tuple[int, int], int]]:
    return [(_direction_from_string(line[0]), int(line[2:])) for line in file]


def _direction_from_string(string: str) -> tuple[int, int]:
    if string == 'L': return LEFT
    if string == 'R': return RIGHT
    if string == 'U': return UP
    if string == 'D': return DOWN
    raise ValueError(f'Unknown direction "{string}"')


def part_1(data: list[tuple[tuple[int, int], int]]) -> int:
    return _simulate_rope(data, 2)


def part_2(data: list[tuple[tuple[int, int], int]]) -> int:
    return _simulate_rope(data, 10)


def _simulate_rope(data: list[tuple[tuple[int, int], int]],
                   rope_length: int) -> int:
    rope = [[0, 0] for _ in range(rope_length)]
    visited: set[tuple[int, int]] = set([(0, 0)])
    for (dx, dy), distance in data:
        for _ in range(distance):
            rope[0][0] += dx
            rope[0][1] += dy
            dx_i = dx
            dy_i = dy
            for i in range(1, len(rope)):
                x_too_far = abs(rope[i - 1][0] - rope[i][0]) > 1
                y_too_far = abs(rope[i - 1][1] - rope[i][1]) > 1
                if not (x_too_far or y_too_far):
                    continue
                if x_too_far and not y_too_far:
                    dy_i = rope[i - 1][1] - rope[i][1]
                if y_too_far and not x_too_far:
                    dx_i = rope[i - 1][0] - rope[i][0]
                rope[i][0] += dx_i
                rope[i][1] += dy_i
            visited.add((rope[-1][0], rope[-1][1]))
    return len(visited)


class Test9(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO('R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n')
        data = parse_input(input)
        self.assertEqual(part_1(data), 13)

    def test_part_2_example_1(self):
        input = io.StringIO('R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n')
        data = parse_input(input)
        self.assertEqual(part_2(data), 1)

    def test_part_2_example_2(self):
        input = io.StringIO('R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20\n')
        data = parse_input(input)
        self.assertEqual(part_2(data), 36)


if __name__ == '__main__':
    main()
