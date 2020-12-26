
def getNthNumberSpoken(n, data):
    turnCount = 1
    ageTracker = {}
    for d in data:
        if ageTracker.get(d, None) != None:
            if ageTracker[d][1] is None:
                ageTracker[d][1] = turnCount
            else:
                ageTracker[d][0] = ageTracker[d][1]
                ageTracker[d][1] = turnCount
        else:
            ageTracker[d] = [turnCount, None]
        turnCount += 1
    
    lastNum = data[-1]

    while turnCount <= n:
        print(turnCount)
        if ageTracker[lastNum][1] == None:
            lastNum = 0
            if ageTracker.get(0, None) != None:
                if ageTracker[0][1] is None:
                    ageTracker[0][1] = turnCount
                else:
                    ageTracker[0][0] = ageTracker[0][1]
                    ageTracker[0][1] = turnCount
            else:
                ageTracker[0] = [turnCount, None]
        else:
            lastNum = ageTracker[lastNum][1] - ageTracker[lastNum][0]
            if ageTracker.get(lastNum, None) != None:
                if ageTracker[lastNum][1] is None:
                    ageTracker[lastNum][1] = turnCount
                else:
                    ageTracker[lastNum][0] = ageTracker[lastNum][1]
                    ageTracker[lastNum][1] = turnCount
            else:
                ageTracker[lastNum] = [turnCount, None]


        turnCount += 1

    return lastNum

if __name__ == "__main__":
    data = list(map(int, open("15.txt").read().split(',')))
    
    print('Part1:', getNthNumberSpoken(2020, data))
    print('Part2:', getNthNumberSpoken(30000000, data))