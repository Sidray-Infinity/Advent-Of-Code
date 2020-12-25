


if __name__ == "__main__":

    data = open("13.txt").read().split('\n')
    arrTime = int(data[0])
    data = data[1].split(',')

    newData = []
    for d in data:
        if d == 'x':
            newData.append('x')
            continue
        if arrTime % int(d) != 0:
            newData.append(int(d) * ((arrTime // int(d)) + 1))
        else:
            newData.append(arrTime)

    minFound = 999999999999999
    idx = -1
    for i in range(len(newData)):
        if newData[i] == 'x':
            continue
        if newData[i] < minFound:
            minFound = newData[i]
            idx = i

    print("Part1:", int(data[idx]) * (minFound - arrTime))

    mods = {int(bus): -i % int(bus) for i, bus in enumerate(data) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]

    # Chinese Remainder theorem
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    
    print("Part2:",val)
    """
    STUPID BRUTE FORCE DOESN'T WORK FOR PART 2

    startTime = None
    count = 1
    while True:
        # print(count)
        check = int(data[0]) * count + 1
        print("CHECK:", check)
        flag = True
        for i in range(1, len(data)):
            if data[i] == 'x':
                check += 1
                continue
            if check % int(data[i]) != 0:
                flag = False
                break
            check += 1
        if flag:
            startTime = int(data[0]) * count
            break
        
        count += 1
    print("Part2:",startTime)
"""
