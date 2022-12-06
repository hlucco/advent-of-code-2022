from collections import Counter

with open("data.txt", "r") as file:
    packet = file.read()
    for i in range(0, len(packet)-4):
        print(packet[i:i+4])
        counter = Counter(packet[i:i+4])
        if len(list(counter.keys())) == 4:
            print(i+4)
            break
