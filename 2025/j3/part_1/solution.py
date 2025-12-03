def solution(vals_parsed) :
    res = 0
    for line in vals_parsed :
        max1 = 0
        max2 = 0
        for char in range(len(line)) :
            val = int(line[char])
            if val > max1 and char+1 < len(line) :
                max1 = val
                max2 = int(line[char+1])
                char += 1
            elif val > max2 :
                max2 = val
        res += max1 * 10 + max2
    return res

if __name__ == "__main__" :
    vals_parsed = open('input.txt', 'r').read().splitlines()
    print(solution(vals_parsed))
