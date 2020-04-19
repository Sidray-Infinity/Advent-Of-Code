
import operator


def straight_line_potential(seq, u, v):
    """
    Calculates just the straight line potential
    """

    r = len(seq)
    c = len(seq[0])

    potential = 0

    # Row vector; pos side
    i = v+1
    while i < c:
        if seq[u][i] == '#':
            potential += 1
            break
        i += 1

    # Row vector; neg side
    i = v-1
    while i >= 0:
        if seq[u][i] == '#':
            potential += 1
            break
        i -= 1

    # Column vector; pos side
    i = u+1
    while i < r:
        if seq[i][v] == '#':
            potential += 1
            break
        i += 1

    # column vector; neg side
    i = u-1
    while i >= 0:
        if seq[i][v] == '#':
            potential += 1
            break
        i -= 1

    return potential


def get_potential(seq, u, v):
    """
    * Returns the monitoring potential of the position (i, j)
    * Explore a line of sight till you hit an asteroid, or the boundary
    """

    r = len(seq)
    c = len(seq[0])

    potential = 0

    # The 2 row and column vectors
    potential = straight_line_potential(seq, u, v)

    # Quad 1

    blocks = []
    for a in range(1, r-u):
        for b in range(1, c-v):

            if a == b and a != 1:
                continue

            flag = True
            for block in blocks:
                if a > block[0] and b > block[1]:
                    if a/block[0] == b/block[1] and block != (1, 1):
                        flag = False
                        break

            if flag == False:
                continue

            U, V = u+a, v+b

            while U < r and V < c:

                if seq[U][V] == '#':
                    blocks.append((a, b))
                    potential += 1
                    break

                U, V = U+a, V+b

    # Quad 2
    blocks = []
    for a in range(1, u+1):
        for b in range(1, c-v):

            if a == b and a != 1:
                continue

            flag = True
            for block in blocks:
                if a > block[0] and b > block[1]:
                    if a/block[0] == b/block[1] and block != (1, 1):
                        flag = False
                        break

            if flag == False:
                continue

            U, V = u-a, v+b

            while U >= 0 and V < c:

                if seq[U][V] == '#':
                    blocks.append((a, b))
                    potential += 1
                    break

                U, V = U-a, V+b

    # Quad 3
    blocks = []
    for a in range(1, u+1):
        for b in range(1, v+1):

            if a == b and a != 1:
                continue

            flag = True
            for block in blocks:
                if a > block[0] and b > block[1]:
                    if a/block[0] == b/block[1] and block != (1, 1):
                        flag = False
                        break

            if flag == False:
                continue

            U, V = u-a, v-b

            while U >= 0 and V >= 0:

                if seq[U][V] == '#':
                    blocks.append((a, b))
                    potential += 1
                    break
                U, V = U-a, V-b

    # Quad 4
    blocks = []
    for a in range(1, r-u):
        for b in range(1, v+1):

            if a == b and a != 1:
                continue

            flag = True
            for block in blocks:
                if a > block[0] and b > block[1]:
                    if a/block[0] == b/block[1] and block != (1, 1):
                        flag = False
                        break

            if flag == False:
                continue

            U, V = u+a, v-b

            while U < r and V >= 0:

                if seq[U][V] == '#':
                    blocks.append((a, b))
                    potential += 1
                    break

                U, V = U+a, V-b

    return potential


