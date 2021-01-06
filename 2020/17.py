import numpy as np
import sys
from copy import deepcopy
from itertools import product

np.set_printoptions(threshold=sys.maxsize)

def isValid(x,y,z,s):
    return x >=0 and x < s[0] and y >=0 and y < s[1] and z >=0 and z < s[2]

def isValid2(x,y,z,t,s):
    return x >=0 and x < s[0] and y >=0 and y < s[1] and z >=0 and z < s[2] and t >= 0 and t < s[3]

if __name__ == "__main__":
    data = [list(x) for x in open("17.txt").read().split('\n')]
    num_steps = 6
    ld = len(data)
    fd = ld + num_steps * 2

    # ALLOCATE THE MAXIMUM POSSIBLE SPACE BEFOREHAND
    g = np.full((2 * num_steps + 1, fd, fd), '.')
    
    g[(2 * num_steps + 1)//2, num_steps: num_steps + ld, num_steps: num_steps + ld] = np.asarray(data)

    ndiff = list(product([0, 1, -1], repeat=3))
    ndiff.remove((0,0,0))

    for _ in range(num_steps):
        tg = deepcopy(g)
        for i in range(g.shape[0]):
            for j in range(g.shape[1]):
                for k in range(g.shape[2]):
                    ncount = 0
                    for d in ndiff:
                        if isValid(i+d[0],j+d[1],k+d[2],g.shape) and g[i+d[0],j+d[1],k+d[2]] == '#':
                            ncount += 1

                    if g[i,j,k] == '#' and ncount != 2 and ncount != 3:
                        tg[i,j,k] = '.'
                    if g[i,j,k] == '.' and ncount == 3:
                        tg[i,j,k] = '#'
        g = tg
  
    active = 0
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            for k in range(g.shape[2]):
                if g[i,j,k] == '#':
                    active += 1

    print("Part1:", active)

    # ALLOCATE THE MAXIMUM POSSIBLE SPACE BEFOREHAND
    w = 2 * num_steps + 1
    g = np.full((w, w*w, fd, fd), '.')
    
    g[w//2, w//2, num_steps: num_steps + ld, num_steps: num_steps + ld] = np.asarray(data)
    print(g.shape)
    

    ndiff = list(product([0, 1, -1], repeat=4))
    ndiff.remove((0,0,0,0))
    print(len(ndiff))

    for step in range(num_steps):
        print(step)
        tg = deepcopy(g)
        for i in range(g.shape[0]):
            for j in range(g.shape[1]):
                for k in range(g.shape[2]):
                    for t in range(g.shape[3]):
                        ncount = 0
                        for d in ndiff:
                            if isValid2(i+d[0],j+d[1],k+d[2],t+d[3],g.shape) and g[i+d[0],j+d[1],k+d[2],t+d[3]] == '#':
                                ncount += 1

                        if g[i,j,k,t] == '#' and ncount != 2 and ncount != 3:
                            tg[i,j,k,t] = '.'
                        if g[i,j,k,t] == '.' and ncount == 3:
                            tg[i,j,k,t] = '#'
        g = tg
  
    active = 0
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            for k in range(g.shape[2]):
                for t in range(g.shape[3]):
                    if g[i,j,k,t] == '#':
                        active += 1

    print("Part2:", active)