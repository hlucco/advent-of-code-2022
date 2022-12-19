class Rock:
    def __init__(self, string_rep):
        self.height = len(string_rep)
        self.width = len(string_rep[0])
        self.body = string_rep

def print_chamber(chamber):
    for row in range(len(chamber)-1, 0, -1):
        print(chamber[row])

def update_chamber(chamber, current_pos, current_rock):
    sx, sy = (current_pos[0] + current_rock.height - 1, current_pos[1])
    for i, row in enumerate(current_rock.body):
        for j, col in enumerate(row):
            cx, cy = sx - i, j + sy            
            cell_contents = chamber[cx][cy]
            if cell_contents == ".":
                chamber[cx][cy] = col
    
    return chamber

def get_rocks(path):
    with open(path, "r") as rock_file:
        rocks = []
        line = rock_file.readline()
        current_rock = []
        while(line):
            if (line != "\n"):
                current_rock.append([*line.strip("\n")])
            else:
                rocks.append(Rock(current_rock))
                current_rock = []
            line = rock_file.readline()
        rocks.append(Rock(current_rock))

    return rocks

def apply_jet(chamber, current_pos, current_rock, direction):
    possible = True
    if (direction == ">"):
        if (current_pos[1] + current_rock.width < len(chamber[0])):
            for row in range(current_pos[0], current_pos[0]+current_rock.height):
                col = current_pos[1] + current_rock.width
                c_cell = chamber[row][col]
                r_cell = current_rock.body[row - current_pos[0]][-1]
                if c_cell == "#" and r_cell == "#":
                    possible = False
                    
            if possible:
                current_pos = (current_pos[0], current_pos[1] + 1)
            
    if (direction == "<"):
        if (current_pos[1] - 1 >= 0):
            for row in range(current_pos[0], current_pos[0]+current_rock.height):
                col = current_pos[1]-1
                c_cell = chamber[row][col]
                r_cell = current_rock.body[row - current_pos[0]][-1]
                if c_cell == "#" and r_cell == "#":
                    possible = False
                    
            if possible:
                current_pos = (current_pos[0], current_pos[1] - 1)

    return current_pos

def fall_step(chamber, current_pos, current_rock):
    new_pos = (current_pos[0] - 1, current_pos[1])
    # print(current_pos)
    for c_cell, r_cell in zip(chamber[new_pos[0]][new_pos[1]:new_pos[1]+current_rock.width], current_rock.body[-1]):
        # print(c_cell, r_cell)
        if c_cell == "#" and r_cell == "#":
            return new_pos, False
    
    return new_pos, True

with open("./test.txt", "r") as file:
    input = [*file.read().strip("\n")]

    chamber = [["." for _ in range(7)] for _ in range(5000)]

    start_idx = 2
    current_highest = 1
    rock_count = 0
    input_pointer = 0
    rock_pointer = 0
    rocks = get_rocks("./rocks.txt")
    time = 0

    while(rock_count < 2023):
        current_pos = (current_highest + 3, start_idx)
        current_rock = rocks[rock_pointer]
        falling = True
        while(falling and current_pos[0] >= 1):
            if time % 2 == 0:
                # jet step
                # print("jet step", input[input_pointer], current_pos)
                current_pos = apply_jet(chamber, current_pos, current_rock, input[input_pointer])
                input_pointer = (input_pointer + 1) % len(input)
                # print(current_pos)
            else:
                # print("fall step")
                # fall step
                current_pos, falling = fall_step(chamber, current_pos, current_rock)

            time += 1
        
        chamber = update_chamber(chamber, (current_pos[0]+1, current_pos[1]), current_rock)
        # print("===================================")
        # print_chamber(chamber)
        current_highest = max(current_highest, current_pos[0] + 1 + current_rock.height)
        rock_count += 1
        rock_pointer = (rock_pointer + 1) % len(rocks)
    
    print_chamber(chamber)
    print(current_highest)