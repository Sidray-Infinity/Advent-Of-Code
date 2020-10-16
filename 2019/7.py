
from itertools import permutations
import copy


def intcode_new(seq, phase, input_=0):
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

    phase_ip = True

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
            if phase_ip:
                x = phase
                phase_ip = False
            else:
                x = input_
            seq[seq[i+1]] = x

            i += 2

        if op_code == '04':
            if mode_1 == '0':
                a = seq[seq[i+1]]
            elif mode_1 == '1':
                a = seq[i+1]

            i += 2
            return a

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


def max_thrust(seq):

    base_phase = list(range(0, 5))
    op_signals = []

    s1 = copy.copy(seq)
    s2 = copy.copy(seq)
    s3 = copy.copy(seq)
    s4 = copy.copy(seq)
    s5 = copy.copy(seq)

    phases = list(permutations(base_phase))

    for p in phases:

        s1 = copy.copy(seq)
        s2 = copy.copy(seq)
        s3 = copy.copy(seq)
        s4 = copy.copy(seq)
        s5 = copy.copy(seq)

        o1 = intcode_new(s1, p[0])
        o2 = intcode_new(s2, p[1], o1)
        o3 = intcode_new(s3, p[2], o2)
        o4 = intcode_new(s4, p[3], o3)
        o5 = intcode_new(s5, p[4], o4)

        op_signals.append(o5)

    return max(op_signals)


"""

MY CODE. DEBUG IT

def intcode_new_fb(amp, phase, input_=0):
    i = 0
    phase_ip = True

    while i < len(amp.seq):
        inst = list(str(amp.seq[i]))
        while len(inst) != 4:
            inst.insert(0, '0')

        op_code = ''.join(inst[-2:])
        mode_1 = inst[1]
        mode_2 = inst[0]

        if op_code == "99":
            amp.halt = True
            return amp

        if op_code == '01':
            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]     # Para1 in adress mode
            elif mode_1 == '1':
                a = amp.seq[i+1]          # Para1 in immediate mode

            if mode_2 == '0':
                b = amp.seq[amp.seq[i+2]]     # Para2 in adress mode
            elif mode_2 == '1':
                b = amp.seq[i+2]          # Para2 in immediate mode

            amp.seq[amp.seq[i+3]] = a + b
            i += 4

        if op_code == '02':
            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            if mode_2 == '0':
                b = amp.seq[amp.seq[i+2]]
            elif mode_2 == '1':
                b = amp.seq[i+2]

            amp.seq[amp.seq[i+3]] = a * b
            i += 4

        if op_code == '03':
            if phase_ip:
                x = phase
                phase_ip = False
            else:
                x = input_
            amp.seq[amp.seq[i+1]] = x

            i += 2

        if op_code == '04':
            if mode_1 == '0':
                a = amp.seq[seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            i += 2
            amp.output = a
            return amp

        if op_code == '05':

            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            if a != 0:
                if mode_2 == '0':
                    b = amp.seq[amp.seq[i+2]]
                elif mode_2 == '1':
                    b = amp.seq[i+2]
                i = b
            else:
                i += 3

        if op_code == '06':
            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            if a == 0:
                if mode_2 == '0':
                    b = amp.seq[amp.seq[i+2]]
                elif mode_2 == '1':
                    b = amp.seq[i+2]
                i = b
            else:
                i += 3
        if op_code == '07':
            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            if mode_2 == '0':
                b = amp.seq[amp.seq[i+2]]
            elif mode_2 == '1':
                b = amp.seq[i+2]

            if a < b:
                amp.seq[amp.seq[i+3]] = 1
            else:
                amp.seq[amp.seq[i+3]] = 0
            i += 4

        if op_code == '08':
            if mode_1 == '0':
                a = amp.seq[amp.seq[i+1]]
            elif mode_1 == '1':
                a = amp.seq[i+1]

            if mode_2 == '0':
                b = amp.seq[amp.seq[i+2]]
            elif mode_2 == '1':
                b = amp.seq[i+2]

            if a == b:
                amp.seq[amp.seq[i+3]] = 1
            else:
                amp.seq[amp.seq[i+3]] = 0
            i += 4


class Amplifier(object):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq
        self.halt = False
        self.output = None


def max_thrust_with_feedback(seq):

    op_thrusts = []
    phases = list(permutations(list(range(5, 10))))

    for p in phases:

        # Define 5 amplifiers
        amps = [Amplifier(seq) for i in range(5)]

        # hardcode the first loop
        amps[0] = intcode_new_fb(amps[0], p[0], 0)
        amps[1] = intcode_new_fb(amps[1], p[1], amps[0].output)
        amps[2] = intcode_new_fb(amps[2], p[2], amps[1].output)
        amps[3] = intcode_new_fb(amps[3], p[3], amps[2].output)
        amps[4] = intcode_new_fb(amps[4], p[4], amps[3].output)

        active = 0
        prev = 4

        while not amps[4].halt:

            
            if active == 0:
                prev = 4
            else:
                prev = active - 1
          
            amps[active] = intcode_new_fb(
                amps[active], p[active], amps[prev].output)
            active = (active + 1) % 5

        op_thrusts.append(amps[4].output)

    return op_thrusts
"""


