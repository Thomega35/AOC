def isContainingTheOther (tuple1, tuple2) :
    if (tuple1[0] >= tuple2[0] and tuple1[1] <= tuple2[1]) or (tuple1[0] <= tuple2[0] and tuple1[1] >= tuple2[1]) : 
        return True
    return False

def isOverlapping (tuple1, tuple2) :
    if (tuple1[1] >= tuple2[0] and tuple1[1] <= tuple2[1]) or (tuple1[0] >= tuple2[0] and tuple1[0] <= tuple2[1]) :
        return True
    return False

IN = open("./input.txt", "r").read().splitlines()
IN = [i.split("-") for i in IN]
for i in range(len(IN)) :
    IN[i] = int(IN[i][0]),int(IN[i][1].split(",")[0]),int(IN[i][1].split(",")[1]),int(IN[i][2])

sum = 0
for i in IN :
    if (isContainingTheOther((i[0],i[1]),(i[2],i[3]))) :
        sum += 1

nboverlap = 0
for i in IN:
    if (isOverlapping((i[0],i[1]),(i[2],i[3])) or isContainingTheOther((i[0],i[1]),(i[2],i[3]))) :
        nboverlap += 1

print(sum)
print(nboverlap)
