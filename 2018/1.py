
if __name__ == "__main__":
    
    data = open("1.txt").read().split("\n")
    data = list(map(int, data))

    
    print(sum(data))

    seen = {0}
    found = False
    ans = 0
    result = 0

    while found == False:
        for drift in data:
            result += drift
            if result in seen:
                found = True
                ans = result
                break
            else:
                seen.add(result)
    print(ans)
