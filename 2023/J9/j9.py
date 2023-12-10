IN = open('j9.txt', 'r').read().splitlines()

def isAllZero(datas) :
    for data in datas :
        if data != 0 :
            return False
    return True

res = 0
for dataLine in IN :
    datas = dataLine.split()
    datas = [int(i) for i in datas]
    resTemp = datas[-1]

    print(datas, resTemp)
    while not isAllZero(datas) :
        newDatas = []
        for i in range(1, len(datas)) :
            newDatas.append(datas[i] - datas[i-1])

        datas = newDatas
        print(datas, resTemp)
        resTemp += datas[-1]
    
    res += resTemp

print(res)