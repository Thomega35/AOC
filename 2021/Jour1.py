IN = open("./J1-input.txt", "r").read().splitlines()
IN = [int(x) for x in IN]
sum = 0
for i in range(0,len(IN)-3) :
    if ((IN[i] + IN[i+1] + IN[i+2] ) < (IN[i+1] + IN[i+2] + IN[i+3] )) :
        sum += 1
print(sum)