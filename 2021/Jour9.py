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
print(listminiloc)