import numpy as np
IN = open('j14.txt', 'r').read().splitlines()

IN = [list(line) for line in IN]

def cycle(table) :
    is_moving = True
    # North
    while is_moving:
        is_moving = False
        for row in range(len(table)):
            rock_idexes = []
            for col in range(len(table[row])):
                if table[row][col] == 'O':
                    rock_idexes.append(col)
            for rock in rock_idexes:
                if table[row-1][rock] == '.' and row > 0:
                    table[row-1][rock] = 'O'
                    table[row][rock] = '.'
                    is_moving = True
                    
    is_moving = True
    # West
    while is_moving:
        is_moving = False
        for row in range(len(table)):
            rock_idexes = []
            for col in range(len(table[row])):
                if table[row][col] == 'O':
                    rock_idexes.append(col)
            for rock in rock_idexes:
                if table[row][rock-1] == '.' and rock > 0:
                    table[row][rock-1] = 'O'
                    table[row][rock] = '.'
                    is_moving = True
                    
    # South
    is_moving = True
    while is_moving:
        is_moving = False
        for row in range(len(table)-1, -1, -1):
            rock_idexes = []
            for col in range(len(table[row])):
                if table[row][col] == 'O':
                    rock_idexes.append(col)
            for rock in rock_idexes:
                if  row < len(table)-1 and table[row+1][rock] == '.':
                    table[row+1][rock] = 'O'
                    table[row][rock] = '.'
                    is_moving = True
                    
    # East
    is_moving = True
    while is_moving:
        is_moving = False
        for row in range(len(table)):
            rock_idexes = []
            for col in range(len(table[row])):
                if table[row][col] == 'O':
                    rock_idexes.append(col)
            for rock in rock_idexes:
                if rock < len(table[row])-1 and table[row][rock+1] == '.':
                    table[row][rock+1] = 'O'
                    table[row][rock] = '.'
                    is_moving = True
    
    return table

def get_table_in_tables_index(tables, table):
    for i in range(len(tables)):
        if np.array_equal(tables[i], table):
            return i

def calc_somme(table):
    somme = 0
    to_add = 1
    for index in range(len(table)-1, -1, -1):
        for elem in table[index] :
            somme += to_add if elem == 'O' else 0
        to_add += 1
    return somme

tables = []

index = 1
indice = None

while True:
    tables.append([ np.copy(elem) for elem in IN ])
    IN = cycle(IN)
    indice = get_table_in_tables_index(tables, IN)
    if  indice != None :
        tables.append([ np.copy(elem) for elem in IN ])
        break
    index += 1
    if index % 10 == 0:
        print(index)

print(index - indice, index)
for elem in range((1000000000 - index) % (index - indice)):
    IN = cycle(IN)

print(calc_somme(IN))