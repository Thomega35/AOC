IN = open("./J3-input.txt", "r").read().splitlines()
#IN = [int(x) for x in IN]
nbfinalup = ""
nbfinaldown = ""
for k in range(0,12) :
    if len(IN) == 1:
        break;
    TAB = [[],[]]
    nb0 = 0
    nb1 = 0
    for i in range(0,len(IN)) :
        if IN[i][k] == "0":
            nb0 += 1
            TAB[0].append(IN[i])
        else :
            nb1 += 1
            TAB[1].append(IN[i])
    if nb1<nb0 :
        IN = TAB[1]
    else :
        IN = TAB[0]
print(int(IN[0],2))
nbfinaldown = "100000111000"
nbfinalup = "011111101111"
nbfinal = int(nbfinaldown,2) * int(nbfinalup,2)
print('nbfd = ' + str(int(nbfinaldown,2)) + '\nnbfup = ' + str(int(nbfinalup,2)) + '\nnbf = ' + str(nbfinal))