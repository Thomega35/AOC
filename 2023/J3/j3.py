class PartNumber :
    def __init__(self, value, begx, begy, endx, endy):
        self.value = value
        self.begx = begx
        self.begy = begy
        self.endx = endx
        self.endy = endy

    def __str__(self):
        return str(self.value) + " " + str(self.begx) + " " + str(self.begy) + " " + str(self.endx) + " " + str(self.endy)

SHEME = open("j3.txt", "r").read().splitlines()
NB_SHEME = SHEME.copy()

PART_LIST = []
sum = 0

# replace all non digit by a space
for row in range(len(NB_SHEME)):
    for case in range(len(NB_SHEME[row])):
        if not NB_SHEME[row][case].isdigit():
            NB_SHEME[row] = NB_SHEME[row].replace(NB_SHEME[row][case], " ")

beg = False
begx = 0
begy = 0
for row in range(len(NB_SHEME)):
    for case in range(len(NB_SHEME[row])):
        if NB_SHEME[row][case].isdigit():
            if not beg:
                begx = case
                begy = row
                if len(NB_SHEME[row]) == case+1 or NB_SHEME[row][case+1] == " ":
                    PART_LIST.append(PartNumber(int(NB_SHEME[row][begx:case+1]), begx, begy, case, row))
                else:
                    beg = True
            else:
                if len(NB_SHEME[row]) == case+1 or NB_SHEME[row][case+1] == " ":
                    PART_LIST.append(PartNumber(int(NB_SHEME[row][begx:case+1]), begx, begy, case, row))
                    beg = False
                    begx = 0
                    begy = 0

# for part in PART_LIST:
#     print(part)

for part in PART_LIST:
    # Check if there is a symbol around the number
    toAdd = False
    for check_y in range(part.begy-1, part.endy+2):
        if not (check_y < 0 or check_y >= len(SHEME)):
            for check_x in range(part.begx-1, part.endx+2):
                if not (check_x < 0 or check_x >= len(SHEME[check_y])):
                    if not (check_y == part.begy and ( check_x >= part.begx and check_x <= part.endx)) :
                        if not (SHEME[check_y][check_x].isdigit() or SHEME[check_y][check_x] == "."):
                            toAdd = True
                            break
        if toAdd:
            break
    if toAdd:
        sum += part.value

print(sum)