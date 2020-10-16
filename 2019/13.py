import time
import numpy as np


def intcode_new(seq, grid, rb, bp, pp, init=0,):
    """
    Instructions : 5 digits (put 0 if less)

    # Dynamic expansion included

    """
    i = init
    phase_ip = True
    rel_base = rb
    op = []

    while i < len(seq):
        inst = list(str(seq[i]))
        while len(inst) != 5:
            inst.insert(0, '0')

        op_code = ''.join(inst[-2:])
        mode_1 = inst[2]
        mode_2 = inst[1]
        mode_3 = inst[0]

        if op_code == "99":
            print("HALT!")
            return [-1, -1, -1], -1, -1, seq

        if op_code == '01':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
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
                # print(len(seq), seq[i+3])
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
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)

                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
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
                seq[seq[i+3]] = a * b
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+3]):
                        seq.append(0)
                seq[rel_base + seq[i+3]] = a * b

            i += 4

        if op_code == '03':

            for g in grid:
                print(''.join(g))
            time.sleep(0.0000000001)

            if bp > pp:
                a = 1
            elif bp < pp:
                a = -1
            else:
                a = 0
            x = a

            if mode_1 == "0":
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        print("Test")
                        seq.append(0)
                seq[seq[i+1]] = x
            elif mode_1 == "2":
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
                        seq.append(0)
                seq[rel_base + seq[i+1]] = x

            i += 2

        if op_code == '04':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            i += 2

            op.append(a)
            if len(op) == 3:

                return op, rel_base, i, seq

        if op_code == '05':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if a != 0:

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
                        # print(len(seq), rel_base + seq[i+2])
                    b = seq[rel_base + seq[i+2]]

                i = b
            else:
                i += 3

        if op_code == '06':

            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
                        seq.append(0)
                a = seq[rel_base + seq[i+1]]

            if a == 0:
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
                i = b
            else:
                i += 3

        if op_code == '07':
            if mode_1 == '0':
                if (seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < seq[i+1]:
                        seq.append(0)
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]
            elif mode_1 == '2':
                if (rel_base + seq[i+1]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+1]):
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
                if a < b:
                    seq[seq[i+3]] = 1
                else:
                    seq[seq[i+3]] = 0
            elif mode_3 == '2':
                if (rel_base + seq[i+3]) > len(seq)-1:
                    while len(seq)-1 < (rel_base + seq[i+3]):
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
                    while len(seq)-1 < seq[i+1]:
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


def draw_tiles(seq):

    tiles = []
    i = 0
    rel_base = 0

    while True:
        op, rel_base, i, seq = intcode_new(seq, 0, rel_base, 0, 0, i)
        if rel_base == -1 and i == -1:
            break
        tiles.append(op)

    count = 0
    for t in tiles:
        if t[2] == 2:
            count += 1

    print("NUM BLOCK TILES:", count)
    input("Press enter to play")


def play(seq):
    """
    0 -> neutral, -1 -> left, 1 -> right
    """

    tiles = []
    i = 0
    rel_base = 0
    curr_score = 0
    ip = 0
    pp = 20
    bp = 2

    mapper = {
        0: '.',
        1: '|',
        2: '#',
        3: '=',
        4: 'O'
    }

    grid = []
    for _ in range(22):
        grid.append(['.']*38)

    while True:

        op, rel_base, i, seq = intcode_new(seq, grid, rel_base, bp, pp, i)

        if op[0] == -1 and op[1] == 0:
            curr_score = op[2]
            print("-"*20)
            print("SCORE:", curr_score)
            print("-"*20)

        elif op[0] >= 0 and op[1] >= 0:
            grid[op[1]][op[0]] = mapper[op[2]]

            if op[2] == 3:
                pp = op[0]

            if op[2] == 4:
                bp = op[0]

        if rel_base == -1 and i == -1:
            break
        tiles.append(op)


if __name__ == "__main__":
    seq = list(map(int, open("13.txt", "r").read().split(",")))

    # part 1
    draw_tiles(seq)

    # part 2
    seq[0] = 2
    play(seq)
