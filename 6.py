
from collections import defaultdict
import copy


def get_orbit_map(seq):

    orbits = defaultdict(list)

    for s in seq:
        a, b = s.split(')')[0], s.split(')')[1]
        orbits[a].append(b)

    final_orbits = copy.copy(orbits)

    for k in orbits.keys():
        for ele in orbits[k]:
            if orbits.get(ele, None) == None:
                final_orbits[ele] = []

    return final_orbits


def calculate_orbits(seq):
    """
    * Except COM, every object is in orbit around exactly one other object.
    * AAA)BBB -> BBB is in orbit around AAA
    * Return : sum of direct and indirect oribits
    """

    num_direct_orbits = 0
    num_indirect_orbits = 0

    final_orbits = get_orbit_map(seq)

    # print(final_orbits)

    for k in final_orbits.keys():
        # Counting direct orbits
        num_direct_orbits += len(final_orbits[k])

    for k in final_orbits.keys():
        t = 0
        if k != 'COM':
            for k1 in final_orbits.keys():
                if k in final_orbits[k1]:
                    P = k1

            while P != 'COM':
                t += 1
                if P != "":
                    k = P
                for k1 in final_orbits.keys():
                    if k in final_orbits[k1]:
                        P = k1

        num_indirect_orbits += t

    return num_direct_orbits + num_indirect_orbits


def num_orbit_trasfer(seq):

    orbits = get_orbit_map(seq)

    # Determine highest common ancestor

    ans_you = []
    ans_san = []
    P_you, P_san = '', ''

    for k in orbits.keys():
        if 'YOU' in orbits[k]:
            P_you = k
        if 'SAN' in orbits[k]:
            P_san = k

    k = P_you
    P = ''
    while P != "COM":
        if P != '':
            k = P
        for k1 in orbits.keys():
            if k in orbits[k1]:
                ans_you.append(k1)
                P = k1

    k = P_san
    P = ''
    while P != "COM":
        if P != '':
            k = P
        for k1 in orbits.keys():
            if k in orbits[k1]:
                ans_san.append(k1)
                P = k1

    nearest_ans = ''
    for x in ans_you:
        if x in ans_san:
            nearest_ans = x
            break

    jumps = 2                  # To include the jump to current orbting planets

    for x in ans_you:
        if x == nearest_ans:
            break
        jumps += 1

    for x in ans_san:
        if x == nearest_ans:
            break
        jumps += 1

    return jumps


if __name__ == "__main__":
    seq = open("6.txt", "r").read().split('\n')

    # Part 1
    print(calculate_orbits(seq))  # takes time, have patience

    # Part 2
    print(num_orbit_trasfer(seq))
