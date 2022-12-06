from collections import Counter

with open("data.txt", "r") as file:
    packet = file.read()
    for i in range(0, len(packet)-14):
        print(packet[i:i+14])
        counter = Counter(packet[i:i+14])
        if len(list(counter.keys())) == 14:
            print(i+14)
            break