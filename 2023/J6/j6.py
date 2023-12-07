import math
IN = open("j6.txt", "r").read().splitlines()

times = IN[0].split(":")[1].split(" ")
times = [ int(i) for i in filter(lambda x: x != "", times) ]
distances = IN[1].split(":")[1].split(" ")
distances = [ int(i) for i in filter(lambda x: x != "", distances) ]

print(times)
print(distances)

results = []
for duree_to_beat in range(len(times)):
    local_answers = []
    for time_holding in range(times[duree_to_beat]):
        if time_holding * (times[duree_to_beat] - time_holding) > distances[duree_to_beat]:
            local_answers.append(time_holding)
    results.append(len(local_answers))
print(results)
print(math.prod(results))