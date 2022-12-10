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

    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == "addx":
            new_value = int(tokens[1])

            comp_val = x + (40 * current_row)
            current_row, display_result = update(comp_val, cycle, display_result, current_row)
            cycle += 1
            display_pointer += 1

            comp_val = x + (40 * current_row)
            current_row, display_result = update(comp_val, cycle, display_result, current_row)
            cycle += 1
            display_pointer += 1
            
            x += new_value
        else:
            comp_val = x + (40 * current_row)
            current_row, display_result = update(comp_val, cycle, display_result, current_row)
            cycle += 1
            display_pointer += 1
    
    print(display_result)
    