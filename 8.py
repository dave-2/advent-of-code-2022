import io
import unittest


def main():
    with open('8.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> list[list[int]]:
    return [[int(tree) for tree in line.rstrip()] for line in file]


def part_1(data: list[list[int]]) -> int:
    return sum(_is_visible(data, x, y)
               for x in range(len(data)) for y in range(len(data[0])))


def _is_visible(tree_patch: list[list[int]], x: int, y: int) -> bool:
    height = tree_patch[x][y]
    x1 = any(tree_patch[x1][y] >= height for x1 in range(x))
    x2 = any(tree_patch[x2][y] >= height for x2 in range(x + 1, len(tree_patch)))
    y1 = any(tree_patch[x][y1] >= height for y1 in range(y))
    y2 = any(tree_patch[x][y2] >= height for y2 in range(y + 1, len(tree_patch[0])))
    return not(x1 and x2 and y1 and y2)


def part_2(data: list[list[int]]) -> int:
    return max(_scenic_score(data, x, y)
               for x in range(len(data)) for y in range(len(data[0])))


def _scenic_score(tree_patch: list[list[int]], x: int, y: int) -> int:
    x1 = _viewing_distance(tree_patch, x, y, -1, 0, x)
    x2 = _viewing_distance(tree_patch, x, y, 1, 0, len(tree_patch) - x - 1)
    y1 = _viewing_distance(tree_patch, x, y, 0, -1, y)
    y2 = _viewing_distance(tree_patch, x, y, 0, 1, len(tree_patch[0]) - y - 1)
    return x1 * x2 * y1 * y2


def _viewing_distance(tree_patch: list[list[int]], x: int, y: int,
                      dx: int, dy: int, length: int) -> int:
    height = tree_patch[x][y]
    viewing_distance = 0
    for _ in range(length):
        viewing_distance += 1
        x += dx
        y += dy
        if tree_patch[x][y] >= height:
            break
    return viewing_distance


_TEST_INPUT = """30373
25512
65332
33549
35390
"""


class Test8(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_1(data), 21)

    def test_part_2(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_2(data), 8)


if __name__ == '__main__':
    main()
