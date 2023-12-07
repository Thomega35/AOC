def findSum (IN) :
    sum = 0
    for i in range(0,len(IN)-3) :
        if ((IN[i] + IN[i+1] + IN[i+2] ) < (IN[i+1] + IN[i+2] + IN[i+3] )) :
            sum += 1
    return sum
IN = open("J1-input.txt", "r").read().splitlines()
for i in range(0,len(IN)) :
    if (IN[i] != '') :
        IN[i] = int(IN[i])
RES = []
sum = 0
for i in IN :
    if (i != '') :
        sum += i
    else :
        RES.append(sum)
        sum = 0
RES.sort()
# Print the sum of the 3 max values in RES
print(RES[-1] + RES[-2] + RES[-3])
# IN = [int(x) for x in IN]
#IN = list(filter(lambda x: x != [], IN))    #remove empty list
# print(findSum(IN))