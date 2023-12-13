IN = open("j11.txt", "r").read().splitlines()

spaced_vert = []

for row in IN :
    if not '#' in row :
        spaced_vert.append(list(elem.replace('.', 'X') for elem in row))
    else :
        spaced_vert.append(list(row))

spaced = [[] for _ in range(len(spaced_vert))]

for col_index in range(len(spaced_vert[0])) :
    to_extend = True
    for row_index in range(len(spaced_vert)) :
        if spaced_vert[row_index][col_index] == '#' :
            to_extend = False

    for row_index in range(len(spaced_vert)) :
        # spaced[row_index].append(spaced_vert[row_index][col_index])
        if not to_extend :
            spaced[row_index].append(spaced_vert[row_index][col_index])
        else :
            spaced[row_index].append('X')

stars = set()

for row in range(len(spaced)) :
    for col in range(len(spaced[row])) :
        if spaced[row][col] == '#' :
            stars.add((row, col))

sum = 0
nb_connections = 0

for star1 in stars :
    for star2 in stars :
        if star1 != star2 :
            dist = abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])
            for elem in range(min(star1[0], star2[0]), max(star1[0], star2[0])) :
                if spaced[elem][star1[1]] == 'X' :
                    dist += 999999
            for elem in range(min(star1[1], star2[1]), max(star1[1], star2[1])) :
                if spaced[star1[0]][elem] == 'X' :
                    dist += 999999
            # print(star1, star2, dist)
            sum += dist
            nb_connections += 1

# print("spaced_vert")
# for row in spaced_vert :
#     print(row)

print("spaced")
for row in spaced :
    print(row)

# print(stars)
print(sum//2, nb_connections//2)