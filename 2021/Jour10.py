jeVoudraisOuvrirUneParanthese = open("J10-input.txt", "r").read().splitlines()
print(jeVoudraisOuvrirUneParanthese)
wrongSymb = 0
typepar = "({[<"
for listeparanthese in jeVoudraisOuvrirUneParanthese :
    pile = []
    for paranthese in listeparanthese :
        if paranthese in typepar :
            pile.append(paranthese)
        elif paranthese == ">" :
            if not (len(pile) and pile[len(pile)-1]=="<") :
                wrongSymb += 25137
                print(">")
                break
            pile=pile[:len(pile)-1]
        elif paranthese == ")" :
            if not (len(pile) and pile[len(pile)-1]=="(") :
                wrongSymb += 3
                print(")")
                break
            pile=pile[:len(pile)-1]
        elif paranthese == "}" :
            if not (len(pile) and pile[len(pile)-1]=="{") :     
                wrongSymb += 1197
                print("}")
                break
            pile=pile[:len(pile)-1]
        elif paranthese == "]" :
            if not (len(pile) and pile[len(pile)-1]=="[") :
                wrongSymb += 57
                print("]")
                break
            pile=pile[:len(pile)-1]
print(wrongSymb)