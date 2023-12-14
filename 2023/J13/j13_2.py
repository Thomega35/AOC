IN = open("j13.txt", "r").read().splitlines()

board = []
resultat = 0

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


def getSum(mirror_temp, initSum):
    somme = 0
    for symetricAxe in range(1,len(mirror_temp)):
        isSymetricVertical = True
        for pointer in range(symetricAxe):

            if symetricAxe + pointer < len(mirror_temp) and symetricAxe - pointer > 0:
                if mirror_temp[symetricAxe - pointer - 1] != mirror_temp[symetricAxe + pointer]:
                    isSymetricVertical = False
                    break

        if isSymetricVertical and symetricAxe * 100 != initSum :
            somme += symetricAxe * 100
            break
        else:
            isSymetricVertical = False
    
    if isSymetricVertical:
        return somme

    for symetricAxe in range(1,len(mirror_temp[0])):
        isSymetricHorizontal = True
        for pointer in range(symetricAxe):

            if symetricAxe + pointer < len(mirror_temp[0]) and symetricAxe - pointer > 0:
                for line in mirror_temp:
                    if line[symetricAxe - pointer - 1] != line[symetricAxe + pointer]:
                        isSymetricHorizontal = False
                        break

        if isSymetricHorizontal and symetricAxe * 1 != initSum:
            somme += symetricAxe * 1
            break

    if isSymetricHorizontal :
        return somme
    # throw error
    return 0

for mirror in mirrors:

    initSum = getSum(mirror, 0)
    solution_found = False

    for smuge_place in range(len(mirror) * len(mirror[0])):

        mirror_copy = [elem.copy() for elem in mirror]
        if mirror_copy[smuge_place // len(mirror[0])][smuge_place % len(mirror[0])] == "#" :
            mirror_copy[smuge_place // len(mirror[0])][smuge_place % len(mirror[0])] = "."
        else:
            mirror_copy[smuge_place // len(mirror[0])][smuge_place % len(mirror[0])] = "#"

        nouvelle_somme = getSum(mirror_copy, initSum)
        if nouvelle_somme == 0:
            continue
        if nouvelle_somme != initSum:
            solution_found = True
            
            resultat += nouvelle_somme
            break
    if not solution_found:
        raise Exception("no solution found")
        
print(resultat)
