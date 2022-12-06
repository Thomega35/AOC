import numpy as np
def getPriority (IN) :
    sum = 0
    for maxicommon in IN :
        toadd = 0
        # print(maxicommon)
        if ord(maxicommon) >= ord('a') :
            toadd = (ord(maxicommon) - ord('a'))+1
        else :
            toadd = (ord(maxicommon) - ord('A'))+1+26
        # print(toadd)
        sum += toadd
    return sum
IN = open("./input.txt", "r").read().splitlines()

listeBadge = []
for i in range(100) :
    index = i*3
    group = [IN[index], IN[index+1], IN[index+2]]
    badge = "".join(set(group[0]).intersection(group[1], group[2]))
    listeBadge.append(badge)

sum = 0
for badge in listeBadge :
    sum += getPriority(badge)
print(sum)