

if __name__ == "__main__":

    # Part 1

    sum_fuel = 0

    f = open("1.txt", "r")
    for line in f.readlines():
        sum_fuel += int(line)//3 - 2

    print(sum_fuel)

    # Part 2

    final_fuel = 0
    f.seek(0)

    for line in f.readlines():
        mod_fule = int(line)//3 - 2
        t = mod_fule
        while mod_fule > 0:
            mod_fule = int(mod_fule)//3 - 2
            if mod_fule > 0:
                t += mod_fule
        final_fuel += t

    print(final_fuel)
