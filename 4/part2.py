with open ("./data.txt", "r") as file:
    pairs = file.readlines()
    total = 0
    for pair in pairs:
        pair_string = pair.strip("\n")
        split = pair_string.split(",")
        pairs = [x.split("-") for x in split]

        a1, a2 = [int(x) for x in pairs[0]]
        b1, b2 = [int(x) for x in pairs[1]]

        if not (
            (a1 < b1 and a2 < b1) or 
            (a1 > b2 and a2 > b2) or
            (b1 < a1 and b2 < a1) or
            (b1 > a2 and b2 > a2)):
            total += 1
    
    print(total)
            