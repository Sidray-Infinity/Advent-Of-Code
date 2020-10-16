
if __name__ == "__main__":
    twoCounter = 0
    threeCounter = 0

    data = open("2.txt").read().split('\n')

    for line in data:
        charCounter = {}
        for c in line:
            if charCounter.get(c, None) == None:
                charCounter[c] = 1
            else:
                charCounter[c] += 1 

        for key in charCounter.keys():
            if charCounter[key] == 2:
                twoCounter += 1
                break
        
        for key in charCounter.keys():
            if charCounter[key] == 3:
                threeCounter += 1
                break

    print(twoCounter * threeCounter)

    for i in range(len(data)):
        flag = False
        for j in range(i+1, len(data)):
            diff = 0
            for k in range(len(data[i])):
                if data[i][k] != data[j][k]:
                    diff += 1
            if diff == 1:
                for k in range(len(data[i])):
                    if data[i][k] == data[j][k]:
                        print(data[i][k], end='')
                print()
                flag = True
                break
        if flag:
            break