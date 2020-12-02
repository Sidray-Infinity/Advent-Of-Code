


if __name__ == "__main__":
    data = open("2.txt").read().split('\n')
    valid = 0

    for d in data:
        eles = d.split(' ')
        l = int(eles[0].split('-')[0])
        u = int(eles[0].split('-')[1])
        t = eles[1][0]
        count = 0
        for c in eles[2]:
            if c == t:
                count += 1

        if count >= l and count <= u:
            valid += 1

    print("PART1:", valid)
    valid = 0
    for d in data:
        eles = d.split(' ')
        pos1 = int(eles[0].split('-')[0])
        pos2 = int(eles[0].split('-')[1])
        t = eles[1][0]

        if (eles[2][pos1-1] == t and eles[2][pos2-1] != t) or (eles[2][pos1-1] != t and eles[2][pos2-1] == t):
            valid += 1

    print("PART2:", valid)