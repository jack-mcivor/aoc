from collections import Counter, defaultdict
from pathlib import Path

enable_jokers = True
if enable_jokers:
    cards = 'A K Q T 9 8 7 6 5 4 3 2 J'.split()
else:
    cards = 'A K Q J T 9 8 7 6 5 4 3 2'.split()
_hand_scores = '5 4 3_2 3 2_2 2 1'.split()

lines = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines()
lines = Path("2023/day7.txt").read_text().splitlines()

scores_to_card_ranks_and_bids = [[], [], [], [], [], [], []]

for line in lines:
    hand, bid_ = line.split()
    bid = int(bid_)
    c = Counter(hand)
    if enable_jokers and 'J' in c:
        count_js = c.pop('J')
    else:
        count_js = 0
    counts = c.values()
    # 5Js: high card -> 5 oak
    #       6->0
    # 4Js: high card -> 5 oak
    #       6->0
    # 3Js: high card -> 4 oak, or pair -> 5 oak
    #       6->1, 5->0
    # 2Js: high card -> 3 oak, or pair -> 4 oak, or 3 oak -> 5 oak
    #       6->3, 5->1, 3->0
    # J:   high card -> pair, or pair -> 3 oak, or 3 oak -> 4 oak, or 2 pair -> full house, or 4 oak -> 5 oak
    #       6->5, 5->3, 3->1, 4->2, 1->0
    count_js_to_score_change = {
        5: {6: 0},
        4: {6: 0},
        3: {6:1, 5:0},
        2: {6:3, 5:1, 3:0},
        1: {6:5, 5:3, 3:1, 4:2, 1:0}
    }
    if 5 in counts:
        # 5 of a kind
        score = 0
    elif 4 in counts:
        # 4 of a kind
        score = 1
    elif 3 in counts:
        if 2 in counts:
            # full house
            score = 2
        else:
            # 3 of a kind
            score = 3
    elif 2 in counts:
        if Counter(counts)[2] == 2:
            # two-pair
            score = 4
        else:
            # pair
            score = 5
    else:
        # high card
        score = 6
    if enable_jokers and count_js:
        score = count_js_to_score_change[count_js][score]
    card_ranks = tuple(cards.index(card) for card in hand)
    scores_to_card_ranks_and_bids[score].append((card_ranks, bid))

rank = 0
winnings = 0
# go from weakest to strongest hand
for ranks_bids in scores_to_card_ranks_and_bids[::-1]:
    ranks_bids_sorted = sorted(ranks_bids, key=lambda x: x[0], reverse=True)
    for _r, bid in ranks_bids_sorted:
        rank += 1
        winnings += rank*bid
print(winnings)
