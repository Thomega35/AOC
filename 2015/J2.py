TailleKdoString = open("2015/J2-input.txt", "r").read().splitlines()
TailleKdoInt = [[int(dimension) for dimension in kdo.split("x")] for kdo in TailleKdoString]
SizeOfWrappingPaper = 0
SizeOfRisbom = 0
for kdo in TailleKdoInt :
    face = []
    face.append(kdo[0]*kdo[1])
    face.append(kdo[1]*kdo[2])
    face.append(kdo[0]*kdo[2])
    wrappingPaper = sum([2*sizef for sizef in face]) + min(face)
    kdo = sorted(kdo)
    risbom = 2*kdo[0] + 2*kdo[1] + kdo[0]*kdo[1]*kdo[2]
    print(kdo,wrappingPaper)
    SizeOfWrappingPaper += wrappingPaper
    SizeOfRisbom += risbom
print(SizeOfWrappingPaper)
print(SizeOfRisbom)