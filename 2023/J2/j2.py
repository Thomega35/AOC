IN = open("j2.txt","r").read().splitlines()
sum = 0
for i in range(len(IN)):
    game, tirages = IN[i].split(":")
    game = game.split(" ")
    id = int(game[1])
    tirages = tirages.split(";")
    toAdd = True
    for tirage in tirages:
        colors = tirage.split(",")
        for color in colors:
            nothing, color_value, color_name = color.split(" ")
            color_value = int(color_value)
            if color_name == "red" and color_value > 12:
                toAdd = False
                break
            if color_name == "green" and color_value > 13:
                toAdd = False
                break
            if color_name == "blue" and color_value > 14:
                toAdd = False
                break
    if toAdd:
        sum += id
print(sum)