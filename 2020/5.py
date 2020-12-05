
def computeSeatNumber(x):
    l = 0
    r = 127
    for i in range(7):
        mid = (l+r)//2
        if x[i] == 'F':
            r = mid
        else:
            l = mid + 1
    row = l
    l = 0
    r = 7
    for i in range(7, 10):
        mid = (l+r)//2
        if x[i] == 'L':
            r = mid
        else:
            l = mid + 1
    col = l
    return row * 8 + col

if __name__ == "__main__":

    data = open("5.txt").read().split('\n')
    maxSeat = -1
    for d in data:
        maxSeat = max(maxSeat, computeSeatNumber(d))
    print("Part1:", maxSeat)

    s = set()
    for d in data:
        s.add(computeSeatNumber(d))
    vacants = list(set(range(128*8)) - s)
    for i in range(1, len(vacants)):
        if vacants[i] - vacants[i-1] != 1:
            print("Part2:", vacants[i])
            break