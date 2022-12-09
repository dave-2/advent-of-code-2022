import functools
import io
from typing import Callable, TypeVar, Union
import unittest


Directory = dict[str, Union['Directory', int]]


def main():
    with open('7.input') as file:
        data = parse_input(file)
    print('Part One:', part_1(data))
    print('Part Two:', part_2(data))


def parse_input(file: io.TextIOBase) -> Directory:
    filesystem: Directory = {'/': {}}
    working_dir_list = ['/']

    for line in file:
        if line.startswith('$ cd '):
            dir_name = line[5:-1]
            if dir_name == '/':
                working_dir_list = ['/']
            elif dir_name == '..':
                working_dir_list.pop()
            else:
                working_dir_list.append(dir_name)
            continue

        if line == '$ ls\n':
            continue

        working_dir = _find_directory(filesystem, working_dir_list)

        if line.startswith('dir '):
            dir_name = line[4:-1]
            working_dir[dir_name] = {}
            continue

        size, name = line[:-1].split(' ')
        working_dir[name] = int(size)

    return filesystem


def _find_directory(filesystem: Directory, dir_list: list[str]) -> Directory:
    current_dir: Directory = filesystem
    for dir_name in dir_list:
        next_dir = current_dir[dir_name]
        if isinstance(next_dir, int):
            raise ValueError(f'Tried to enter a file: "{dir_name}"')
        current_dir = next_dir
    return current_dir


def part_1(data: Directory) -> int:
    return treeduce(_sum_directories_under_100000, data)[0]


def _sum_directories_under_100000(
        accum: list[tuple[int, int]], file_sizes: int) -> tuple[int, int]:
    total = sum(subtotal for subtotal, _ in accum)
    dir_size = sum(subdir_size for _, subdir_size in accum) + file_sizes
    if dir_size <= 100000:
        total += dir_size
    return total, dir_size


def part_2(data: Directory) -> int:
    minimum_size = treeduce(_dir_size, data) - 40000000
    minimum_dir_func = functools.partial(_minimum_dir_over_size, minimum_size)
    return treeduce(minimum_dir_func, data)[0]


def _dir_size(subdir_sizes: list[int], file_sizes: int) -> int:
    return sum(subdir_sizes) + file_sizes


def _minimum_dir_over_size(minimum_size: int, accum: list[tuple[int, int]],
                           file_sizes: int) -> tuple[int, int]:
    dir_size = sum(subdir_size for _, subdir_size in accum) + file_sizes
    min_dir = min(
        (min_subdir for min_subdir, _ in accum if min_subdir >= minimum_size),
        default=None) or dir_size
    return min_dir, dir_size


T = TypeVar('T')
def treeduce(function: Callable[[list[T], int], T], dir: Directory) -> T:
    accumulator: list[T] = []
    file_sizes = 0
    for dir_or_file in dir.values():
        if isinstance(dir_or_file, int):
            file_sizes += dir_or_file
            continue
        accumulator.append(treeduce(function, dir_or_file))
    return function(accumulator, file_sizes)


_TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Test7(unittest.TestCase):

    def test_part_1(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_1(data), 95437)

    def test_part_2(self):
        input = io.StringIO(_TEST_INPUT)
        data = parse_input(input)
        self.assertEqual(part_2(data), 24933642)


if __name__ == '__main__':
    main()
