import numpy as np
from collections import defaultdict

def isValid(x, r):
    return x >= r[0] and x <= r[1]

if __name__ == "__main__":
    data = open("16.txt").read().split('\n\n')

    class_data = data[0].split('\n')
    ranges = {}

    for cd in class_data:
        className, rangedata = cd.split(': ')
        r1, r2 = rangedata.split(' or ')
        r11,r12 = map(int, r1.split('-'))
        r21,r22 = map(int, r2.split('-'))
        ranges[className] = ((r11,r12),(r21,r22))

    nearbyTickets = data[2].split('\n')[1:]
    nearbyTickets =np.asarray([list(map(int, line.split(','))) for line in nearbyTickets])

    invalidNumbers = []
    invalidLineNumbers = []

    for i in range(nearbyTickets.shape[0]):
        for j in range(nearbyTickets.shape[1]):
            flag = True
            for c in ranges.keys():
                if isValid(nearbyTickets[i][j], ranges[c][0]) or isValid(nearbyTickets[i][j], ranges[c][1]):              
                    flag = False
                    break
            if flag:
                invalidNumbers.append(nearbyTickets[i][j])
                invalidLineNumbers.append(i)

    print("Part1:", sum(invalidNumbers))

    nearbyTickets = np.delete(nearbyTickets, invalidLineNumbers, axis=0)
    
    fieldPositions = defaultdict(list)

    for c in ranges:
        for j in range(nearbyTickets.shape[1]):
            flag = True
            for i in range(nearbyTickets.shape[0]):   
                if (not isValid(nearbyTickets[i][j], ranges[c][0])) and (not isValid(nearbyTickets[i][j], ranges[c][1])):
                    flag = False
                    break

            if flag:
                fieldPositions[c].append(j)

    fieldPositions = [[x, fieldPositions[x]] for x in fieldPositions]
    
    # PREETY STUPID IDEA, BUT WORKS
    fieldPositions = sorted(fieldPositions, key=lambda x : len(x[1]))

    curr_value = fieldPositions[0][1][0]
    count = 1

    while count < len(ranges):
        for i in range(count, len(fieldPositions)):
            try:
                fieldPositions[i][1].remove(curr_value)
            except ValueError:
                continue
        curr_value = fieldPositions[count][1][0]
        count += 1
    fieldPositions = {x[0]:x[1][0] for x in fieldPositions}
 
    keys = [c for c in ranges if c.split(' ')[0] == "departure"]
    myTicket = list(map(int, data[1].split('\n')[1].split(',')))

    prod = 1
    for k in keys:
        prod *= myTicket[fieldPositions[k]]
    print("Part2:", prod)