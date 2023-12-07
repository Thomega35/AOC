IN = open("./input.txt", "r").read().splitlines()
IN = [i.split(" ") for i in IN]

for i in range(0,len(IN)) :
    if (IN[i][0] == 'A' and IN[i][1] == 'X') : # Pierre Loose
        IN[i][1]= 'Z'
    elif (IN[i][0] == 'A' and IN[i][1] == 'Y') : # Pierre Draw
        IN[i][1]= 'X'
    elif (IN[i][0] == 'A' and IN[i][1] == 'Z') : # Pierre Win
        IN[i][1]= 'Y'
    elif (IN[i][0] == 'B' and IN[i][1] == 'X') : # Feuille Loose
        IN[i][1]= 'X'
    elif (IN[i][0] == 'B' and IN[i][1] == 'Y') : # Feuille Draw
        IN[i][1]= 'Y'
    elif (IN[i][0] == 'B' and IN[i][1] == 'Z') : # Feuille Win
        IN[i][1]= 'Z'
    elif (IN[i][0] == 'C' and IN[i][1] == 'X') : # Ciseaux Loose 
        IN[i][1]= 'Y'
    elif (IN[i][0] == 'C' and IN[i][1] == 'Y') : # Ciseaux Draw 
        IN[i][1]= 'Z'
    elif (IN[i][0] == 'C' and IN[i][1] == 'Z') : # Ciseaux Win
        IN[i][1]= 'X'
    else :
        print("Error")




sum = 0
for i in range(0,len(IN)) :
    if (IN[i][0] == 'A' and IN[i][1] == 'X') : # Pierre Pierre
        sum += 1+3
    elif (IN[i][0] == 'A' and IN[i][1] == 'Y') : # Pierre Feuille
        sum += 2+6
    elif (IN[i][0] == 'A' and IN[i][1] == 'Z') : # Pierre Ciseaux
        sum += 3+0
    elif (IN[i][0] == 'B' and IN[i][1] == 'X') : # Feuille Pierre
        sum += 1+0
    elif (IN[i][0] == 'B' and IN[i][1] == 'Y') : # Feuille Feuille
        sum += 2+3
    elif (IN[i][0] == 'B' and IN[i][1] == 'Z') : # Feuille Ciseaux
        sum += 3+6
    elif (IN[i][0] == 'C' and IN[i][1] == 'X') : # Ciseaux Pierre 
        sum += 1+6
    elif (IN[i][0] == 'C' and IN[i][1] == 'Y') : # Ciseaux Feuille 
        sum += 2+0
    elif (IN[i][0] == 'C' and IN[i][1] == 'Z') : # Ciseaux Ciseaux
        sum += 3+3
    else :
        print("Error")
    print(len(IN))


print(sum)