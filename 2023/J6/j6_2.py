import math
IN = open("j6_2.txt", "r").read().splitlines()

times = IN[0].split(":")[1].split(" ")
times = [ int(i) for i in filter(lambda x: x != "", times) ]
distances = IN[1].split(":")[1].split(" ")
distances = [ int(i) for i in filter(lambda x: x != "", distances) ]

print(times)
print(distances)

results = []
for duree_to_beat in range(len(times)):
    min = 0
    max = 0
    for time_holding in range(times[duree_to_beat]):
        if time_holding * (times[duree_to_beat] - time_holding) > distances[duree_to_beat]:
            min = time_holding
            break
    for time_holding in range(times[duree_to_beat], 0, -1):
        if time_holding * (times[duree_to_beat] - time_holding) > distances[duree_to_beat]:
            max = time_holding
            break

print(max-min + 1)