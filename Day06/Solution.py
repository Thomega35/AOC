IN = open("./input.txt", "r").read().splitlines()
IN = IN[0]

packetSize = 14
for i in range(len(IN)) :
    packet = IN[i:i+packetSize]
    if len(packet) == len(set(packet)) :
        print(i+packetSize)
        break