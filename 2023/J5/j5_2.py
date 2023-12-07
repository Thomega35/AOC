import numpy as np

IN = open("j5.txt", "r").read().splitlines()
seeds = IN[0].split(":")[1]
seeds = seeds[1:len(seeds)].split(" ")
IN = IN[2:len(IN)]

new_seeds = []
for index in range(0, len(seeds)//2):
    new_seeds.append((int(seeds[index*2]), int(seeds[index*2+1])+1))
    index += 1

seeds = new_seeds

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
seeds_res = np.zeros(51045248379, bool)
for seed_range in seeds:
    print(seed_range)
    seeds_res[seed_range[0]:seed_range[0]+seed_range[1]] = True
    
estRentre = False
for index, seed in enumerate(seeds_res):
    if index % 1000000 == 0:
        print(index, "/", len(seeds_res), estRentre)
    if seed:
        estRentre = True
        location = int(index)
        for dict in dicts:
            for ranges, value in dict.items():
                if location in ranges:
                    location = value + location
                    break
        locations.append(location)

print(min(locations))