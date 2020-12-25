import itertools

def toBinary(x):
    return bin(int(x)).replace("0b", "").rjust(36, '0')

def applyMask(mask, x):
    if mask is None:
        return x

    mask = list(mask)
    num = list(toBinary(x))

    for i in range(len(mask)):
        if mask[i] != 'X':
            num[i] = mask[i]

    return int(''.join(num), 2)

def xIndices(addrs):
    res = []
    for i in range(len(addrs)):
        if addrs[i] == 'X':
            res.append(i)

    return res
    
def applyMaskToMem(mask, adrs):
    if mask is None:
        return [adrs]

    mask = list(mask)
    addrs = list(toBinary(adrs))

    for i in range(len(mask)):
        if mask[i] != '0':
            addrs[i] = mask[i]

    res = []
    x_indices = xIndices(addrs)
    combs = list(itertools.product([0, 1], repeat=len(x_indices)))
    for c in combs:
        count = 0
        for i in x_indices:
            addrs[i] = str(c[count])
            count += 1
        res.append(int(''.join(addrs), 2))
    return res

if __name__ == "__main__":
    data = open("14.txt").read().split('\n')

    currMask = None
    mem = {}

    for d in data:
        cmnd, value = d.split(" = ")
        if cmnd == "mask":
            currMask = value
        else:
            index = int(cmnd.split('[')[1].split(']')[0])
            mem[index] = applyMask(currMask, int(value))

    print("Part1:", sum(mem.values()))

    currMask = None
    mem = {}

    for j, d in enumerate(data):
        cmnd, value = d.split(" = ")
        if cmnd == "mask":
            currMask = value
        else:
            index = int(cmnd.split('[')[1].split(']')[0])
            addresses = applyMaskToMem(currMask, index)
            for a in addresses:
                mem[a] = int(value)

    print("Part2:", sum(mem.values()))