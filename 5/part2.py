with open("./data.txt",  "r") as file:
    init_state = []
    c_line = file.readline()
    while(c_line != "\n"):
        init_state.append(c_line)
        c_line = file.readline()

    init_state.reverse()
    crane_state = {int(x): [] for x in init_state[0] if x != " " and x != "\n"}

    for row in init_state[1:]:
        for count, i in enumerate(range(1, len(row), 4)):
            if row[i] != " ":
                crane_state[count+1].append(row[i])
        count+=1
    
    while(c_line):
        c_line = file.readline()
        if c_line:
            tokens = c_line.split(" ")
            num_to_mov, source, dest = int(tokens[1]), int(tokens[3]), int(tokens[5])
            temp = crane_state[source][-num_to_mov:]
            del crane_state[source][-num_to_mov:]
            crane_state[dest] += temp
    
    result = ""
    for key in crane_state:
        result += crane_state[key][-1]

    print(result)