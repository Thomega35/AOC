DumboOctopusGrid = open("J11-input.txt", "r").read().splitlines()
DumboOctopusGrid = [[int(octopus) for octopus in Row] for Row in DumboOctopusGrid] 

def increall (rowfonc,octopusfonc) :
    global nb_flashes
    rangey = range(-1,2) 

    if not (rowfonc > 0 and rowfonc < (len(DumboOctopusGrid)-1)) :
        rangey = range(-1,1) 
        if not (rowfonc > 0) :
            rangey = range(2)
    rangex = range(-1,2)

    if not (octopusfonc > 0 and octopusfonc < (len(DumboOctopusGrid[rowfonc])-1)) :
        rangex = range(-1,1)
        if not octopusfonc > 0 :
            rangex = range(2)
            
    for autoury in rangey:
        for autourx in rangex:
            print("oh", rowfonc + autoury,octopusfonc + autourx)
            DumboOctopusGrid[rowfonc+ autoury][octopusfonc+autourx] += 1
            if  DumboOctopusGrid[rowfonc+ autoury][octopusfonc+autourx] == 10 :
                print("ReFlashes")
                nb_flashes +=1
                increall(rowfonc+autoury, octopusfonc+autourx)

def all (dumbo) :
    first = dumbo[0][0]
    for rowfonc in range(len(dumbo)) :
        for octopusfonc in range(len(dumbo[rowfonc])) :
            if not dumbo[rowfonc][octopusfonc] == first :
                return False
    return True
nb_flashes = 0
step = 0
while not all(DumboOctopusGrid) :
    print("step :",step+1)
    for Row in range(len(DumboOctopusGrid)) :
        for octopus in range(len(DumboOctopusGrid[Row])) :
            DumboOctopusGrid[Row][octopus] += 1
            print("ck" , Row, octopus)
            if DumboOctopusGrid[Row][octopus] == 10 :
                print("Flashes")
                nb_flashes +=1
                increall(Row, octopus)

    for Row in range(len(DumboOctopusGrid)) :
        for octopus in range(len(DumboOctopusGrid[Row])) :
            if DumboOctopusGrid[Row][octopus] >= 10 :
                print("reset")
                DumboOctopusGrid[Row][octopus] = 0
    step +=1
print(DumboOctopusGrid)
print("nb_flashes =", nb_flashes)
print("step =", step)