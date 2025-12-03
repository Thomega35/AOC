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
    pattern  = s[0]
    for i in s[1:] :
        rest = s[len(pattern):]
        while rest.startswith(pattern) :
            rest = rest[len(pattern):]
        if rest == '' :
            return True
        pattern += i
    return False


if __name__ == "__main__" :
    vals_parsed = open('input.txt', 'r').read().splitlines()[0].split(',')
    print(solution(vals_parsed))
