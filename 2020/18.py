
class NewNum:
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return NewNum(self.x + o.x)

    def __sub__(self, o):
        return NewNum(self.x * o.x)

class NewNum2:
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return NewNum2(self.x * o.x)

    def __mul__(self, o):
        return NewNum2(self.x + o.x)

def wrapClass(line, c):
    arr = list(line)
    for i in range(len(arr)):
        if arr[i] in list(map(str, range(10))):
            arr[i] = c + "(" + arr[i] + ")"
        
    return ''.join(arr)


if __name__ == "__main__":
    data = open("18.txt").read().split('\n')
    s = 0
    for d in data:
        t = d.replace('*', '-')
        wrappedString = wrapClass(t, "NewNum")
        s += eval(wrappedString).x

    print("Part1:", s)

    s = 0
    for d in data:
        t = []
        for c in d:
            if c == '+':
                t.append('*')
            elif c == '*':
                t.append('+')
            else:
                t.append(c)

        t = ''.join(t)
        wrappedString = wrapClass(t, "NewNum2")
        s += eval(wrappedString).x

    print("Part2:", s)