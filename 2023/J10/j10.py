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
if start[0] >= 1 and re.search(r'[F|7|\|]', IN[start[0]-1][start[1]]):
    start_top = True
    print(IN[start[0]-1][start[1]])
    print(re.search(IN[start[0]-1][start[1]], r'[L|J|\|]'))
# match | or L or J
if start[0] <= len(IN)-2 and re.search(r'[L|J|\|]', IN[start[0]+1][start[1]]):
    start_bot = True
    print(IN[start[0]+1][start[1]])
# match - or F or L
if start[1] >= 1 and re.search(r'[F|L|\-]', IN[start[0]][start[1]-1]):
    start_left = True
    print(IN[start[0]][start[1]-1])
# match - or 7 or J
if start[1] <= len(IN[0])-2 and re.search(r'[7|J|\-]', IN[start[0]][start[1]+1]):
    start_right = True
    print(IN[start[0]][start[1]+1])
    
def setMap(start_x, start_y, lastDirection):
    lenght = 1
    while IN[start_x][start_y] != 'S':
        if MAP[start_x][start_y] != ".":
            if MAP[start_x][start_y] != "S":
                MAP[start_x][start_y] = min(lenght, MAP[start_x][start_y])
        else:
            MAP[start_x][start_y] = lenght
        if lastDirection == "UP":
            if IN[start_x][start_y] == "|":
                start_x -= 1
            elif IN[start_x][start_y] == "F":
                start_y += 1
                lastDirection = "RIGHT"
            elif IN[start_x][start_y] == "7":
                start_y -= 1
                lastDirection = "LEFT"
        elif lastDirection == "LEFT":
            if IN[start_x][start_y] == "-":
                start_y -= 1
            elif IN[start_x][start_y] == "L":
                start_x -= 1
                lastDirection = "UP"
            elif IN[start_x][start_y] == "F":
                start_x += 1
                lastDirection = "DOWN"
        elif lastDirection == "RIGHT":
            if IN[start_x][start_y] == "-":
                start_y += 1
            elif IN[start_x][start_y] == "J":
                start_x -= 1
                lastDirection = "UP"
            elif IN[start_x][start_y] == "7":
                start_x += 1
                lastDirection = "DOWN"
        elif lastDirection == "DOWN":
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
print(start_top, start_bot, start_left, start_right)
if start_top :
    setMap(cur_x-1, cur_y, "UP")
    for line in MAP:
        print(line)
    print()
if start_bot :
    setMap(cur_x+1, cur_y, "DOWN")
    for line in MAP:
        print(line)
    print()
if start_left :
    setMap(cur_x, cur_y-1, "LEFT")
    for line in MAP:
        print(line)
    print()
if start_right :
    setMap(cur_x, cur_y+1, "RIGHT")
    for line in MAP:
        print(line)
    print()

# get max value in MAP
max_value = 0
for line in MAP:
    for item in line:
        if item != "." and item != "S":
            max_value = max(max_value, item)
print(max_value)