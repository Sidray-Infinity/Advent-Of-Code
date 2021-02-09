

data = list(map(int, list(open("1.txt").read()[:-1])))
sum = 0
n = len(data)
for i in range(1, n):
    if data[i] == data[i-1]:
        sum += data[i]

if data[0] == data[-1]:
    sum += data[0]

print("Part1:", sum)

sum = 0
for i in range(len(data)):
    if data[i] == data[(i+n//2)%n]:
        sum += data[i]

print("Part2:", sum)