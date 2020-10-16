

def isValid(x):
    """
    Criterias :
    * Atleast 1 pair of repeated adjacent digits
    * Non decreasing in nature (can be increasing, or constant)
    """

    x_str = list(str(x))
    max_ = int(x_str[0])
    has_rep = False

    for i in range(len(x_str)):
        if i > 0 and x_str[i] == x_str[i-1]:
            has_rep = True
        if int(x_str[i]) < max_:
            return False
        max_ = int(x_str[i])

    if has_rep:
        return True
    return False


def isValid_modified(x):
    """
    Criterias :
    * Atleast 1 pair of repeated adjacent digits
    * Non decreasing in nature (can be increasing, or constant)
    """

    x_str = list(str(x))
    max_ = int(x_str[0])
    has_rep = False

    for i in range(len(x_str)):

        """
        Make sure the number is non decreasing,
        and checks if it has adjacent repeatation
        """

        if i > 0 and x_str[i] == x_str[i-1]:
            has_rep = True
        if int(x_str[i]) < max_:
            return False
        max_ = int(x_str[i])

    if has_rep:
        reps = {}
        for i in range(1, len(x_str)):
            if x_str[i] == x_str[i-1]:
                if reps.get(x_str[i], None) == None:
                    reps[x_str[i]] = 2
                else:
                    reps[x_str[i]] += 1

        for key in reps.keys():
            if reps[key] == 2:
                return True

    return False


if __name__ == "__main__":

    l, u = 240298, 784956
    print(l, u)

    # Part 1

    count = 0
    for i in range(l, u):
        if isValid(i):
            count += 1

    print(count)

    # Part 2

    count = 0
    for i in range(l, u):
        if isValid_modified(i):
            count += 1

    print(count)
