with open("./data.txt", "r") as file:
    lines = file.readlines()

    lines = list(map(lambda x: x.strip("\n"), lines))

    x = 1
    display_result = ""
    cycle = 0
    display_pointer = 1
    current_row = 0

    def update(comp_val, cycle, display_result, current_row):
        if (comp_val == cycle or cycle == comp_val-1 or cycle == comp_val + 1):
            display_result += "█"
        else:
            display_result += "."

        if (display_pointer % 40 == 0):
            current_row += 1
            display_result += "\n"
        
        return current_row, display_result

    def tick(x, cycle, current_row, display_pointer, display_result):
        comp_val = x + (40 * current_row)
        current_row, display_result = update(comp_val, cycle, display_result, current_row)
        cycle += 1
        display_pointer += 1

        return cycle, current_row, display_result, display_pointer

    for line in lines:
        tokens = line.split(" ")
        
        cycle, current_row, display_result, display_pointer = tick(x, cycle, current_row, display_pointer, display_result)
        
        if tokens[0] == "addx":
            new_value = int(tokens[1])
            cycle, current_row, display_result, display_pointer = tick(x, cycle, current_row, display_pointer, display_result)
            x += new_value
    
    print(display_result)
    