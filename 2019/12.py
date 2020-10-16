import time
import numpy as np
from itertools import combinations


class System(object):
    def __init__(self, m1, m2, m3, m4):
        super().__init__()
        self.moons = [m1, m2, m3, m4]
        self.history = []

    def update_history(self):
        update = []
        for m in self.moons:
            update.append(m.pos + m.vel)

        self.history.append(update)

    def __call__(self, m1, m2, m3, m4):
        self.moons = [m1, m2, m3, m4]

    def history_repeated(self):
        update = []
        for m in self.moons:
            update.append(m.pos + m.vel)
        for d in self.history:
            if d == update:
                print("History repeated!")
                return True

        return False


def cmp(a, b):
    return 0 if a == b else -1 if a < b else 1


class Moon(object):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.vel = [0, 0, 0]
        self.pe = sum([abs(x) for x in self.pos])
        self.ke = sum([abs(x) for x in self.vel])
        self.history = {tuple(self.pos): [self.vel]}

    def update_pos(self):
        for i, v in enumerate(self.vel):
            self.pos[i] += v
        self.pe = sum([abs(x) for x in self.pos])

    def update_ke(self):
        self.ke = sum([abs(x) for x in self.vel])

    def changeGravity(self, other):
        for i in range(3):
            d = cmp(self.pos[i], other.pos[i])
            self.vel[i] -= d
            other.vel[i] += d


def gravity(m1, m2):

    for i in range(3):

        if m1.pos[i] < m2.pos[i]:
            m1.vel[i] += 1
            m2.vel[i] -= 1
        elif m1.pos[i] > m2.pos[i]:
            m1.vel[i] -= 1
            m2.vel[i] += 1

    return m1, m2


def print_info(i, a, b, c, d):

    print(f"After {i} steps:")
    print("pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>" %
          (a.pos[0], a.pos[1], a.pos[2], a.vel[0], a.vel[1], a.vel[2]))
    print("pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>" %
          (b.pos[0], b.pos[1], b.pos[2], b.vel[0], b.vel[1], b.vel[2]))
    print("pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>" %
          (c.pos[0], c.pos[1], c.pos[2], c.vel[0], c.vel[1], c.vel[2]))
    print("pos=<x=%3d, y=%3d, z=%3d>, vel=<x=%3d, y=%3d, z=%3d>" %
          (d.pos[0], d.pos[1], d.pos[2], d.vel[0], d.vel[1], d.vel[2]))
    print("-------------------------------------------------------")


def simulate():
    """
    * Each moon has 3d pos and 3d velocity(starting as 0)
    * For each time step, first update velocity, then pos
    """
    io = Moon([0, 4, 0])
    eu = Moon([-10, -6, -14])
    ga = Moon([9, -16, -3])
    ca = Moon([6, -1, 2])

    for i in range(1, 1001):

        # input()
        io, eu = gravity(io, eu)
        io, ga = gravity(io, ga)
        io, ca = gravity(io, ca)
        eu, ga = gravity(eu, ga)
        eu, ca = gravity(eu, ca)
        ga, ca = gravity(ga, ca)

        io.update_pos()
        eu.update_pos()
        ga.update_pos()
        ca.update_pos()

        io.update_ke()
        eu.update_ke()
        ga.update_ke()
        ca.update_ke()

        print_info(i, io, eu, ga, ca)


def simulate2():

    io = Moon([8, -10, 0])
    eu = Moon([5, 5, 10])
    ga = Moon([2, -7, 3])
    ca = Moon([9, -8, -3])
    steps = 0

    s = System(io, eu, ga, ca)
    s.update_history()

    while True:

        io, eu = gravity(io, eu)
        io, ga = gravity(io, ga)
        io, ca = gravity(io, ca)
        eu, ga = gravity(eu, ga)
        eu, ca = gravity(eu, ca)
        ga, ca = gravity(ga, ca)

        io.update_pos()
        eu.update_pos()
        ga.update_pos()
        ca.update_pos()

        s(io, eu, ga, ca)

        steps += 1
        print(steps)

        if s.history_repeated():
            print(steps)
            break

        s.update_history()


def simulate3():
    pos = np.asarray([[],
                      [],
                      [],
                      []])


if __name__ == "__main__":

    simulate2()
