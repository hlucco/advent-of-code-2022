with open ("./data.txt", "r") as file:
    data = file.readlines()
    c_sum = 0
    totals = []
    for line in data:
        if line == "\n":
            totals.append(c_sum)
            c_sum = 0
        else:
            c_sum += int(line)

    print(sum(list(sorted(totals))[-3:]))