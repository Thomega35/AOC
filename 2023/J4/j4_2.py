IN = open("j4t.txt", "r").read().splitlines()

id = 1

table_score = {}

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

    table_score[id] = score
    id += 1

card_result = [1] * len(table_score)

for card in table_score:
    score = table_score[card]
    for j in range(0, card_result[card-1]):
        for i in range(0, score):
            card_result[card+i] += 1
    print(card_result)
print(table_score)
