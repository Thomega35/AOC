IN = open('j14.txt', 'r').read().splitlines()

IN = [list(line) for line in IN]

isMoving = True
while isMoving:
    isMoving = False
    for row in range(len(IN)):
        rock_idexes = []
        for col in range(len(IN[row])):
            if IN[row][col] == 'O':
                rock_idexes.append(col)
        for rock in rock_idexes:
            if IN[row-1][rock] == '.' and row > 0:
                IN[row-1][rock] = 'O'
                IN[row][rock] = '.'
                isMoving = True
                
somme = 0
toAdd = 1
for index in range(len(IN)-1, -1, -1):
    for elem in IN[index] :
        somme += toAdd if elem == 'O' else 0
    toAdd += 1
                
for line in IN:
    print(line)
    
print(somme)