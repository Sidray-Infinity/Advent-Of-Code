from collections import Counter

if __name__ == "__main__":
    jolts = list(map(int, open("10.txt").read().split('\n')))
    currJolt = 0
    
    jolts = sorted(jolts)
    jolts.append(jolts[-1]+3)

    diffs = {1:0, 2:0, 3:0}

    for j in jolts:
        diffs[j - currJolt] += 1
        currJolt = j

    print("Part1:", diffs[1] * diffs[3])

    dp = Counter()
    dp[0] = 1

    for jolt in jolts:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]
    
    print("Part2:", dp[jolts[-1]])
    