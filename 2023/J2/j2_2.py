IN = open("j2.txt","r").read().splitlines()
sum = 0
for i in range(len(IN)):
    game, tirages = IN[i].split(":")
    game = game.split(" ")
    id = int(game[1])
    tirages = tirages.split(";")
    min_red, min_green, min_blue = 0, 0, 0
    for tirage in tirages:
        colors = tirage.split(",")
        for color in colors:
            nothing, color_value, color_name = color.split(" ")
            color_value = int(color_value)
            if color_name == "red" and color_value > min_red:
                min_red = color_value
            if color_name == "green" and color_value > min_green:
                min_green = color_value
            if color_name == "blue" and color_value > min_blue:
                min_blue = color_value
    sum+= min_green * min_blue * min_red
print(sum)