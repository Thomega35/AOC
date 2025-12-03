def solution(vals_parsed) :
    res = 0
    for line in vals_parsed :
        jolt = line[:12]
        for char in range(12,len(line)) :
            val = int(line[char])
            for num in range(len(jolt)-1) :
                if int(jolt[num]) < int(jolt[num+1]) :
                    jolt = jolt[:num] + jolt[num+1:] + str(val)
                    break
                elif num == len(jolt)-2 and int(jolt[num+1]) < val :
                    jolt = jolt[:len(jolt)-1] + str(val)
        res += int(jolt)
    return res

if __name__ == "__main__" :
    vals_parsed = open('input.txt', 'r').read().splitlines()
    print(solution(vals_parsed))
