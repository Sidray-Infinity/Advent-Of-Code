def binarySearch(data, l, r, x):
    if l > r:
        return -1
    elif l == r:
        if data[l] == x:
            return x
        else:
            return -1

    mid = (l+r)//2
    if data[mid] == x:
        return x
    elif data[mid] < x:
        return binarySearch(data, mid+1, r, x)    
    else:
        return binarySearch(data, l, mid, x)  

if __name__ == "__main__":
    data = list(map(int, open("1.txt").read().split('\n')))
    data = sorted(data)
    for d in data:
        val = binarySearch(data, 0, len(data)-1, 2020-d)
        if val != -1:
            print('PART1:', d * val)
            break

    for i in range(len(data)):
        flag = False
        for j in range(i, len(data)):
            val = binarySearch(data, 0, len(data)-1, 2020-data[i]-data[j])
            if val != -1:
                flag = True
                print('PART2:', data[i] * data[j] * val)
                break
        if flag:
            break