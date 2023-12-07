def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

IN = open("j1.txt", "r").read().splitlines()
sum = 0
for sentence in IN:
    first = False
    first_digit = ""
    last_digit = ""
    last = False
    for char in sentence:
        if is_digit(char) and not first:
            first_digit = char
            first = True
        elif is_digit(char) and first:
            last_digit = char
            last = True
    if not last:
        last_digit = first_digit
    sum += int(first_digit + last_digit)

print(sum)
