lavaMap = open("J9-input.txt").read().splitlines()


lavaMap = [[int(lavatube) for lavatube in lavaRow] for lavaRow in lavaMap]


listminiloc = []



for Row in range(len(lavaMap)) :


    for tube in range(len(lavaMap[Row])) :



        minLeft  =  tube < 1                    or (lavaMap[Row][tube-1] > lavaMap[Row][tube])


        minRight = tube>=len(lavaMap[Row])-1    or (lavaMap[Row][tube+1] > lavaMap[Row][tube])


        minDown  = Row>=len(lavaMap)-1          or (lavaMap[Row+1][tube] > lavaMap[Row][tube])


        minUp    = Row < 1                      or (lavaMap[Row-1][tube] > lavaMap[Row][tube])



        if minLeft and minRight and minDown and minUp :


            listminiloc.append([Row,tube])
            


def zonesize(row, tube) :



    Left  = (zonesize(row, tube-1) if ((tube > 0)                 and ((row,tube-1) not in listcheck) and (lavaMap[row][tube-1] > lavaMap[row][tube]) and lavaMap[row][tube-1] != 9) else 0)


    Right = (zonesize(row, tube+1) if ((tube<len(lavaMap[row])-1) and ((row,tube+1) not in listcheck) and (lavaMap[row][tube+1] > lavaMap[row][tube]) and lavaMap[row][tube+1] != 9) else 0)


    Down  = (zonesize(row+1, tube) if ((row<len(lavaMap)-1)       and ((row+1,tube) not in listcheck) and (lavaMap[row+1][tube] > lavaMap[row][tube]) and lavaMap[row+1][tube] != 9) else 0) 


    Up    = (zonesize(row-1, tube) if ((row > 0)                  and ((row-1,tube) not in listcheck) and (lavaMap[row-1][tube] > lavaMap[row][tube]) and lavaMap[row-1][tube] != 9) else 0)


    listcheck.add((row,tube))



    return (1 if lavaMap[row][tube]!=9 else 0) +  Left  +  Right  +  Up  +  Down 



ZoneSize = [0,0,0]


for [miniR,miniT] in listminiloc :


    ZoneSize.sort()


    listcheck = set()


    ZoneActual = zonesize(miniR, miniT)


    if ZoneActual > ZoneSize[0] :


        ZoneSize[0] = ZoneActual


    print(ZoneActual)


print(ZoneSize, "=", ZoneSize[0]*ZoneSize[1]*ZoneSize[2])