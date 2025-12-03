def solution(vals_parsed) :
    res = 0
    for val in vals_parsed :
        a, b = map(int, val.split('-'))
        for i in range(a, b + 1) :
            if is_invalid(i) :
                res += i
    return res

def is_invalid(n) :
    s = str(n)
    if len(s)%2 != 0 :
        return False
    l_half, r_half = int(s[:len(s)//2]), int(s[len(s)//2:])
    return l_half == r_half

if __name__ == "__main__" :
    vals_parsed = open('input.txt', 'r').read().splitlines()[0].split(',')
    print(solution(vals_parsed))
