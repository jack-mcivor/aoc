from copy import copy
from pathlib import Path

lines = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()
lines = Path("2023/day3.txt").read_text().splitlines()
adj_sums = 0
gear_ratios = 0

X = int
Y = int
symbols: list[tuple[X, Y]] = []
gears: list[tuple[X, Y]] = []
number_map: dict[tuple[X, Y], int] = {}
codes: list[list[str]] = []
number_idx = -1
for y, line in enumerate(lines):
    in_num = False
    for x, char in enumerate(line):
        if char.isdigit():
            if not in_num:
                number_idx += 1
                codes.append([])
                in_num = True
            codes[number_idx].append(char)
            number_map[(x, y)] = number_idx
        elif char != ".":
            symbols.append((x, y))
            if char == "*":
                gears.append((x, y))
            in_num = False
        else:
            in_num = False

numbers: list[int] = []
for code in codes:
    numbers.append(int("".join(code)))

numbers_for_adjacency = copy(numbers)
for x, y in symbols:
    for lookup_x, lookup_y in (
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ):
        idx = number_map.get((lookup_x, lookup_y))
        if idx is not None:
            adj_sums += numbers_for_adjacency[idx]
            # ensure we don't double count by zeroing it out
            numbers_for_adjacency[idx] = 0
print(adj_sums)

for x, y in gears:
    gear_idx_nums = set()
    for lookup_x, lookup_y in (
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ):
        idx = number_map.get((lookup_x, lookup_y))
        if idx is not None:
            # ensure we don't double count by storing only unique number indices
            gear_idx_nums.add(idx)

    if len(gear_idx_nums) == 2:
        gear_0_idx, gear_1_idx = tuple(gear_idx_nums)
        gear_ratios += numbers[gear_0_idx] * numbers[gear_1_idx]

print(gear_ratios)
