

if __name__ == "__main__":
    data = list(map(int, open("15.txt").read().split(',')))
    ageTracker = {}

    for d in data:
        for k in ageTracker.keys():
            ageTracker[k][0] += 1
        ageTracker[d] = [1, False]
        

    print(ageTracker)

    numCount = 3
    lastNum = data[-1]

    while numCount != 2020:

        if ageTracker.get(lastNum, None) != None:
            if ageTracker[lastNum][1] == False:
                ageTracker[0][1] = True
                ageTracker[0][0] = 0
                lastNum = 0
            else:
                t = lastNum
                lastNum = numCount - 1 - ageTracker[lastNum][0]
                ageTracker[t][0] = 0
        else:
            ageTracker[lastNum] = [0, False]

        for k in ageTracker.keys():
            ageTracker[k][0] += 1
        print(numCount, lastNum)
        numCount += 1
        

    print("Part1:", lastNum)