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
    lasts = [datas[0]]

    print(datas)
    while not isAllZero(datas) :
        newDatas = []
        for i in range(1, len(datas)) :
            newDatas.append(datas[i] - datas[i-1])

        datas = newDatas
        lasts.append(datas[0])
    # datas[-1]

    print(lasts)
    current = 0
    for last in reversed(lasts) :
        current = last - current
        print(current)

    res += current

print(res)