rows = open("1.txt").read().split("\n")

digits = set(list("1234567890"))
m = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

res1 = 0
for row in rows:
    chars = list(row)
    first = None
    last = None
    for i, c in enumerate(chars):
        if c in digits:
            if first is None:
                first = c
            last = c

    res1 += int(first + last)

print("Part1:",res1)

res2 = 0
for row in rows:
    first = None
    last = None
    for i in range(len(row)):
        for ds in m.keys():
            if ds == row[i:i+len(ds)]:
                if first is None:
                    first = m[ds]
                last = m[ds]

            if row[i] in digits:
                if first is None:
                    first = row[i]
                last = row[i]
    res2 += int(first + last)

print("Part2:", res2)