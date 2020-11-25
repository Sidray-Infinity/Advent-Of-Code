import numpy as np

if __name__ == "__main__":

    data = open("3.txt").read().split('\n')

    data = [d.split('@')[1] for d in data]
    data = [d.split(':') for d in data]
    data = [[list(map(int, d[0].split(','))), list(map(int, d[1].split('x')))] for d in data]
    
    sheet = np.asarray([[set()] * 1000] * 1000)
    for i in range(len(data)):
        print(i, data[i])
        for j in range(data[i][0][1] + 1, data[i][0][1] + data[i][1][1]):
            for k in range(data[i][0][0] + 1, data[i][0][0] + data[i][1][0]):
                sheet[j][k].add(i)

    count = 0
    print(sheet)
    for i in range(1000):
        for j in range(1000):
            if len(sheet[i][j]) >= 2:
                count += 1
    print(count)