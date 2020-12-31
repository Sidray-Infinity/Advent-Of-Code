
def getNthNumberSpoken(n, data):
    age_tracker = {num:i+1 for i, num in enumerate(data[:-1])}
    next_num = data[-1]
    spoken_num = None
    for turn in range(len(data)+1, n+1):
        # print(turn)
        last_turn_count = turn - 1
        if next_num in age_tracker:
            spoken_num = last_turn_count - age_tracker[next_num]
        else:
            spoken_num = 0
        age_tracker[next_num] = last_turn_count
        next_num = spoken_num

    return spoken_num

if __name__ == "__main__":
    data = list(map(int, open("15.txt").read().split(',')))
    print('Part1:', getNthNumberSpoken(2020, data)) # O(n)
    print('Part2:', getNthNumberSpoken(30000000, data))
