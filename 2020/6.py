

if __name__ == "__main__":
    data = open("6.txt").read().split('\n\n')

    count = 0
    for d in data:
        s = set()
        for ans in d.split('\n'):
            for c in ans:
                s.add(c)

        count += len(s)
    print('Part1:', count)

    count = 0
    for d in data:
        s = set(list("abcdefghijklmnopqrstuvwxyz"))
        for ans in d.split('\n'):
            s = s.intersection(set(list(ans)))

        count += len(s)
    print('Part2:', count)
