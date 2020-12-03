

if __name__ == "__main__":
    data = open("3.txt").read().split('\n')
    height = len(data)
    width = len(data[0])
    count = 0
    w = 3
    h = 1
    while h < height:
        if data[h][w] == '#':
            count += 1
        h += 1
        w = (w + 3) % width

    print("PART1:", count)

    res = 1
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for s in slopes:
        count = 0
        w = s[0]
        h = s[1]
        dw = s[0]
        dh = s[1]
        while h < height:
            if data[h][w] == '#':
                count += 1
            h += dh
            w = (w + dw) % width
        res *= count

    print("PART2:", res)

