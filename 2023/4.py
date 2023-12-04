from collections import defaultdict

rows = open("4.txt").read().splitlines()

num_cards = [1] * len(rows)

res1 = 0
res2 = 0
for i in range(len(rows)):
    card_info = rows[i].split(": ")
    num_info = card_info[1].split(" | ")
    winiing_num = set([int(x) for x in num_info[0].split(" ") if x != ''])
    got_num = set([int(x) for x in num_info[1].split(" ") if x != ''])
    our_win_num = got_num.intersection(winiing_num)
    if len(our_win_num) > 0:
        res1 += 2 ** (len(our_win_num) - 1)
    j = i+1
    while j < len(rows) and j <= i + len(our_win_num):
        num_cards[j] += num_cards[i]
        j += 1

print("Part1:", res1)
print("Part2:", sum(num_cards))