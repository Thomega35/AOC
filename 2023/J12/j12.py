IN = open("j12.txt", "r").read().splitlines()

nb_solutions = 0

# Example : 
# Path : ...#...##...##...
# Expected to find : 1,2,2 
def is_path_valid(path, expected_to_find):
    for number_to_find in expected_to_find:
        if path.find("#") == -1 :
            return False
        first_hash_index = path.find("#")
        path = path[first_hash_index:]
        nb_hash = 0
        for i in range(len(path)):
            if path[i] == "#":
                nb_hash += 1
            else:
                break
        if nb_hash != number_to_find:
            return False
        else:
            path = path[nb_hash:]
    if path.find("#") >= 1:
        return False
    return True

def make_paths(path_blured, indexs_of_blur):
    if indexs_of_blur == []:
        return [path_blured]
    path1 = path_blured
    path2 = path_blured
    return make_paths(path1.replace("?", "#", 1), indexs_of_blur[1:].copy()) + make_paths(path2.replace("?", ".", 1), indexs_of_blur[1:].copy())

for i in range(len(IN)):
    map_onsen, expected_to_find = IN[i].split(" ")
    expected_to_find = [int(x) for x in expected_to_find.split(",")]
    print(map_onsen, expected_to_find)

    indexs = []
    for j in range(len(map_onsen)):
        if map_onsen[j] == "?":
            indexs.append(j)

    paths = make_paths(map_onsen, indexs)
    for path in paths:
        if is_path_valid(path, expected_to_find):
            nb_solutions += 1
            print(path, expected_to_find)
            
print(nb_solutions)