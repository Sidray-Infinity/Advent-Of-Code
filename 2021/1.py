
data = list(map(int, open("1.txt").read().split("\n")))
count = 0

for i in range(1, len(data)):
  if data[i] > data[i-1]:
    count += 1

print("part1:", count)

prevWindow = sum(data[:3])
count = 0

for i in range(3, len(data)):
  if (prevWindow - data[i-3] + data[i]) > prevWindow:
    count += 1
  prevWindow = prevWindow - data[i-3] + data[i]


print("part2:", count)