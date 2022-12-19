with open ("./data.txt", "r") as file:
    lines = list(map(lambda x: x.strip("\n").split(","), file.readlines()))
    lines = [tuple([int(y) for y in x]) for x in lines]

    print(lines)

    count = 0
    sides = [(-1,0,0), (1,0,0), (0,-1,0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for x, y, z in lines:
        for dx, dy, dz in sides:
            if (x+dx, y+dy, z+dz) not in lines:
                count += 1
    
    print(count)