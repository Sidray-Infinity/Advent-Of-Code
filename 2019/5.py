import copy


def intcode_new(seq):
    """
    modes -> 0(position mode: parameter as address),
             1(immediate mode: parameter as value)

    opcode -> 1(add &+1 & &+2, store in &+3),
              2(mult &+1 & &+2, store in &+3),
              3(stores input @ +1),
              4(outputs value @ +1),
              99(finished, halt)

    Instructions : 5 digits (put 0 if less)

    """
    i = 0

    while i < len(seq):

        inst = list(str(seq[i]))

        while len(inst) != 4:
            inst.insert(0, '0')
        # print(inst)
        # input()
        op_code = ''.join(inst[-2:])
        mode_1 = inst[1]
        mode_2 = inst[0]

        if op_code == "99":
            break

        if op_code == '01':
            if mode_1 == '0':
                a = seq[seq[i+1]]     # Para1 in adress mode
            elif mode_1 == '1':
                a = seq[i+1]          # Para1 in immediate mode

            if mode_2 == '0':
                b = seq[seq[i+2]]     # Para2 in adress mode
            elif mode_2 == '1':
                b = seq[i+2]          # Para2 in immediate mode

            seq[seq[i+3]] = a + b
            i += 4

        if op_code == '02':
            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            if mode_2 == '0':
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]

            seq[seq[i+3]] = a * b
            i += 4

        if op_code == '03':
            x = int(input("Enter input: "))
            seq[seq[i+1]] = x

            i += 2

        if op_code == '04':
            if mode_1 == '0':
                print(seq[seq[i+1]])
            elif mode_1 == '1':
                print(seq[i+1])
            i += 2

        if op_code == '05':

            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            if a != 0:
                if mode_2 == '0':
                    b = seq[seq[i+2]]
                elif mode_2 == '1':
                    b = seq[i+2]
                i = b
            else:
                i += 3

        if op_code == '06':
            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            if a == 0:
                if mode_2 == '0':
                    b = seq[seq[i+2]]
                elif mode_2 == '1':
                    b = seq[i+2]
                i = b
            else:
                i += 3
        if op_code == '07':
            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            if mode_2 == '0':
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]

            if a < b:
                seq[seq[i+3]] = 1
            else:
                seq[seq[i+3]] = 0
            i += 4

        if op_code == '08':
            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            if mode_2 == '0':
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]

            if a == b:
                seq[seq[i+3]] = 1
            else:
                seq[seq[i+3]] = 0
            i += 4


if __name__ == "__main__":
    seq = list(map(int, open("5.txt", "r").read().split(',')))
    seq2 = copy.copy(seq)
    # Part 1
    intcode_new(seq)

    # Part 2
    intcode_new(seq2)
