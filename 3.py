import math


def get_trace(dir_line):
    """
    Returns the trace (order of points as traversed) for the given
    instructions.
    """
    trace = [(0, 0)]

    for i, cmnd in enumerate(dir_line):
        if cmnd[0] == 'R':
            new_pos = (trace[i][0] + int(cmnd[1:]), trace[i][1])
        if cmnd[0] == 'L':
            new_pos = (trace[i][0] - int(cmnd[1:]), trace[i][1])
        if cmnd[0] == 'U':
            new_pos = (trace[i][0], trace[i][1] + int(cmnd[1:]))
        if cmnd[0] == 'D':
            new_pos = (trace[i][0], trace[i][1] - int(cmnd[1:]))
        trace.append(new_pos)
    return trace


def get_intersection_distances(int_points, trace):
    l_steps = []

    for point in int_points:
        steps = 0
        #print("STEPS:", steps, "L1:", l1_steps)
        for i in range(len(trace)-1):
            a = trace[i]
            b = trace[i+1]

            if a[0] == b[0]:
                # Veritcal line segment
                if point[0] == a[0]:
                    if (point[1] > a[1] and point[1] < b[1]) \
                            or (point[1] < a[1] and point[1] > b[1]):
                        steps += abs(a[1] - point[1])
                        break
                else:
                    steps += abs(a[1] - b[1])

            elif a[1] == b[1]:
                # horizontal line segment
                if point[1] == a[1]:
                    if (point[0] > a[0] and point[0] < b[0]) \
                            or (point[0] < a[0] and point[0] > b[0]):
                        steps += abs(a[0] - point[0])
                        break
                else:
                    steps += abs(a[0] - b[0])

        l_steps.append(steps)
    return l_steps


if __name__ == "__main__":

    # Part 1

    f = open("3.txt", "r")

    dir_line1 = f.readline().split(',')
    dir_line2 = f.readline().split(',')

    # The stupid /n at the end. Remove it !
    dir_line1[len(dir_line1)-1] = dir_line1[len(dir_line1)-1][:-1]

    trace1 = get_trace(dir_line1)
    trace2 = get_trace(dir_line2)

    int_points = []

    for i in range(len(trace1)-1):
        a1 = trace1[i]
        a2 = trace1[i+1]

        for j in range(len(trace2)-1):
            b1 = trace2[j]
            b2 = trace2[j+1]

            if a1[0] == a2[0]:
                # base line is Vertical line
                if b1[1] == b2[1]:
                    # target line is horizontal
                    if (b1[1] >= a1[1] and b1[1] <= a2[1]) \
                            or (b1[1] >= a2[1] and b1[1] <= a1[1]):
                        if (b1[0] > a1[0] and b2[0] < a1[0]) \
                                or (b1[0] < a1[0] and b2[0] > a1[0]):
                            # Found intersection point
                            int_point = (a1[0], b1[1])
                            int_points.append(int_point)

            elif a1[1] == a2[1]:
                # base line is Horizontal line
                if b1[0] == b2[0]:
                    # target line is vertical
                    if (b1[0] >= a1[0] and b1[0] <= a2[0]) \
                            or (b1[0] >= a2[0] and b1[0] <= a1[0]):
                        if (b1[1] > a1[1] and b2[1] < a1[1]) \
                                or (b1[1] < a1[1] and b2[1] > a1[1]):
                            # Found intersection point
                            int_point = (b1[0], a1[1])
                            int_points.append(int_point)

    distances = [abs(x[0])+abs(x[1]) for x in int_points]
    print(min(distances))

    # Part 2 ------------------------------------------------------

    l1_steps = []
    l2_steps = []

    l1_steps = get_intersection_distances(int_points, trace1)
    l2_steps = get_intersection_distances(int_points, trace2)

    print(l1_steps)
    print(l2_steps)

    final = []
    for i in range(len(l1_steps)):
        final.append(l1_steps[i]+l2_steps[i])

    print(min(final))
