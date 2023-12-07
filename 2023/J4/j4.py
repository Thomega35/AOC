IN = open("j4.txt", "r").read().splitlines()

sum = 0

for scratch_card in IN:
    name, card = scratch_card.split(":")
    rolled_numbers, winning_numbers = card.split("|")
    temp = rolled_numbers.split(" ")
    rolled_numbers = []
    for nb in temp:
        if nb != "":
            rolled_numbers.append(nb)

    temp = winning_numbers.split(" ")
    winning_numbers = []
    for nb in temp:
        if nb != "":
            winning_numbers.append(nb)

    score = 0
    for nb in rolled_numbers:
        if nb in winning_numbers:
            score += 1
    if score != 0:
        sum += 2**(score-1)
    print(score, 2**(score-1))

print(sum)