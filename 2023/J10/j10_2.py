IN = open('j10.txt', 'r').read().splitlines()
print(IN)
import re
MAP = [["."]*len(IN[0]) for i in range(len(IN))]

start = None
toBreak = False
for i in range(len(IN)):
    for j in range(len(IN[i])):
        if IN[i][j] == 'S':
            start = (i, j)
            # set i, j in map to S
            MAP[i][j] = 'S'
            toBreak = True
            break
    if toBreak:
        break

for line in MAP:
    print(line)

for line in IN:
    print(line)
start_top, start_left, start_bot, start_right = False, False, False, False
# match | or F or 7
if start[0] >= 1 and IN[start[0]-1][start[1]] in ['F', '7', '|']:
    start_top = True
    print(IN[start[0]-1][start[1]])
    print(re.search(IN[start[0]-1][start[1]], r'[L|J|\|]'))
# match | or L or J
if start[0] <= len(IN)-2 and IN[start[0]+1][start[1]] in ['L', 'J', '|']:
    start_bot = True
    print(IN[start[0]+1][start[1]])
# match - or F or L
if start[1] >= 1 and IN[start[0]][start[1]-1] in ['F', 'L', '-']:
    start_left = True
    print(IN[start[0]][start[1]-1])
# match - or 7 or J
if start[1] <= len(IN[0])-2 and IN[start[0]][start[1]+1] in ['7', 'J', '-']:
    start_right = True
    print(IN[start[0]][start[1]+1])
    
def setMap(start_x, start_y, lastDirection, BORDER):
    lenght = 1
    while IN[start_x][start_y] != 'S':
        if MAP[start_x][start_y] != ".":
            MAP[start_x][start_y] = min(lenght, MAP[start_x][start_y])
        else:
            MAP[start_x][start_y] = lenght
        if lastDirection == "UP":
            BORDER[start_x][start_y] = "B"
            if start_y <= len(IN[0])-2 and BORDER[start_x][start_y+1] != "B":
                BORDER[start_x][start_y+1] = "C"
            if IN[start_x][start_y] == "|":
                start_x -= 1
            elif IN[start_x][start_y] == "F":
                start_y += 1
                lastDirection = "RIGHT"
            elif IN[start_x][start_y] == "7":
                start_y -= 1
                lastDirection = "LEFT"
        elif lastDirection == "LEFT":
            BORDER[start_x][start_y] = "B"
            if start_x >= 1 and BORDER[start_x-1][start_y] != "B":
                BORDER[start_x-1][start_y] = "C"
            if IN[start_x][start_y] == "-":
                start_y -= 1
            elif IN[start_x][start_y] == "L":
                start_x -= 1
                lastDirection = "UP"
            elif IN[start_x][start_y] == "F":
                start_x += 1
                lastDirection = "DOWN"
        elif lastDirection == "RIGHT":
            BORDER[start_x][start_y] = "B"
            if start_x <= len(IN)-2 and BORDER[start_x+1][start_y] != "B":
                BORDER[start_x+1][start_y] = "C"
            if IN[start_x][start_y] == "-":
                start_y += 1
            elif IN[start_x][start_y] == "J":
                start_x -= 1
                lastDirection = "UP"
            elif IN[start_x][start_y] == "7":
                start_x += 1
                lastDirection = "DOWN"
        elif lastDirection == "DOWN":
            BORDER[start_x][start_y] = "B"
            if start_y >= 1 and BORDER[start_x][start_y-1] != "B":
                BORDER[start_x][start_y-1] = "C"
            if IN[start_x][start_y] == "|":
                start_x += 1
            elif IN[start_x][start_y] == "L":
                start_y += 1
                lastDirection = "RIGHT"
            elif IN[start_x][start_y] == "J":
                start_y -= 1
                lastDirection = "LEFT"
        lenght += 1

cur_x, cur_y = start[0], start[1]

BORDER1 = [["."]*len(IN[0]) for _ in range(len(IN))]
BORDER1[start[0]][start[1]] = "B"

BORDER2 = [["."]*len(IN[0]) for _ in range(len(IN))]
BORDER2[start[0]][start[1]] = "B"

BORDER3 = [["."]*len(IN[0]) for _ in range(len(IN))]
BORDER3[start[0]][start[1]] = "B"

BORDER4 = [["."]*len(IN[0]) for _ in range(len(IN))]
BORDER4[start[0]][start[1]] = "B"

print(start_top, start_bot, start_left, start_right)

if start_top :
    setMap(cur_x-1, cur_y, "UP", BORDER1)
    for line in MAP:
        print(line)
    print()
if start_bot :
    # BORDER = [["."]*len(IN[0]) for _ in range(len(IN))]
    # BORDER[start[0]][start[1]] = "B"
    setMap(cur_x+1, cur_y, "DOWN", BORDER2)
    for line in MAP:
        print(line)
    print()
if start_left :
    # BORDER = [["."]*len(IN[0]) for _ in range(len(IN))]
    # BORDER[start[0]][start[1]] = "B"
    setMap(cur_x, cur_y-1, "LEFT", BORDER3)
    for line in MAP:
        print(line)
    print()
if start_right :
    # BORDER = [["."]*len(IN[0]) for _ in range(len(IN))]
    # BORDER[start[0]][start[1]] = "B"
    setMap(cur_x, cur_y+1, "RIGHT", BORDER4)
    for line in MAP:
        print(line)
    print()

for line in BORDER1:
    print(line)
print()

for line in BORDER2:
    print(line)
print()

for line in BORDER3:
    print(line)
print()

for line in BORDER4:
    print(line)
print()

print(start_top, start_bot, start_left, start_right)

for border in [BORDER1, BORDER2, BORDER3, BORDER4]:
    try:
        isEnlarged = True
        while isEnlarged:
            isEnlarged = False
            for i in range(len(border)):
                for j in range(len(border[i])):
                    if border[i][j] == "C":
                        if border[i-1][j] == ".":
                            border[i-1][j] = "C"
                            isEnlarged = True
                        if border[i+1][j] == ".":
                            border[i+1][j] = "C"
                            isEnlarged = True
                        if border[i][j-1] == ".":
                            border[i][j-1] = "C"
                            isEnlarged = True
                        if border[i][j+1] == ".":
                            border[i][j+1] = "C"
                            isEnlarged = True

        nb_inside = 0
        for i in range(len(border)):
            for j in range(len(border[i])):
                if border[i][j] == "C":
                    nb_inside += 1

        if nb_inside != 0:
            for line in border:
                print(line)
            print(nb_inside)
    except:
        print()
    

# BORDER = [["."]*len(IN[0]) for i in range(len(IN))]
# for i in range(len(IN)):
#     for j in range(len(IN[i])):
#         if MAP[i][j] != ".":
#             BORDER[i][j] = IN[i][j]

# for line in BORDER:
#     print(line)

# print()

# for line in range(len(BORDER)):
#     if BORDER[line][0] == ".":
#         BORDER[line][0] = "O"
#     if BORDER[line][-1] == ".":
#         BORDER[line][-1] = "O"

# for line in range(len(BORDER[0])):
#     if BORDER[0][line] == ".":
#         BORDER[0][line] = "O"
#     if BORDER[-1][line] == ".":
#         BORDER[-1][line] = "O"

# for line in BORDER :
#     print(line)

# print()


# for line in BORDER :
#     print(line)
