
max_color_values = {
    "red": 12,
    "green": 13,
    "blue": 14
}

rows = open("2.txt").read().split("\n")

res1 = 0
for row in rows:
    skip_game = False
    game_info = row.split(": ")
    game_id = int(game_info[0].split(" ")[1])
    sets = game_info[1].split("; ")
    for s in sets:
        cubes = s.split(", ")
        for c in cubes:
            cubes_info = c.split(" ")
            if int(cubes_info[0]) > max_color_values[cubes_info[1]]:
                skip_game = True
                break

            if skip_game:
                break

    if skip_game:
        continue

    res1 += game_id

res2 = 0
for row in  rows:
    min_power = 999999999999999999
    game_info = row.split(": ")
    game_id = int(game_info[0].split(" ")[1])
    sets = game_info[1].split("; ")
    nr, nb, ng = 0, 0, 0
    for s in sets:
        cubes = s.split(", ")
        for c in cubes:
            cubes_info = c.split(" ")
            print(cubes_info)
            if cubes_info[1] == "red":
                nr = max(nr, int(cubes_info[0]))
            if cubes_info[1] == "green":
                ng = max(ng, int(cubes_info[0]))
            if cubes_info[1] == "blue":
                nb = max(nb, int(cubes_info[0]))
    min_power = min(min_power, nr*ng*nb)
    res2 += min_power


print("Part1:", res1)
print("Part2:", res2)