with open ("./data.txt", "r") as file:
    pairs = file.readlines()
    total = 0
    for pair in pairs:
        pair_string = pair.strip("\n")
        split = pair_string.split(",")
        pairs = [x.split("-") for x in split]

        a1, a2 = [int(x) for x in pairs[0]]
        b1, b2 = [int(x) for x in pairs[1]]

        smallest_start = min(a1, b1)
        largest_end = max(a2, b2)

        if (smallest_start == a1 and largest_end == a2) or (smallest_start == b1 and largest_end == b2):
            total += 1
    
    print(total)
            