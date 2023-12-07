import string
databrutenumber =open("J8-input.txt", "r").read().splitlines()
dataGaucheDroite = [string.split("|") for string in databrutenumber]
nb14778 = 0
for i in range(len(dataGaucheDroite)) :
    matrice = [[string.ascii_lowercase[i] for i in range (7)] for _ in range(9)]
    print(matrice)
    listeDroitewithSpace = dataGaucheDroite[i][1].split(" ")
    listeDroitewithoutSpace = list(filter(None, listeDroitewithSpace))
    nbres = [0,0,0,0]
    for number in range(len(listeDroitewithoutSpace)) :
        st = listeDroitewithoutSpace[number]
        if "a" in st and "c" in st and "e" in st and "d" in st and "g"in st and "f"in st and "b" in st :
            nbres[number] = 8
        elif "c" in st and "e" in st and "f" in st and "a" in st and "b"in st and "d" in st :
            nbres[number] = 9
        elif "c" in st and "d" in st and "f" in st and "g" in st and "e"in st and "b" in st :
            nbres[number] = 6
        elif "c" in st and "a" in st and "g" in st and "e" in st and "d"in st and "b" in st :
            nbres[number] = 0
        elif "c" in st and "d" in st and "f" in st and "b" in st and "e"in st :
            nbres[number] = 5
        elif "g" in st and "c" in st and "d" in st and "f" in st and "a"in st :
            nbres[number] = 2
        elif "f" in st and "b" in st and "c" in st and "a" in st and "d"in st :
            nbres[number] = 3
        elif len(st) == 4 :
            nbres[number] = 4
        elif len(st) == 3 :
            nbres[number] = 7
        elif len(st) == 2 :
            nbres[number] = 1
    #print(nbres)
print(nb14778)