def destroy_asteroids(seq, coord):
    """
    returns the coordinate of 200th asteroid to be destroyed
    """

    u = coord[0]
    v = coord[1]
    count = 0
    last_victim = (0, 0)
    r = len(seq)
    c = len(seq[0])

    while True:

        # pos up
        if count >= 200:
            return last_victim
        i = u-1
        while i > 0:
            if seq[i][v] == '#':
                seq[i][v] = '.'
                count += 1
                last_victim = (i, v)
                break
            i -= 1

        # quad 1
        blocks = []
        points = []
        for a in range(1, u+1):
            for b in range(1, c-v):
                if a == b and a != 1:
                    continue
                flag = True
                for block in blocks:
                    if a > block[0] and b > block[1]:
                        if a/block[0] == b/block[1] and block != (1, 1):
                            flag = False
                            break

                if flag == False:
                    continue

                U, V = u-a, v+b

                while U >= 0 and V < c:
                    if seq[U][V] == '#':
                        m = abs(V-v)/abs(U-u)
                        points.append((U, V, m))
                        blocks.append((a, b))
                        seq[U][V] = '.'
                        break

                    U, V = U-a, V+b

        points = sorted(points, key=lambda x: x[2])

        print(count, last_victim)
        for p in points:
            if count >= 200:
                return last_victim
            last_victim = (p[0], p[1])
            count += 1
            print(count, (p[0], p[1]))

        # pos right
        if count >= 200:
            return last_victim
        i = v+1
        while i < c:
            if seq[u][i] == '#':
                seq[u][i] = '.'
                count += 1
                last_victim = (u, i)
                break
            i += 1

        # quad 2
        blocks = []
        points = []
        for a in range(1, r-u):
            for b in range(1, c-v):
                if a == b and a != 1:
                    continue
                flag = True
                for block in blocks:
                    if a > block[0] and b > block[1]:
                        if a/block[0] == b/block[1] and block != (1, 1):
                            flag = False
                            break

                if flag == False:
                    continue

                U, V = u+a, v+b

                while U < r and V < c:
                    if seq[U][V] == '#':
                        m = abs(V-v)/abs(U-u)
                        points.append((U, V, m))
                        blocks.append((a, b))
                        seq[U][V] = '.'
                        break

                    U, V = U+a, V+b

        points = sorted(points, key=lambda x: x[2], reverse=True)

        print(count, last_victim)
        for p in points:
            if count >= 200:
                return last_victim
            last_victim = (p[0], p[1])
            count += 1
            print(count, (p[0], p[1]))

        # pos down
        if count >= 200:
            return last_victim
        i = u+1
        while i < r:
            if seq[i][v] == '#':
                seq[i][v] = '.'
                count += 1
                last_victim = (i, v)
                break
            i += 1

        # quad 3
        blocks = []
        points = []
        for a in range(1, r-u):
            for b in range(1, v+1):
                if a == b and a != 1:
                    continue
                flag = True
                for block in blocks:
                    if a > block[0] and b > block[1]:
                        if a/block[0] == b/block[1] and block != (1, 1):
                            flag = False
                            break

                if flag == False:
                    continue

                U, V = u+a, v-b

                while U < r and V >= 0:
                    if seq[U][V] == '#':
                        m = abs(V-v)/abs(U-u)
                        points.append((U, V, m))
                        blocks.append((a, b))
                        seq[U][V] = '.'
                        break

                    U, V = U+a, V-b

        points = sorted(points, key=lambda x: x[2])

        print(count, last_victim)
        for p in points:
            if count >= 200:
                return last_victim
            last_victim = (p[0], p[1])
            count += 1
            print(count, (p[0], p[1]))

        # pos left
        if count >= 200:
            return last_victim
        i = v-1
        while i > 0:
            if seq[u][i] == '#':
                seq[u][i] = '.'
                count += 1
                last_victim = (u, i)
                break
            i -= 1

        # quad 4
        blocks = []
        points = []
        for a in range(1, u+1):
            for b in range(1, v+1):
                if a == b and a != 1:
                    continue
                flag = True
                for block in blocks:
                    if a > block[0] and b > block[1]:
                        if a/block[0] == b/block[1] and block != (1, 1):
                            flag = False
                            break

                if flag == False:
                    continue

                U, V = u-a, v-b

                while U >= 0 and V >= 0:
                    if seq[U][V] == '#':
                        m = abs(V-v)/abs(U-u)
                        points.append((U, V, m))
                        blocks.append((a, b))
                        seq[U][V] = '.'
                        break

                    U, V = U-a, V-b

        points = sorted(points, key=lambda x: x[2], reverse=True)

        print(count, last_victim)
        for p in points:
            if count >= 200:
                return last_victim
            last_victim = (p[0], p[1])
            count += 1
            print(count, (p[0], p[1]))


def best_asteroid(seq):
    """
    Returns the coordinates and the monitoring potential of the
    best asteroid
    """

    potentials = {}
    max_pot = 0
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] == '#':
                pot = get_potential(seq, i, j)
                potentials[(i, j)] = pot
                max_pot = max(max_pot, pot)

    return max_pot, max(potentials.items(), key=operator.itemgetter(1))[0]


if __name__ == "__main__":

    seq = [list(x) for x in open("10.txt", "r").read().split("\n")]

    """
    * A monitoring station can detect any asteroid to which it has
      direct line of sight
    * This line of sight can be at any angle, not just lines aligned
      to the grid or diagonally.
    * lazer initial direction is up, rotates clockwise
    """

    # Part 1
    max_pot, coord = best_asteroid(seq)
    print(max_pot, coord)  # Takes time, have patience

    # Part 2
    pos = destroy_asteroids(seq, coord)
    print(pos, pos[1]*100 + pos[0])
