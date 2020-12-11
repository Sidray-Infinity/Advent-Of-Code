
from copy import deepcopy


def isInfiniteLoop(insts):
    states = [False] * len(insts)
    index = 0
    accumulator = 0

    while True:
        if index == len(insts):
            break
        if states[index]:
            return False, None

        states[index] = True
        cmnd, value = insts[index].split(' ')
        if cmnd == 'nop':
            index += 1
        elif cmnd == 'acc':
            accumulator += int(value)
            index += 1
        elif cmnd == 'jmp':
            index += int(value)

    return True, accumulator

if __name__ == "__main__":
    insts = open("8.txt").read().split('\n')
    states = [False] * len(insts)

    index = 0
    accumulator = 0

    while index < len(insts) and not states[index]:
        states[index] = True
        cmnd, value = insts[index].split(' ')
        if cmnd == 'nop':
            index += 1
        elif cmnd == 'acc':
            accumulator += int(value)
            index += 1
        elif cmnd == 'jmp':
            index += int(value)

    print('Part1:', accumulator)

    for i in range(len(insts)):
        cmnd, value = insts[i].split(' ')
        if cmnd == 'acc':
            continue
        instsCopy = deepcopy(insts)
        if cmnd == 'nop':
            instsCopy[i] = ' '.join(['jmp', value])
        else:
            instsCopy[i] = ' '.join(['nop', value])
        isNotInfinite, acc = isInfiniteLoop(instsCopy)
        if isNotInfinite:
            print("Part2:", acc)
            break
