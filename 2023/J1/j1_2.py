import re

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def string_to_int_at_beginning(string):
    if is_digit(string[1]):
        return string[1]
    elif re.match("\$one.*", string):
        return "1"
    elif re.match("\$two.*", string):
        return "2"
    elif re.match("\$three.*", string):
        return "3"
    elif re.match("\$four.*", string):
        return "4"
    elif re.match("\$five.*", string):
        return "5"
    elif re.match("\$six.*", string):
        return "6"
    elif re.match("\$seven.*", string):
        return "7"
    elif re.match("\$eight.*", string):
        return "8"
    elif re.match("\$nine.*", string):
        return "9"
    else:
        return string_to_int_at_beginning("$"+string[2:])

def string_to_int_at_end(string):
    if is_digit(string[-2]):
        return string[-2]
    elif re.match(".*one\$", string):
        return "1"
    elif re.match(".*two\$", string):
        return "2"
    elif re.match(".*three\$", string):
        return "3"
    elif re.match(".*four\$", string):
        return "4"
    elif re.match(".*five\$", string):
        return "5"
    elif re.match(".*six\$", string):
        return "6"
    elif re.match(".*seven\$", string):
        return "7"
    elif re.match(".*eight\$", string):
        return "8"
    elif re.match(".*nine\$", string):
        return "9"
    else:
        return string_to_int_at_end(string[:-2]+"$")

IN = open("j1.txt", "r").read().splitlines()
sum = 0

for lettres in IN:
    first_digit = string_to_int_at_beginning("$"+lettres)
    last_digit = string_to_int_at_end(lettres+"$")
    val = int(first_digit + last_digit)
    sum += val

print(sum)



