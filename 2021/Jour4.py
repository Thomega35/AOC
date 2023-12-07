import numpy

def checkwin(liste):
    boole = False
    somme = 0
    for i in range(len(liste)) :
        for j in range(len(liste[i])) :
            if liste[i][j][1] == False :
                somme += liste[i][j][0]
    #check x
    for i in liste :
        tempboule = True
        for j in i :
            if j[1] == False :
                tempboule = False
        if tempboule == True :
            boole = True

    #check y
    for i in range(5) :
        tempboule = True
        for j in range(5) :
            if liste[j][i][1] == False :
                tempboule = False
        if tempboule == True :
            boole = True
    return (boole,somme)

IN = open("J4input.txt", "r").read().splitlines()
IN = [ x.split() for x in IN]
IN = list(filter(lambda x: x != [], IN))    #remove empty list

IN = [[int(i) for i in IN[0][0].split(",")]] + [[(int(j),False) for j in i] for i in IN if i != IN[0]]

#print(IN)
solved = numpy.zeros((100), dtype=bool)

for x in IN[0] :
    for i in range(1,len(IN)) :
        for j in range(len(IN[i])) :
            if (IN[i][j][0] == x) :
                IN[i][j] = (IN[i][j][0],True);
                [boole, somme] = checkwin(IN[i-((i-1)%5):i+ (5-((i-1)%5))])
                if boole :
                    solved[int((i-1)/5)] = True
                    print(int((i-1)/5))
                    if (all(solved)) :
                        print(IN[i-((i-1)%5):i+ (5-((i-1)%5))])
                        print("x = " + str(x))
                        print("somme = " + str(somme))
                        print ("multiply = " + str(x*somme))
                        break
        else :
            continue
        break
    else :
        continue
    break
print(solved)