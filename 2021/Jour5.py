import numpy as np
def maximum(listeIN):
    maxi = 0
    for point1,point2 in listeIN:
        xin,yin = [int(x) for x in point1.split(",")]
        xfin,yfin = [int(x) for x in point2.split(",")]
        if (maxi < max(xin,yin,yin,yfin)) :
            maxi = max(xin,yin,yin,yfin)
    return maxi

IN = open("./J5-input.txt", "r").read().splitlines()
IN = [x.split(" -> ") for x in IN]
print(maximum(IN))

tablo = np.full((991, 991), 0)
for point1,point2 in IN:
    xin,yin = [int(x) for x in point1.split(",")]
    xfin,yfin = [int(x) for x in point2.split(",")]

    #if (xin == xfin or yin == yfin) :
        #print(xin,yin,",",xfin,yfin)
    while(xin != xfin or yin != yfin) :
        tablo[xin][yin] +=1
        if (xin < xfin) :
            xin += 1
        if (xin > xfin) :
            xin -= 1
        if (yin < yfin) :
            yin += 1
        if (yin > yfin) :
            yin -= 1
    tablo[xfin][yfin] +=1
res = 0
for x in tablo :
    for y in x :
        if y >= 2 :
            res +=1

print(res)
