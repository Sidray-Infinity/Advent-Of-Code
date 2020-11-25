from datetime import datetime
from collections import defaultdict, Counter

if __name__ == "__main__":
    data = open("4.txt").read().split('\n')
    data.sort(key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'))
    time = defaultdict(list)
    
    guard = {} # To find the guard that sleeps the most
    curr_guard = int(data[0].split(' ')[3].strip('#'))
    for i in range(1, len(data)):
        eles_prev = data[i-1].split(' ')
        eles_curr = data[i].split(' ')
        if eles_curr[2] == "Guard":
            curr_guard = int(eles_curr[3].strip('#'))
        elif eles_curr[2] == "wakes":
            if guard.get(curr_guard, None) == None:
                guard[curr_guard] = int(eles_curr[1][3:5]) - int(eles_prev[1][3:5])
            else:
                guard[curr_guard] += int(eles_curr[1][3:5]) - int(eles_prev[1][3:5])
            for i in range(int(eles_prev[1][3:5]), int(eles_curr[1][3:5])):
                    time[i].append(curr_guard)

    sleepy_guard = max(guard, key=guard.get)

    req_time = 0
    max_freq = 0

    for k in time.keys():
        count = 0
        for e in time[k]:
            if e == sleepy_guard:
                count += 1

        if count > max_freq:
            max_freq = count
            req_time = k

    print('PART 1 :', req_time * sleepy_guard)

    req_time = 0
    max_freq = 0
    freq_guard = None

    for k in time.keys():
        freqs = dict(Counter(time[k]))
        if max(freqs.values()) > max_freq:
            max_freq = max(freqs.values())
            req_time = k
            for f in freqs.keys():
                if freqs[f] == max_freq:
                    freq_guard = f
                    break
    print('PART 2: ', freq_guard*req_time)
