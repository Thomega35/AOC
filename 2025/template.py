import utils

def solution(vals_parsed) :
    res = utils.todo(vals_parsed)
    return res

if __name__ == "__main__" :
    vals = open('input.txt', 'r').read().splitlines()
    vals_parsed = [ i.split(',') for i in (vals)]
    print(solution(vals_parsed))
