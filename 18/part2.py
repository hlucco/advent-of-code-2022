with open ("./data.txt", "r") as file:
    lines = list(map(lambda x: x.strip("\n").split(","), file.readlines()))
    lines = [tuple([int(y) for y in x]) for x in lines]

    minx = min(i[0] for i in lines) - 1
    maxx = max(i[0] for i in lines) + 2
    miny = min(i[1] for i in lines) - 1
    maxy = max(i[1] for i in lines) + 2
    minz = min(i[2] for i in lines) - 1
    maxz = max(i[2] for i in lines) + 2

    water = set()
    tofill = [(minx, miny, minz)]
    while tofill:
        wx, wy, wz = tofill.pop()
        if (wx, wy, wz) in water or (wx, wy, wz) in lines:
            continue
        water.add((wx, wy, wz))
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            tx, ty, tz = wx+dx,wy+dy,wz+dz
            if minx <= tx < maxx and miny <= ty < maxy and minz <= tz < maxz:
                tofill.append((tx, ty, tz))

    n = 0
    for x,y,z in lines:
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if (x+dx,y+dy,z+dz) in water:
                n += 1
    print(n)