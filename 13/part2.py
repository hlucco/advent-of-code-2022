from functools import cmp_to_key
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

    def compare_list(left, right):
        for i in range(len(left)):
            value = 0
            try:
                left_val, right_val = left[i], right[i]
                if type(left_val) == int and type(right_val) == int:
                    if left_val < right_val:
                        return -1
                    if left_val > right_val:
                        return 1

                if type(left_val) == list and type(right_val) == list:
                    value = compare_list(left_val, right_val)
                
                if (type(left_val) == int and type(right_val) == list):
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

    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets += [pair[0], pair[1]]
        
    sorted_packets = list(sorted(packets, key=cmp_to_key(lambda l, r: compare_list(l, r))))
    
    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))