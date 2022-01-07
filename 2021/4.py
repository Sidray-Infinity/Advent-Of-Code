#!/usr/local/bin/python3

import re

def toMatrix(str):
  res = []
  rows = str.split("\n")
  for row in rows:
    res.append(list(map(int, re.split(r'\s+', row.strip()))))
  return res

def checkBingo(board):
  # Check each row
  for row in board:
    if sum(row) == -5:
      return True

  # Check each column
  for i in range(5):
    s = 0
    for row in board:
      s += row[i]
    if s == -5:
      return True
    
  return False

def checkPresentAndMark(board, v):
  for i in range(5):
    for j in range(5):
      if board[i][j] == v: board[i][j] = -1

def getRestSum(board):
  s = 0
  for row in board:
    for r in  row:
      if r > 0: s += r
  return s


data = open("4.txt").read().split("\n\n")

calls = list(map(int, data[0].split(",")))
boards = [toMatrix(board) for board in data[1:]]

bingo = False
for call in calls:
  for board in boards:
    checkPresentAndMark(board, call)
    if checkBingo(board):
      print("part1:", getRestSum(board) * call)
      bingo = True
      break

  if bingo:
    break

lastBoardData = None
boards = [toMatrix(board) for board in data[1:]]

for call in calls:
  for i, board in enumerate(boards):
    converted = False
    if not checkBingo(board):
      checkPresentAndMark(board, call)
      converted = True
    if checkBingo(board) and converted:
      lastBoardData = (board, call)

print("part2:", getRestSum(lastBoardData[0]) * lastBoardData[1])
