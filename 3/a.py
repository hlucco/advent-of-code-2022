from collections import Counter

with open ("./data.txt", "r") as file:
    data = file.readlines()

    total_prio = 0
    for i in range(0, len(data), 3):
        rucksacks = data[i:i+3]

        first_comp = rucksacks[0].strip("\n")
        second_comp = rucksacks[1].strip("\n")
        third_comp = rucksacks[2].strip("\n")

        first_count = Counter(first_comp)        
        second_count = Counter(second_comp)
        third_count = Counter(third_comp)

        # print(first_comp, second_comp)
        # print(first_count, second_count, third_count)

        total_rucksack_prio = 0
        for key in first_count:
            if key in second_count and key in third_count:
                total_rucksack_prio = ord(key) - 96
                if total_rucksack_prio < 0:
                    total_rucksack_prio = (total_rucksack_prio + 58)

                    print(key, total_rucksack_prio)
        
        total_prio += total_rucksack_prio
    print(total_prio)