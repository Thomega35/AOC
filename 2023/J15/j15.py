IN = open('j15.txt', 'r').read().splitlines()

IN = [ i for i in IN[0].split(',')]
print(IN)

somme = 0

def get_char_of_instruction(instruction) :
    tempsum = 0
    for character in instruction :
        value = ord(character)
        tempsum += value
        tempsum *= 17
        tempsum %= 256
    return tempsum

for instruction in IN :
    tempsum = get_char_of_instruction(instruction)
    somme += tempsum

print(somme)