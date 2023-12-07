import numpy as np
Order = open("2015/J6-input.txt", "r").read().splitlines()
Order = [instruction.split() for instruction in Order]
grid = np.zeros((1000,1000))
for instruction in Order :
    if (instruction[0] + instruction[1]) == "turnon" :
        [xin,yin] = [int(x) for x in instruction[2].split(",")]
        [xout,yout] = [int(x) for x in instruction[4].split(",")]
        for x in range(min(xin,xout),max(xin,xout)+1) :
            for y in range(min(yin,yout),max(yin,yout)+1) :
                grid[x,y] += 1
    elif (instruction[0] + instruction[1]) == "turnoff" :
        [xin,yin] = [int(x) for x in instruction[2].split(",")]
        [xout,yout] = [int(x) for x in instruction[4].split(",")]
        for x in range(min(xin,xout),max(xin,xout)+1) :
            for y in range(min(yin,yout),max(yin,yout)+1) :
                if grid[x,y] > 0 :
                    grid[x,y] -= 1
    else :
        [xin,yin] = [int(x) for x in instruction[1].split(",")]
        [xout,yout] = [int(x) for x in instruction[3].split(",")]
        for x in range(min(xin,xout),max(xin,xout)+1) :
            for y in range(min(yin,yout),max(yin,yout)+1) :
                grid[x,y] = (grid[x,y] + 2)

print(grid)
nbmaison = 0    
for colonnes in grid :
    nbmaison += sum(colonnes)
print(nbmaison)