
if __name__ == "__main__":
    pps = open("4.txt").read().split('\n\n')
    mapper = {'byr':0, 'iyr':1, 'eyr':2, 'hgt':3, 'hcl':4, 'ecl':5, 'pid':6}
    count = 0
    for p in pps:
        valid = [False]*7
        lines = p.split('\n')
        for l in lines:
            eles = l.split(' ')
            for e in eles:
                if e.split(':')[0] == "cid":
                    continue
                valid[mapper[e.split(':')[0]]] = True
        if all(valid):
            count += 1
    print("Part1:", count)

    count = 0
    validators = {
        'byr': lambda x : len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
        'iyr': lambda x : len(x) == 4 and int(x) >= 2010 and int(x) <= 2020, 
        'eyr': lambda x : len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
        'hgt': lambda x : True if (x[-2:] == "cm" and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or 
                                    (x[-2:] == "in" and int(x[:-2]) >= 59 and int(x[:-2]) <= 76)
                                else False,
        'hcl': lambda x : x[0] == '#' and len(x[1:]) == 6 and all([c in set('1234567890abcdef') for c in x[1:]]),
        'ecl': lambda x : x in set(["amb","blu","brn","gry","grn","hzl","oth"]),
        'pid': lambda x : len(x) == 9
    }
    for p in pps:
        valid = [False]*7
        lines = p.split('\n')
        for l in lines:
            eles = l.split(' ')
            for e in eles:
                field, value = e.split(':')
                if field == "cid":
                    continue
                if validators[field](value):
                    valid[mapper[field]] = True
        if all(valid):
            count += 1
    print("Part2:", count)


