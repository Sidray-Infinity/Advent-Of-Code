def intcode_new(seq):
    """
    Instructions : 5 digits (put 0 if less)

    # Dynamic expansion included

    """
    i = 0
    phase_ip = True
    rel_base = 0

    while i < len(seq):
        inst = list(str(seq[i]))

        while len(inst) != 5:
            inst.insert(0, '0')

        op_code = ''.join(inst[-2:])
        mode_1 = inst[2]
        mode_2 = inst[1]
        mode_3 = inst[0]

        if op_code == "99":
            break

        if op_code == '01':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if mode_2 == '0':
                if (seq[i+2]) > len(seq)-1:
                    while len(seq) < seq[i+2]:
                        seq.append(0)
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]
            elif mode_2 == '2':
                if (rel_base + seq[i+2]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+2]):
                        seq.append(0)
                b = seq[rel_base + seq[i+2]]

            if mode_3 == '0':
                if (seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < seq[i+3]:
                        seq.append(0)
                #print(len(seq), seq[i+3])
                seq[seq[i+3]] = a + b
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+3]):
                        seq.append(0)
                seq[rel_base + seq[i+3]] = a + b

            i += 4

        if op_code == '02':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if mode_2 == '0':
                if (seq[i+2]) > len(seq)-1:
                    while len(seq) < seq[i+2]:
                        seq.append(0)
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]
            elif mode_2 == '2':
                if (rel_base + seq[i+2]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+2]):
                        seq.append(0)
                b = seq[rel_base + seq[i+2]]

            if mode_3 == '0':
                if (seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < seq[i+3]:
                        seq.append(0)
                seq[seq[i+3]] = a * b
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+3]):
                        seq.append(0)
                seq[rel_base + seq[i+3]] = a * b

            i += 4

        if op_code == '03':
            x = int(input("Enter input: "))

            if mode_1 == "1":
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        print("Test")
                        seq.append(0)

                seq[seq[i+1]] = x
            elif mode_1 == "2":
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                seq[rel_base + seq[i+1]] = x

            i += 2

        if op_code == '04':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            i += 2
            print("------------------------------\n", a, "\n----------------")
            # return a

        if op_code == '05':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if a != 0:

                if mode_2 == '0':
                    if (seq[i+2]) > len(seq)-1:
                        while len(seq) < seq[i+2]:
                            seq.append(0)
                    b = seq[seq[i+2]]
                elif mode_2 == '1':
                    b = seq[i+2]
                elif mode_2 == '2':
                    if (rel_base + seq[i+2]) > len(seq)-1:
                        while len(seq)-1 < (rel_base + seq[i+2]):
                            seq.append(0)
                        #print(len(seq), rel_base + seq[i+2])
                    b = seq[rel_base + seq[i+2]]

                i = b
            else:
                i += 3

        if op_code == '06':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if a == 0:
                if mode_2 == '0':
                    if (seq[i+2]) > len(seq)-1:
                        while len(seq) < seq[i+2]:
                            seq.append(0)
                    b = seq[seq[i+2]]
                elif mode_2 == '1':
                    b = seq[i+2]
                elif mode_2 == '2':
                    if (rel_base + seq[i+2]) > len(seq)-1:
                        while len(seq) < (rel_base + seq[i+2]):
                            seq.append(0)
                    b = seq[rel_base + seq[i+2]]
                i = b
            else:
                i += 3

        if op_code == '07':
            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if mode_2 == '0':
                if (seq[i+2]) > len(seq)-1:
                    while len(seq) < seq[i+2]:
                        seq.append(0)
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]
            elif mode_2 == '2':
                if (rel_base + seq[i+2]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+2]):
                        seq.append(0)
                b = seq[rel_base + seq[i+2]]

            if mode_3 == '0':
                if (seq[i+3]) > len(seq)-1:
                    while len(seq) < seq[i+3]:
                        seq.append(0)
                if a < b:
                    seq[seq[i+3]] = 1
                else:
                    seq[seq[i+3]] = 0
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq) < (rel_base + seq[i+3]):
                        seq.append(0)
                if a < b:
                    seq[rel_base + seq[i+3]] = 1
                else:
                    seq[rel_base + seq[i+3]] = 0
            i += 4

        if op_code == '08':
            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 != (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if mode_2 == '0':
                if (seq[i+2]) > len(seq)-1:
                    while len(seq)-1 < seq[i+2]:
                        seq.append(0)
                b = seq[seq[i+2]]
            elif mode_2 == '1':
                b = seq[i+2]
            elif mode_2 == '2':
                if (rel_base + seq[i+2]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+2]):
                        seq.append(0)
                b = seq[rel_base + seq[i+2]]

            if mode_3 == '0':
                if (seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < seq[i+3]:
                        seq.append(0)
                if a == b:
                    seq[seq[i+3]] = 1
                else:
                    seq[seq[i+3]] = 0
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+3]):
                        seq.append(0)
                if a == b:
                    seq[rel_base + seq[i+3]] = 1
                else:
                    seq[rel_base + seq[i+3]] = 0
            i += 4

        if op_code == '09':
            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq) < seq[i+1]:
                        seq.append(0)
                rel_base += seq[seq[i+1]]
            if mode_1 == '1':
                rel_base += seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
                        seq.append(0)

                rel_base += seq[rel_base + seq[i+1]]
            i += 2


if __name__ == "__main__":

    seq = list(map(int, open("9.txt", "r").read().split(",")))

    # Part 1 and Part 2

    intcode_new(seq)
