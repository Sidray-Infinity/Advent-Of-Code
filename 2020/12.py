
from os import truncate


def turn(currDirec, x):
    direcMapper = {'E': 0, 'N': 90, 'W': 180, 'S': 270}
    direcMapperComp = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

    return direcMapperComp[(direcMapper[currDirec] + x) % 360]

def move(direc, value, x, y):
    if direc == 'N':
        y += value
    elif direc == 'S':
        y -= value
    elif direc == 'E':
        x += value
    elif direc == 'W':
        x -= value
    return x, y

def move2(dx, dy, direc, value, x, y):
    if direc == 'W':
        if dx == 'W':
            x += value
        else:
            x -= value
    if direc == 'E':
        if dx == 'E':
            x += value
        else:
            x -= value
    if direc == 'N':
        if dy == 'N':
            y += value
        else:
            y -= value
    if direc == 'S':
        if dy == 'S':
            y += value
        else:
            y -= value

    return x, y

def comp(x):
    return {'E':'W', 'W':'E', 'N':'S', 'S':'N'}[x]

def swap(x, y):
    t = x
    x = y
    y = t
    return x, y

if __name__ == "__main__":
    data = open("12.txt").read().split('\n')
    x = 0
    y = 0
    currDirec = 'E'

    for d in data:
        cmnd, value = d[0], int(d[1:])
        if d[0] == 'L':
            currDirec = turn(currDirec, value)
        elif d[0] == 'R':
            currDirec = turn(currDirec, -value)
        elif d[0] == 'F':
            x, y = move(currDirec, value, x, y)
        else:
            x, y = move(cmnd, value, x, y)

    print("Part1:", abs(x)+abs(y))

    x = 0
    y = 0
    xw = 10
    yw = 1
    dx = 'E'
    dy = 'N'

    for d in data:
        cmnd, value = d[0], int(d[1:])
        if d[0] == 'L':
            dx = turn(dx, value)
            dy = turn(dy, value)
            if value in [90, 270]:
                dx, dy = swap(dx, dy)
                xw, yw = swap(xw, yw)
        elif d[0] == 'R':
            dx = turn(dx, -value)
            dy = turn(dy, -value)
            if value in [90, 270]:
                dx, dy = swap(dx, dy)
                xw, yw = swap(xw, yw)
        elif d[0] == 'F':
            x, y = move(dx, value*abs(xw), x, y)
            x, y = move(dy, value*abs(yw), x, y)
        else:
            xw, yw = move2(dx, dy, cmnd, value, xw, yw)
            if xw < 0:
                xw = abs(xw)
                dx = comp(dx)
            if yw < 0:
                yw = abs(yw)
                dy = comp(dy)

    print("Part2:", abs(x)+abs(y))

        
