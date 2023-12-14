IN = open("j13.txt", "r").read().splitlines()

board = []
somme = 0

for line in IN:
    board.append(list(line))

board.append([])
mirrors = [[]]
index = 0

for line in range(len(board)):
    if board[line] != []:
        mirrors[index].append(board[line])
    else:
        index+=1
        mirrors.append([])

mirrors.pop( len(mirrors) - 1 )

for mirror in mirrors:
    # for line in mirror:
    #     print(line)

    for symetricAxe in range(1,len(mirror)):
        isSymetricVertical = True
        for pointer in range(symetricAxe):
            # print(symetricAxe, symetricAxe + pointer, pointer)
            if symetricAxe + pointer < len(mirror) and symetricAxe - pointer > 0:
                if mirror[symetricAxe - pointer - 1] != mirror[symetricAxe + pointer]:
                    # print("vert break", mirror[symetricAxe - pointer - 1],mirror[symetricAxe + pointer])
                    isSymetricVertical = False
                    break
        if isSymetricVertical:
            somme += symetricAxe * 100
            print("vert", somme)
            break
    
    if isSymetricVertical:
        continue

    for symetricAxe in range(1,len(mirror[0])):
        isSymetricHorizontal = True
        for pointer in range(symetricAxe):
            # print(symetricAxe, symetricAxe + pointer, pointer)
            if symetricAxe + pointer < len(mirror[0]) and symetricAxe - pointer > 0:
                for line in mirror:
                    if line[symetricAxe - pointer - 1] != line[symetricAxe + pointer]:
                        isSymetricHorizontal = False
                        # print("hor break", line[symetricAxe - pointer - 1],line[symetricAxe + pointer])
                        break
                    # else:
                        # print(line[symetricAxe - pointer - 1],line[symetricAxe + pointer], end="/")
        if isSymetricHorizontal:
            somme += symetricAxe * 1
            print("hor", somme)
            break
    
    # print("split", somme)
        
print(somme)
