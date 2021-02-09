

data = [list(map(int, d.split('\t'))) for d in open("2.txt").read().split('\n')]

sum = 0
for row in data:
    sum += max(row) - min(row)

print("Part1:", sum)

sum = 0
for row in data:
    for i in range(len(row)):
        flag = False
        for j in range(i+1, len(row)):
            t = row[i] / row[j]
            if t.is_integer():
                sum += t
                flag = True
            t = row[j] / row[i]
            if t.is_integer():
                sum += t
                flag = True
            if flag:
                break

print("Part2:", sum)
            