IN = open("input.txt", "r").read().splitlines()
IN = [ x.split(" ") for x in IN]
forward = 0
depth = 0
aim = 0
for i in range(0,len(IN)) :
    if (IN[i][0] == "forward") :
        forward += int(IN[i][1])
        depth += int(IN[i][1])*aim
    elif (IN[i][0] == "down") :
        aim += int(IN[i][1])
    else :
        aim -= int(IN[i][1])
print(forward)
print(depth)
print(forward*depth)
#number = [int(x) for x in number]
#print(dir)
#print(number)
#[n, L] = Insplitint
#liste = []
#for i in range (n) :
#    liste.append(int(IN[i+1]))
#liste.sort
#print(liste)
#maisonmere = liste[int((len(liste)-1)/2)]
#somme = 0
#print("maisonmere" + str(maisonmere))
#for i in liste :
#    somme += abs(i - maisonmere)
#    print(somme)
#print(somme*2)
#IN2 = open(file + ".ans", "r").read().splitlines()
#print(IN2[0])
#calc = ((n1 + 1)*(n2 + 1)/(n12 + 1) -1)
#print(int(calc))
#IN2 = open(file + ".ans", "r").read().splitlines()
#print(IN2[0])