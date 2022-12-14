with open("./data.txt", "r") as file:

    pairs = []
    current_pair = []
    line = file.readline()
    while(line):
        if (line != "\n"):
            current_pair.append(line)
        else:
            pairs.append(current_pair)
            current_pair = []
        line = file.readline()
    pairs.append(current_pair)

    pairs = list(map(lambda x: tuple(map(lambda y: eval(y.strip("\n")), x)), pairs))

    def sanity_check(left, right):
        if left == []:
            return 0 if right == [] else -1
        if right == []:
            return 1
        
        if (type(left) == list):
            if (type(right) == list):
                cmp = sanity_check(left[0], right[0])
                if cmp == 0:
                    return sanity_check(left[1:], right[1:])
                return cmp
            return sanity_check(left, [right])
        if (type(right) == list):
            return sanity_check([left], right)
        return -1 if left < right else 1 if right < left else 0

    def compare_list(left, right):
        for i in range(len(left)):
            value = 0
            try:
                left_val, right_val = left[i], right[i]
                if type(left_val) == int and type(right_val) == int:
                    # print("both int")
                    if left_val < right_val:
                        return -1
                    if left_val > right_val:
                        return 1

                if type(left_val) == list and type(right_val) == list:
                    # print("list, list")
                    value = compare_list(left_val, right_val)
                
                if (type(left_val) == int and type(right_val) == list):
                    # print("int, list")
                    value = compare_list([left_val], right_val)
                
                if (type(left_val) == list and type(right_val) == int):
                    value = compare_list(left_val, [right_val])

                if value != 0:
                    return value

            except IndexError:
                return 1
        
        if (len(left) < len(right)):
            return -1
        
        if (len(left) == len(right)):
            return 0

    total = 0
    for i, (left,right) in enumerate(pairs):
        result = compare_list(left, right) 
        sanity = sanity_check(left, right)
        if (result != sanity):
            print(left)
            print(right)
            print("result: ", result, sanity)
        if (result == -1 or result == 0):
            total += (i + 1)
    
    print(total)

    # 3029
