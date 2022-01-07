#!/usr/local/bin/python3
import copy

def comp(x):
  if x == '1':
    return '0'
  return '1'

def getMostCommon(data):
  mostCommon = {}
  for i in range(len(data[0])):
    z, o = 0, 0
    for line in data:
      if line[i] == '0': z += 1
      else: o += 1
    if o >= z:
      mostCommon[i] = '1'
    else:
      mostCommon[i] = '0'

  return mostCommon

data = open("3.txt").read().split("\n")

e, g = "", ""
mostCommon = getMostCommon(data)
for i in range(len(data[0])):
  g += mostCommon[i]
  e += comp(mostCommon[i])

print("part1:", int(g, 2) * int(e, 2))

o = copy.copy(data)
c = copy.copy(data)
for i in range(len(data[0])):
  if len(o) > 1:
    mostCommon = getMostCommon(o)
    o = [x for x in o if x[i] == mostCommon[i]]

  if len(c) > 1:
    mostCommon = getMostCommon(c)
    c = [x for x in c if x[i] == comp(mostCommon[i])]

print("part2:", int(o[0], 2) * int(c[0], 2))


