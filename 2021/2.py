commands = []
data = open("2.txt").read().split("\n")
for line in data:
  key, val = line.split(" ")
  commands.append((key, int(val)))

x, y = 0, 0
for c, v in commands:
  if c == "forward":
    x += v
  if c == "up":
    y -= v
  if c == "down":
    y += v

print("part1:", x*y)

x, y, a = 0, 0, 0
for c, v in commands:
  if c == "forward":
    x += v
    y += a*v
  if c == "up":
    a -= v
  if c == "down":
    a += v

print("part2:", x*y)