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
        dial = get_new_pos(dial, direction, steps)
        if dial == 0 :
            res += 1
    return res

def get_new_pos(start : int, direction : Direction, steps : int) -> int:
    res = start
    if direction == Direction.LEFT :
        res -= steps
        res = res % 100
    elif direction == Direction.RIGHT :
        res += steps
        res = res % 100
    return res

if __name__ == "__main__" :
    vals = open('input.txt', 'r').read().splitlines()
    vals_parsed = [ i.split(',') for i in (vals)]
    print(solution(vals_parsed))
