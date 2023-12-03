
from collections import defaultdict

rows = [list(x) for x in open("3.txt").read().split("\n")]
W = len(rows[0])
H = len(rows)


def is_digit(c):
    return c in set(list('1234567890'))

def is_symbol(c):
    # if it's not a digit or '.', then it's a symbol
    return c != '.' and not is_digit(c)

def has_adjacent_symbol(i, j):
    # Each index can have atmost 8 adjacent index
    if j-1 >= 0 and is_symbol(rows[i][j-1]):
        return rows[i][j-1], (i, j-1), True
    if j-1 >= 0 and i-1 >= 0 and is_symbol(rows[i-1][j-1]):
        return rows[i-1][j-1], (i-1, j-1), True
    if i-1 >= 0 and is_symbol(rows[i-1][j]):
        return rows[i-1][j], (i-1, j), True
    if i-1 >= 0 and j+1 < W and is_symbol(rows[i-1][j+1]):
        return rows[i-1][j+1], (i-1, j+1), True
    if j+1 < W and is_symbol(rows[i][j+1]):
        return rows[i][j+1], (i, j+1), True
    if i+1 < H and j+1 < W and is_symbol(rows[i+1][j+1]):
        return rows[i+1][j+1], (i+1, j+1), True
    if i+1 < H and is_symbol(rows[i+1][j]):
        return rows[i+1][j], (i+1, j), True
    if i+1 < H and j-1 >=0 and is_symbol(rows[i+1][j-1]):
        return rows[i+1][j-1], (i+1, j-1), True
    if i-1 >= 0 and is_symbol(rows[i-1][j]):
        return rows[i-1][j], (i-1, j), True
    
    return None, None, False

# keep building the number, while checking if any sumbol adjacent to each digit
# if found, include the number, else skip it
# create map of symbol + index to num set to which it is associated to

i = 0
res1 = 0
m = defaultdict(set) # {1 : [('*', (1, 2), ('/', (3, 4)))]}
while i < H:
    j = 0
    while j < W:
        if is_digit(rows[i][j]):
            include_num = False
            num = ''
            symbols = set()
            while j < W and is_digit(rows[i][j]):
                num += rows[i][j]
                sym, idx, ok = has_adjacent_symbol(i, j)
                if ok:
                    symbols.add((sym, idx))
                    include_num = True
                j += 1

            if include_num:
                for sym in symbols:
                    m[sym].add(int(num))
                res1 += int(num)
        else: j += 1
    i += 1

print("Part1:", res1)

res2 = 0
for k, v in m.items():
    if k[0] == '*' and len(v) == 2:
        res2 += list(v)[0] * list(v)[1]

print("Part2:", res2)