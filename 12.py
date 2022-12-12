import collections
import io
import unittest


Point = tuple[int, int]


def main():
    with open('12.input') as file:
        heightmap, start, end = parse_input(file)
    print('Part One:', part_1(heightmap, start, end))
    print('Part Two:', part_2(heightmap, end))


def parse_input(file: io.TextIOBase) -> tuple[list[list[int]], Point, Point]:
    heightmap: list[list[int]] = []
    start = None
    end = None

    for y, line in enumerate(file):
        heightmap.append([])
        for x, char in enumerate(line.rstrip()):
            heightmap[y].append(
                0 if char == 'S' else 25 if char == 'E' else ord(char) - 97)
            if char == 'S': start = x, y
            if char == 'E': end = x, y

    if not start:
        raise ValueError('Heightmap has no (S)tart location')
    if not end:
        raise ValueError('Heightmap has no (E)nd location')

    return heightmap, start, end


def part_1(heightmap: list[list[int]], start: Point, end: Point) -> int:
    visited: set[Point] = set([start])
    search_queue = collections.deque([[start]])

    def _add_point(path: list[Point], point: Point, max_height: int) -> None:
        x, y = point
        if x < 0 or x >= len(heightmap[0]): return
        if y < 0 or y >= len(heightmap): return
        if heightmap[y][x] > max_height: return
        if point in visited: return
        visited.add(point)
        search_queue.append([*path, point])

    while search_queue:
        path = search_queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return len(path) - 1

        max_height = heightmap[y][x] + 1
        _add_point(path, (x - 1, y), max_height)
        _add_point(path, (x + 1, y), max_height)
        _add_point(path, (x, y - 1), max_height)
        _add_point(path, (x, y + 1), max_height)

    raise ValueError('No path found from Start to End.')


def part_2(heightmap: list[list[int]], end: Point) -> int:
    visited: set[Point] = set([end])
    search_queue = collections.deque([[end]])

    def _add_point(path: list[Point], point: Point, min_height: int) -> None:
        x, y = point
        if x < 0 or x >= len(heightmap[0]): return
        if y < 0 or y >= len(heightmap): return
        if heightmap[y][x] < min_height: return
        if point in visited: return
        visited.add(point)
        search_queue.append([*path, point])

    while search_queue:
        path = search_queue.popleft()
        x, y = path[-1]
        if heightmap[y][x] == 0:
            return len(path) - 1

        min_height = heightmap[y][x] - 1
        _add_point(path, (x - 1, y), min_height)
        _add_point(path, (x + 1, y), min_height)
        _add_point(path, (x, y - 1), min_height)
        _add_point(path, (x, y + 1), min_height)

    raise ValueError('No path found from End to "a".')


_TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


class Test12(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        heightmap, start, end = parse_input(input)
        self.assertEqual(part_1(heightmap, start, end), 31)

    def test_part_2(self):
        input = io.StringIO(_TEST_INPUT)
        heightmap, _, end = parse_input(input)
        self.assertEqual(part_2(heightmap, end), 29)


if __name__ == '__main__':
    main()
