IN = open("j8.txt", "r").read().splitlines()

LR = IN[0]
graph = {}

for instruction in IN[2:] :
    key, value = instruction.split(" = ")
    # print(key, value)
    graph[key] = value

keys = []
for k in graph.keys() :
    if k[2] == "A" :
        keys.append(k)
print(keys)
nb_steps = 0


while True :
    if LR[nb_steps%len(LR)] == "L" :
        for k in range(len(keys)) :
            keys[k] = graph[keys[k]][1:4]
    else :
        for k in range(len(keys)) :
            keys[k] = graph[keys[k]][6:9]

    nb_steps += 1
    to_break = True
    for k in keys :
        if k[2] != "Z" :
            to_break = False

    nb_z = 0
    for k in keys :
        if k[2] == "Z" :
            nb_z += 1

    if nb_z > 1 :
        print(keys, nb_steps)

    if to_break :
        break

print(nb_steps)