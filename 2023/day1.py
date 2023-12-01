from pathlib import Path

lines = Path("2023/day1.txt").read_text().splitlines()
val_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
val = 0


def spelled_out_val(chars):
    for sub, v in val_map.items():
        if line[i:].startswith(sub):
            return v


for line in lines:
    first_val = True
    for i, char in enumerate(line):
        if char.isdigit():
            d = int(char)
        elif v := spelled_out_val(line[i:]):
            d = v
        else:
            continue
        if first_val:
            val += d * 10
            first_val = False
    val += d  # this is the last value

print(val)
