import copy


def intcode(seq):
    """
    opcode -> 1(add &+1 & &+2, store in &+3),
              2(mult &+1 & &+2, store in &+3),
              99(finished, halt)
    """
    i = 0

    while i < len(seq):
        if seq[i] == 99:
            break
        elif seq[i] == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
            i += 4
        elif seq[i] == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
            i += 4
        else:
            print("Invalid Operand")
            return None

    return seq


if __name__ == "__main__":

    # Part 1

    f = open("2.txt", "r")
    seq = [int(x) for x in f.read().split(',')]
    # Add the 1202 error
    seq[1] = 12
    seq[2] = 2

    seq = intcode(seq)
    print(seq[0])

    # Part 2

    f.seek(0)
    seq = [int(x) for x in f.read().split(',')]
    temp = copy.copy(seq)

    # Give input @ &1 & &2 ; (0, 99)
    for i in range(100):
        for j in range(100):
            seq = copy.copy(temp)
            seq[1], seq[2] = i, j
            print(i, j)
            seq = intcode(seq)
            if seq[0] == 19690720:
                print(100 * i + j)
                exit()