class Amp:
    def __init__(self, prog):
        self.prog = prog[:]
        self.ip = 0
        self.output = 0
        self.input_counter = 0
        self.halt = False


def split_instruction(instruction):
    instruction = f"{instruction:05}"
    return instruction[3:], instruction[0:3]


def get_values(input, pos, op, modes):
    mode_a, mode_b, mode_c = modes
    values = []

    if op in ["01", "02", "04", "05", "06", "07", "08"]:
        if mode_c == "0":
            values.append(input[input[pos+1]])
        else:
            values.append(input[pos+1])

        if op in ["01", "02", "05", "06", "07", "08"]:
            if mode_b == "0":
                values.append(input[input[pos+2]])
            else:
                values.append(input[pos+2])

            if op in []:
                if mode_a == "0":
                    values.append(input[input[pos+3]])
                else:
                    values.append(input[pos+3])

    return values


def run_amp(phase, input, amp):
    while amp.prog[amp.ip] != 99:
        op, modes = split_instruction(amp.prog[amp.ip])
        values = get_values(amp.prog, amp.ip, op, modes)

        if op == "01":  # Addition
            amp.prog[amp.prog[amp.ip+3]] = values[0] + values[1]
            amp.ip += 4

        if op == "02":  # Multiplication
            amp.prog[amp.prog[amp.ip+3]] = values[0] * values[1]
            amp.ip += 4

        if op == "03":  # Read and Store input
            if not amp.input_counter:
                amp.prog[amp.prog[amp.ip+1]] = phase
            else:
                amp.prog[amp.prog[amp.ip+1]] = input

            amp.input_counter += 1
            amp.ip += 2

        if op == "04":  # Print Output
            amp.output = values[0]
            amp.ip += 2
            return amp

        if op == "05":  # Jump-if-True
            if values[0]:
                amp.ip = values[1]
            else:
                amp.ip += 3

        if op == "06":  # Jump-if-False
            if not values[0]:
                amp.ip = values[1]
            else:
                amp.ip += 3

        if op == "07":  # Less than
            if values[0] < values[1]:
                amp.prog[amp.prog[amp.ip+3]] = 1
            else:
                amp.prog[amp.prog[amp.ip+3]] = 0
            amp.ip += 4

        if op == "08":  # Equals
            if values[0] == values[1]:
                amp.prog[amp.prog[amp.ip+3]] = 1
            else:
                amp.prog[amp.prog[amp.ip+3]] = 0
            amp.ip += 4

    amp.halt = True
    return amp


def solve(prog):

    max_thrust = 0

    for phases in permutations(range(5, 10), 5):
        amps = [Amp(prog) for i in range(5)]
        active = 0

        while not amps[4].halt:
            amps[active] = run_amp(
                phases[active], amps[active-1].output, amps[active])
            active = (active + 1) % 5

        max_thrust = max(max_thrust, amps[4].output)
    return max_thrust


if __name__ == "__main__":

    seq = list(map(int, open("7.txt", "r").read().split(',')))

    # Part 1
    # print(max_thrust(seq))

    # Part 2
    print(solve(seq))
