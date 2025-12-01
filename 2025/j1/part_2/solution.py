import utils
class Direction :
    LEFT = 'L'
    RIGHT = 'R'

def solution(vals_parsed) :
    dial = 50
    res = 0
    for line in vals_parsed :
        line = line[0]
        direction = Direction.LEFT if line[0] == 'L' else Direction.RIGHT
        steps = int(line[1:])
        dial, bonus = get_new_pos(dial, direction, steps)
        res += bonus
        if dial == 0 :
            res += 1
    return res

def get_new_pos(start : int, direction : Direction, steps : int) -> tuple[int, int] :
    res = start
    bonus = abs(steps - (steps % 100)) // 100
    steps = steps % 100
    if direction == Direction.LEFT :
        res = (res - steps) % 100
        if start != 0 and res != 0 :
            bonus += 1 if res != start - steps else 0
    elif direction == Direction.RIGHT :
        res = (res + steps) % 100
        if start != 0 and res != 0 :
            bonus += 1 if res != start + steps else 0
    return res, bonus

if __name__ == "__main__" :
    vals = open('input.txt', 'r').read().splitlines()
    vals_parsed = [ i.split(',') for i in (vals)]
    print(solution(vals_parsed))
