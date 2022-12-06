# [Q]         [N]             [N]    
# [H]     [B] [D]             [S] [M]
# [C]     [Q] [J]         [V] [Q] [D]
# [T]     [S] [Z] [F]     [J] [J] [W]
# [N] [G] [T] [S] [V]     [B] [C] [C]
# [S] [B] [R] [W] [D] [J] [Q] [R] [Q]
# [V] [D] [W] [G] [P] [W] [N] [T] [S]
# [B] [W] [F] [L] [M] [F] [L] [G] [J]
#  1   2   3   4   5   6   7   8   9 
Crane = [["Q","H","C","T","N","S","V","B"],["G","B","D","W"],["B","Q","S","T","R","W","F"],["N","D","J","Z","S","W","G","L"],["F","V","D","P","M"],["J","W","F"],["V","J","B","Q","N","L"],["N","S","Q","J","C","R","T","G"],["M","D","W","C","Q","S","J"]]
Crane2 = [["Q","H","C","T","N","S","V","B"],["G","B","D","W"],["B","Q","S","T","R","W","F"],["N","D","J","Z","S","W","G","L"],["F","V","D","P","M"],["J","W","F"],["V","J","B","Q","N","L"],["N","S","Q","J","C","R","T","G"],["M","D","W","C","Q","S","J"]]

IN = open("./input.txt", "r").read().splitlines()

instructions = []
for index in range(len(IN)):
    instruction = IN[index].split(" ")
    instructionNB = [int(instruction[1]), int(instruction[3]), int(instruction[5])]
    instructions.append(instructionNB)

# CrateMover 9000
for todo in instructions :
    for index in range(todo[0]) :
        Crane[todo[2]-1] = [(Crane[todo[1]-1].pop(0))] + Crane[todo[2]-1]

# CrateMover 9001
for todo in instructions :
    toadd = []
    for index in range(todo[0]) :
        toadd.append(Crane2[todo[1]-1].pop(0))
    Crane2[todo[2]-1] = toadd + Crane2[todo[2]-1]

for list in Crane :
    print(list[0], end="")
print()

for list in Crane2 :
    print(list[0], end="")
print()
