from pathlib import Path

cards = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines()
cards = Path("2023/day4.txt").read_text().splitlines()

# part 1
ret = 0
for card in cards:
    details = card.split(": ", maxsplit=1)[1]
    winning_s, have_s = details.split(" | ")
    winning = frozenset(int(n) for n in winning_s.split())
    have = tuple(int(n) for n in have_s.split())
    won = tuple(n in winning for n in have)
    n_won = sum(won)
    points = 0
    if n_won:
        points = 1
    for _ in range(n_won - 1):
        points *= 2
    ret += points

print(ret)

# part 2
import numpy as np

copies = np.ones(len(cards), dtype=np.int_)

for i, card in enumerate(cards):
    card_num_, details = card.split(": ", maxsplit=1)
    card_num = int(card_num_.split()[-1].strip())
    winning_s, have_s = details.split(" | ")
    winning = frozenset(int(n) for n in winning_s.split())
    have = tuple(int(n) for n in have_s.split())
    won = tuple(n in winning for n in have)
    n_won = sum(won)
    copies[i + 1 : i + n_won + 1] += copies[i]

print(copies.sum())
