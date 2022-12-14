import math

def drop_sand(rock):
    sand_origin = (500, 0)
    can_move = True
    in_bounds = True
    sand_pos = sand_origin
    moves = [(0, 1), (-1, 1), (1, 1)]
    while(can_move and in_bounds):
        # print("current pos: ", sand_pos)
        move_available = False
        for move in moves:
            pos_check = sand_pos[0] + move[0], sand_pos[1] + move[1]
            # print(pos_check)
            if (pos_check[1] >= len(rock) or pos_check[0] >= len(rock[0])):
                in_bounds = False
                break

            val_at_pos = rock[pos_check[1]][pos_check[0]]
            if val_at_pos == ".":
                move_available = True
                sand_pos = pos_check
                break

        if not move_available:
            can_move = False


    came_to_rest = False
    if in_bounds and not can_move:
        # print("resting sand_pos: ", sand_pos)
        rock[sand_pos[1]][sand_pos[0]] = "o"
        came_to_rest = True

    return rock, came_to_rest

with open("./data.txt", "r") as file:
    lines = list(map(lambda x: x.strip().split("->"), file.readlines()))
    lines = [list(map(lambda x: tuple(map(lambda y: int(y), x.strip().split(","))), line)) for line in lines]

    x_min, x_max = math.inf, -math.inf
    y_min, y_max = math.inf, -math.inf

    for line in lines:
        for t in line:
            x,y = t
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)
    
    x_diff = x_max - x_min
    y_diff = y_max - y_min

    rock_width = 600
    rock_height = y_max + 5

    rock = [["." for _ in range(rock_width)] for _ in range(rock_height)]

    # print("rock dims")
    # print(len(rock), len(rock[0]))

    offset = [0, 0]

    for line in lines:
        for i in range(len(line) - 1):
            a, b = line[i:i+2]
            idx = 0 if a[0] - b[0] != 0 else 1
            off_val = a[abs(idx-1)] - offset[abs(idx-1)]
            # print(a,b)
            start, end = (a[idx], b[idx]) if a[idx] < b[idx] else (b[idx], a[idx])
            # print("start: ", start, "end: ", end)
            diff = end - start
            for i in range(start, end + 1):
                new_val = i - offset[idx]
                new_pos = [0, 0]
                new_pos[idx], new_pos[abs(idx-1)] = new_val, a[abs(idx-1)] - offset[abs(idx-1)]
                # print(new_pos)
                rock[new_pos[1]][new_pos[0]] = "#"


    units_at_rest = 0
    prev_units = None
    while (units_at_rest != prev_units):
        prev_units = units_at_rest
        rock, at_rest = drop_sand(rock)
        if at_rest:
            units_at_rest += 1

    print(units_at_rest)
