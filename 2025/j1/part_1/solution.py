import utils

def solution(vals_parsed) :
    res = utils.todo(vals_parsed)
    return res

if __name__ == "__main__" :
    vals = open('input.txt', 'r').read().splitlines()
    vals_parsed = list(vals[0].split(','))
    print(vals_parsed)
    print(solution(vals_parsed))