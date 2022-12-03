with open ("./data.txt", "r") as file:
    guide = file.readlines()

    mappings = {
        "A" : {
            "X" : 3+0,
            "Y" : 1+3,
            "Z" : 2+6
        },
        "B" : {
            "X" : 1 + 0,
            "Y" : 2 + 3,
            "Z" : 3 + 6,
        },
        "C" : {
            "X" : 0 + 2,
            "Y" : 3 + 3,
            "Z" : 1 + 6
        }
    }

    play_mapping = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }
    
    total_score = 0
    for game in guide:
        chars = game.strip("\n").split(" ")
        round_score = (mappings[chars[0]][chars[1]])
        print(round_score)
        total_score += round_score
    
    print(total_score)