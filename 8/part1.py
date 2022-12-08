with open ("./data.txt", "r") as file:
    lines = file.readlines()

    tree_grid = [(list(map(lambda x: int(x), [*line.strip("\n")]))) for line in lines]

    num_rows, num_cols = len(tree_grid), len(tree_grid[0])

    total = 0
    for i in range(num_rows):
        for j in range(num_cols):
            tree = tree_grid[i][j]

            pointer = i-1
            top_visible = True

            while (pointer >= 0 and top_visible):
                comp = tree_grid[pointer][j]
                if comp >= tree:
                    top_visible = False
                pointer -= 1
            
            pointer = i+1
            bottom_visible = True
            while (pointer < num_rows and bottom_visible):
                comp = tree_grid[pointer][j]
                if comp >= tree:
                    bottom_visible = False
                pointer += 1

            pointer = j-1
            left_visible = True
            while (pointer >= 0 and left_visible):
                comp = tree_grid[i][pointer]
                if comp >= tree:
                    left_visible = False
                pointer -= 1
            
            pointer = j+1
            right_visible = True
            while (pointer < num_cols and right_visible):
                comp = tree_grid[i][pointer]
                if comp >= tree:
                    right_visible = False
                pointer += 1

            if top_visible or bottom_visible or right_visible or left_visible:
                total += 1
    
    print(total)