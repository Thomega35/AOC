IN = open("j8.txt", "r").read().splitlines()

LR = IN[0]
graph = {}

for instruction in IN[2:] :
    key, value = instruction.split(" = ")
    # print(key, value)
    graph[key] = value

key = "AAA"
nb_steps = 0


while True :
    if LR[nb_steps%len(LR)] == "L" :
        key = graph[key][1:4]
    else :
        key = graph[key][6:9]
    # print(key)
    nb_steps += 1
    if key == "ZZZ" :
        break

print(nb_steps)