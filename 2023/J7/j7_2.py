
def tri(hand):
    nb_card = {}
    value = 0
    for card in hand[0]:
        if card[0] in nb_card:
            nb_card[card[0]] += 1
        else:
            nb_card[card[0]] = 1

    try:
        nb_joker = nb_card['J']
        del nb_card['J']
    except:
        nb_joker = 0

    nb_card = sorted(nb_card.items(), key=lambda x: x[1], reverse=True)
    if len(nb_card) > 0:
        nb_card[0] = (nb_card[0][0], nb_card[0][1] + nb_joker)
    print(nb_card)
    if nb_joker == 5 or nb_card[0][1] == 5 :
        value += 10 ** 1000000
    elif nb_card[0][1] == 4 :
        value += 10 ** 100000
    elif nb_card[0][1] == 3 and nb_card[1][1] == 2:
        value += 10 ** 10000
    elif nb_card[0][1] == 3:
        value += 10 ** 1000
    elif nb_card[0][1] == 2 and nb_card[1][1] == 2:
        value += 10 ** 100
    elif nb_card[0][1] == 2:
        value += 10 ** 10

    deck_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}

    for card in enumerate(hand[0]):
        card_value = 0
        if card[1][0] in deck_value:
            card_value = deck_value[card[1][0]]
        else:
            card_value = int(card[1][0])

        value_to_add = card_value * 15 ** (5 - card[0])
        # print(value_to_add)
        value += value_to_add

    return value


IN = open("j7.txt").read().splitlines()

hands = {}

for line in IN:
    line = line.split()
    hands[line[0]] = int(line[1:][0])

# sort by custom function tri
hands = sorted(hands.items(), key=tri, reverse=False)


print(hands)
result_sum = 0
for index, bid in enumerate(hands):
    result_sum += (index + 1) * bid[1]

print(result_sum)
# correct : 249356515