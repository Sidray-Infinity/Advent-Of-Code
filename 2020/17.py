import numpy as np
from itertools import product

def isValid(x,y,z,s):
    return x >=0 and x < s[0] and y >=0 and y < s[1] and z >=0 and z < s[2]

if __name__ == "__main__":
    data = [list(x) for x in open("17.txt").read().split('\n')]
    
    ld = len(data)
    fd = ld + 4
    g = np.full((fd*2-1,fd,fd), '.')

    g[fd//2, fd//2 - ld//2: fd//2 + ld//2 + 1, fd//2 - ld//2: fd//2 + ld//2 + 1] = np.asarray(data)
    # print(g)

    ndiff = list(product([0, 1, -1], repeat=3))
    ndiff.remove((0,0,0))

    for _ in range(6):
        for i in range(g.shape[0]):
            for j in range(g.shape[1]):
                for k in range(g.shape[2]):
                    ncount = 0
                    for d in ndiff:
                        if isValid(i+d[0],j+d[1],k+d[2],g.shape) and g[i+d[0],j+d[1],k+d[2]] == '#':
                            ncount += 1

                    if g[i,j,k] == '#' and not (ncount == 2 or ncount == 3):
                        g[i,j,k] = '.'
                    if g[i,j,k] == '.' and ncount == 3:
                        g[i,j,k] = '#'

    active = 0
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            for k in range(g.shape[2]):
                if g[i,j,k] == '#':
                    active += 1
    print(g)
    print(active)