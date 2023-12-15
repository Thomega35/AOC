IN = open('j15.txt', 'r').read().splitlines()

IN = [ i for i in IN[0].split(',')]
print(IN)

def get_char_of_instruction(instruction) :
    tempsum = 0
    for character in instruction :
        value = ord(character)
        tempsum += value
        tempsum *= 17
        tempsum %= 256
    return tempsum

boxes = {}
for instruction in IN :
    if instruction[-1] == "-" :
        hash_of_instruction = get_char_of_instruction(instruction[:-1])
        if hash_of_instruction in boxes :
            boxes_at_hash = boxes[hash_of_instruction]
            new_boxe_at_hash = []
            for box in boxes_at_hash :
                if box[0] != instruction[:-1] :
                    new_boxe_at_hash.append(box)
            boxes[hash_of_instruction] = new_boxe_at_hash
    else :
        hash_of_instruction = get_char_of_instruction(instruction.split('=')[0])
        if hash_of_instruction in boxes :
            is_already_in = False
            new_boxe_at_hash = []
            for box in boxes[hash_of_instruction] :
                if box[0] == instruction.split('=')[0] :
                    is_already_in = True
                    new_boxe_at_hash.append(instruction.split('='))
                else :
                    new_boxe_at_hash.append(box)
            boxes[hash_of_instruction] = new_boxe_at_hash

            if not is_already_in :
                boxes[hash_of_instruction].append([ a for a in instruction.split('=')])
        else :
            boxes[hash_of_instruction] = [instruction.split('=')]

somme = 0

for box in boxes :
    for index, instruction in enumerate(boxes[box]) :
        to_add = int(instruction[1]) * (index + 1) * (box+1)
        somme += to_add

print(somme)