jeVoudraisOuvrirUneparenthese = open("J10-input.txt", "r").read().splitlines()
sumcompletion = []
typepar = "({[<"
tabassoc = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}

for listeparenthese in jeVoudraisOuvrirUneparenthese :
    pile = []
    wrongSymb = 0
    corru = False
    for parenthese in listeparenthese :
        if parenthese in typepar :
            pile.append(parenthese)
        elif parenthese == ">" :
            if not (len(pile) and pile[len(pile)-1]=="<") :
                print("> corru")
                corru = True
            pile=pile[:len(pile)-1]
        elif parenthese == ")" :
            if not (len(pile) and pile[len(pile)-1]=="(") :
                print(") corru")
                corru = True
            pile=pile[:len(pile)-1]
        elif parenthese == "}" :
            if not (len(pile) and pile[len(pile)-1]=="{") : 
                print("} corru")
                corru = True
            pile=pile[:len(pile)-1]
        elif parenthese == "]" :
            if not (len(pile) and pile[len(pile)-1]=="[") :
                print("] corru")
                corru = True
            pile=pile[:len(pile)-1]
    if not corru :
        pile.reverse()
        print(pile)
        for para in pile :
            wrongSymb = wrongSymb*5 + tabassoc[para]
        sumcompletion.append(wrongSymb)
sumcompletion.sort()
print(sumcompletion[int(len(sumcompletion)/2)]) 