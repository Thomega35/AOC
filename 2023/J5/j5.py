IN = open("j5t.txt", "r").read().splitlines()
seeds = IN[0].split(":")[1]
seeds = seeds[1:len(seeds)].split(" ")
IN = IN[2:len(IN)]

dicts = [{}]
dicts_txt = [[]]
index = 0
for line in IN : 
    if line == "" : 
        index += 1
        dicts_txt.append([])
        dicts.append({})
    else :
        dicts_txt[index].append(line)

print("dicts_txt processed")

# without first line
for dict_index in range(0, len(dicts_txt)):
    for elem in dicts_txt[dict_index][1:len(dicts_txt[dict_index])]:
        elem = elem.split(" ")
        # for i in range(int(elem[2])) :
        #     dicts[dict_index][int(elem[1])+i] = int(elem[0]) + i
        # dicts[dict_index].append(xrange(int(elem[1]), int(elem[2])+int(elem[1])))
        dicts[dict_index][range(int(elem[1]), int(elem[2])+int(elem[1]))] = int(elem[0]) - int(elem[1])

print("dict processed")
    
locations = []
for seed in seeds:
    location = int(seed)
    for dict in dicts:
        for range, value in dict.items():
            if location in range:
                location = value + location
                break
    locations.append(location)
    
# print(dicts_txt)
# print(seeds)
print(locations)
print(min(locations))
# print(dicts)