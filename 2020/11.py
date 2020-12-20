import numpy as np
from copy import deepcopy

def isValid(i, j, g):
    return i >= 0 and i < g.shape[0] and j >=0 and j < g.shape[1]

def step(g):
    tg = deepcopy(g)
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            count = 0
            if tg[i][j] == '.':
                continue
            if isValid(i-1,j,g) and tg[i-1][j] == '#':
                count += 1
            if isValid(i-1,j-1,g) and tg[i-1][j-1] == '#':
                count += 1
            if isValid(i,j-1,g) and tg[i][j-1] == '#':
                count += 1
            if isValid(i+1,j-1,g) and tg[i+1][j-1] == '#':
                count += 1
            if isValid(i+1,j,g) and tg[i+1][j] == '#':
                count += 1
            if isValid(i+1,j+1,g) and tg[i+1][j+1] == '#':
                count += 1
            if isValid(i,j+1,g) and tg[i][j+1] == '#':
                count += 1
            if isValid(i-1,j+1,g) and tg[i-1][j+1] == '#':
                count += 1

            if count == 0 and tg[i][j] == 'L':
                g[i][j] = '#'

            if count >= 4 and tg[i][j] == '#':
                g[i][j] = 'L'

def step2(g):
    tg = deepcopy(g)
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            count = 0
            if tg[i][j] == '.':
                continue

            ti = i-1
            while isValid(ti, j, tg):
                if tg[ti][j] == '#':
                    count += 1
                    break
                if tg[ti][j] == 'L':
                    break
                ti -= 1

            ti = i-1
            tj = j-1
            while isValid(ti, tj, tg):
                if tg[ti][tj] == '#':
                    count += 1
                    break
                if tg[ti][tj] == 'L':
                    break
                ti -= 1
                tj -= 1

            tj = j-1
            while isValid(i, tj, tg):
                if tg[i][tj] == '#':
                    count += 1
                    break
                if tg[i][tj] == 'L':
                    break
                tj -= 1

            ti = i+1
            tj = j-1
            while isValid(ti, tj, tg):
                if tg[ti][tj] == '#':
                    count += 1
                    break
                if tg[ti][tj] == 'L':
                    break
                ti += 1
                tj -= 1


            ti = i+1
            while isValid(ti, j, tg):
                if tg[ti][j] == '#':
                    count += 1
                    break
                if tg[ti][j] == 'L':
                    break
                ti += 1

            ti = i+1
            tj = j+1
            while isValid(ti, tj, tg):
                if tg[ti][tj] == '#':
                    count += 1
                    break
                if tg[ti][tj] == 'L':
                    break
                ti += 1
                tj += 1

            tj = j+1
            while isValid(i, tj, tg):
                if tg[i][tj] == '#':
                    count += 1
                    break
                if tg[i][tj] == 'L':
                    break
                tj += 1

            ti = i-1
            tj = j+1
            while isValid(ti, tj, tg):
                if tg[ti][tj] == '#':
                    count += 1
                    break
                if tg[ti][tj] == 'L':
                    break
                ti -= 1
                tj += 1

            if count == 0 and tg[i][j] == 'L':
                g[i][j] = '#'

            if count >= 5 and tg[i][j] == '#':
                g[i][j] = 'L'

if __name__ == "__main__":
    g = open("11.txt").read().split('\n')
    g = np.asarray([list(r) for r in g])
    
    tg = None

    while (tg != g).any():
        tg = deepcopy(g)
        step(g)

    
    countOccupied = 0
    for i in range(tg.shape[0]):
        for j in range(tg.shape[1]):
            if tg[i,j] == '#':
                countOccupied += 1
    print("Part1:", countOccupied)

    g = open("11.txt").read().split('\n')
    g = np.asarray([list(r) for r in g])

    tg = None

    while (tg != g).any():
        tg = deepcopy(g)
        step2(g)

    
    countOccupied = 0
    for i in range(tg.shape[0]):
        for j in range(tg.shape[1]):
            if tg[i,j] == '#':
                countOccupied += 1
    print("Part2:", countOccupied)