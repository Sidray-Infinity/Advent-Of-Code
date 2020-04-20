import numpy as np
import matplotlib.pyplot as plt


class Painter(object):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq
        self.halt = False
        self.dir = 0        # U:0, L:1, D:2, R:3
        self.pos = (0, 0)

    def update_seq(self, seq):
        self.seq = seq

    def move(self, pos):
        self.pos = pos


def intcode_new(seq, ip, rb, init=0):
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
        print("I:", i, "INST:", ''.join(inst), "IP:", ip)

        op_code = ''.join(inst[-2:])
        mode_1 = inst[2]
        mode_2 = inst[1]
        mode_3 = inst[0]

        if op_code == "99":
            return [-1, -1], -1, -1, seq

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
            x = ip

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
            # print(seq[8])
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
            if len(op) == 2:
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


def draw(seq):
    """
    Return the number of unique pixels it printed on.
    """

    visited_cells = {}
    p = Painter(seq)
    rb = 0
    i = 0

    while True:
        print(p.pos, rb, {0: "U", 1: "R", 2: "D", 3: "L"}[p.dir])
        # input()

        if visited_cells.get(p.pos, None) == None:
            op, rb, i, seq = intcode_new(p.seq, 0, rb, i)
        else:
            print("Found!", p.pos)
            op, rb, i, seq = intcode_new(p.seq, visited_cells[p.pos], rb, i)

        p.update_seq(seq)

        col, turn = op[0], op[1]
        if col == -1 and turn == -1 and rb == -1 and i == -1:
            break

        print("COL:", {0: "B", 1: "W"}[col],
              "TURN:", {0: "LEFT", 1: "RIGHT"}[turn])

        visited_cells[p.pos] = col

        if turn == 0:
            if p.dir == 0:
                p.dir = 3
            else:
                p.dir -= 1
        elif turn == 1:
            if p.dir == 3:
                p.dir = 0
            else:
                p.dir += 1

        if p.dir == 0:
            p.pos = (p.pos[0], p.pos[1]+1)
        elif p.dir == 1:
            p.pos = (p.pos[0]+1, p.pos[1])
        elif p.dir == 2:
            p.pos = (p.pos[0], p.pos[1]-1)
        elif p.dir == 3:
            p.pos = (p.pos[0]-1, p.pos[1])

    print(len(visited_cells))


def draw2(seq):
    """
    Return the number of unique pixels it printed on.
    """

    visited_cells = {}
    p = Painter(seq)
    rb = 0
    i = 0

    first = True

    while True:
        print(p.pos, rb, {0: "U", 1: "R", 2: "D", 3: "L"}[p.dir])

        if visited_cells.get(p.pos, None) == None:
            if first:
                first = False
                op, rb, i, seq = intcode_new(p.seq, 1, rb, i)
            else:
                op, rb, i, seq = intcode_new(p.seq, 0, rb, i)
        else:
            print("Found!", p.pos)
            op, rb, i, seq = intcode_new(p.seq, visited_cells[p.pos], rb, i)

        p.update_seq(seq)

        col, turn = op[0], op[1]
        if col == -1 and turn == -1 and rb == -1 and i == -1:
            break

        print("COL:", {0: "B", 1: "W"}[col],
              "TURN:", {0: "LEFT", 1: "RIGHT"}[turn])

        visited_cells[p.pos] = col

        if turn == 0:
            if p.dir == 0:
                p.dir = 3
            else:
                p.dir -= 1
        elif turn == 1:
            if p.dir == 3:
                p.dir = 0
            else:
                p.dir += 1

        if p.dir == 0:
            p.pos = (p.pos[0], p.pos[1]+1)
        elif p.dir == 1:
            p.pos = (p.pos[0]+1, p.pos[1])
        elif p.dir == 2:
            p.pos = (p.pos[0], p.pos[1]-1)
        elif p.dir == 3:
            p.pos = (p.pos[0]-1, p.pos[1])

    print(len(visited_cells))
    return visited_cells


if __name__ == "__main__":
    """
    * All panels initially black
    * I/P : 0 -> if robot over black panel, 1 -> over black panel
    * O/P : first -> color to be printed (0 -> B, 1 -> W)
            second -> turn direction (0->turn left, 1->turn right)
    * Move one step ahead after turning
    """
    seq = list(map(int, open("11.txt", "r").read().split(",")))

    # Part 1
    draw(seq)

    # Part 2
    cells = draw2(seq)

    grid = np.zeros((50, 50))

    for c in cells:
        grid[c[0]][c[1]] = cells[c]

    plt.imshow(grid)
    plt.show()
