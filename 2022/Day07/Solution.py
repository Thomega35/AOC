class Directory :
    content = []
    parent = None
    name = ""
    def __init__(self, name, parent) :
        self.content = []
        self.name = name
        self.parent = parent
    
    def add(self, obj) :
        self.content.append(obj)

    def getDir(self, name) :
        for obj in self.content :
            if isinstance(obj, Directory) and obj.name == name :
                return obj
        return None
    
    def sum(self) :
        sum = 0
        for obj in self.content :
                sum += obj.sum()
        return sum

class File :
    size = 0
    def __init__(self, size) :
        self.size = size
    
    def sum(self) :
        return self.size


IN = open("./Day07/input.txt", "r").read().splitlines()
for i in range(len(IN)) :
    IN[i] = IN[i].split(" ")

IN = IN[1:]

i = 0
init = Directory("root", None)
current = init
done = False
while i < len(IN) and not done:
    if IN[i][0] == "$" and IN[i][1] == "ls" :
        if i < len(IN) :
            i += 1
        else :
            break
        while IN[i][0] != "$" :
            if IN[i][0] == "dir" :
                current.add(Directory(IN[i][1], current))
            else :
                current.add(File(int(IN[i][0])))
            if i < len(IN)-1 :
                i += 1
            else :
                done = True
                break
    elif IN[i][0] == "$" and IN[i][1] == "cd" and IN[i][2] == ".." :
        current = current.parent
        if i < len(IN) :
            i += 1
        else :
            break
    elif IN[i][0] == "$" and IN[i][1] == "cd" :
        current = current.getDir(IN[i][2])
        if i < len(IN) :
            i += 1
        else :
            break

ResSmall = []
# Add dir to res if sum(dir) < 100000
def addSmallDir(dir) :
    if dir.sum() < 100000 :
        ResSmall.append(dir)

# Go through all dirs and add them to res
def goThroughSmallVersion(dir) :
    for obj in dir.content :
        if isinstance(obj, Directory) :
            addSmallDir(obj)
            goThroughSmallVersion(obj)

goThroughSmallVersion(init)
MaxiSum = 0
for dir in ResSmall :
    MaxiSum += dir.sum()

print(MaxiSum)

# Part 2

spaceToFree = 70000000 - init.sum() 
spaceToFree = 30000000 - spaceToFree

ResBig = []
# Add dir to res if sum(dir) > spaceToFree
def addBigDir(dir) :
    if dir.sum() >= spaceToFree :
        ResBig.append(dir)

# Go through all dirs and add them to res
def goThroughBigVersion(dir) :
    for obj in dir.content :
        if isinstance(obj, Directory) :
            addBigDir(obj)
            goThroughBigVersion(obj)

goThroughBigVersion(init)

print(min(ResBig, key=lambda x: x.sum()).sum())