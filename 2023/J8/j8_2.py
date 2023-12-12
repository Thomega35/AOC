import math

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

start_size = len(keys)
modulo = [0] * start_size
modulo_start = [False] * start_size
modulo_founed = [False] * start_size
while not all(modulo_founed) :
    if LR[nb_steps%len(LR)] == "L" :
        for k in range(len(keys)) :
            keys[k] = graph[keys[k]][1:4]
    else :
        for k in range(len(keys)) :
            keys[k] = graph[keys[k]][6:9]

    for k in range(len(keys)) :
        if keys[k][2] == "Z" and not modulo_start[k] :
            modulo_start[k] = True
        elif keys[k][2] == "Z" and modulo_start[k] and not modulo_founed[k] :
            modulo[k] += 1
            modulo_founed[k] = True
        elif keys[k][2] != "Z" and modulo_start[k] and not modulo_founed[k] :
            modulo[k] += 1

    nb_steps += 1

print(modulo)
# print(lcm(modulo))
print(math.lcm(*modulo))