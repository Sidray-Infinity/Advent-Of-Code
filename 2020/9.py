if __name__ == "__main__":
    data = list(map(int, open("9.txt").read().split('\n')))
    invalidNumber = None
    preambleLength = 25
    for i in range(preambleLength, len(data)):
        preamble = data[i-preambleLength:i]
        flag = True
        for j in range(len(preamble)):
            if data[i] - preamble[j] in set(preamble):
                flag = False
                break
        if flag:
            invalidNumber = data[i]
            print("Part1:", invalidNumber)
            break

    for i in range(len(data)-1):
        res = [data[i],data[i+1]]
        j = i+2
        while sum(res) < invalidNumber and j < len(data):
            res.append(data[j])
            j += 1
        
        if sum(res) == invalidNumber:
            print("Part2:", min(res)+max(res))
            break