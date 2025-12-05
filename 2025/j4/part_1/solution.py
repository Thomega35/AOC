class PaperVal :
    PAPER = '@'
    EMPTY = '.'
    OK = 'X'

def solution(vals_parsed) :
    paper_map = do_map(vals_parsed)
    res = 0
    for (i, j), value in paper_map.items() :
        if value == PaperVal.EMPTY :
            continue
        neighbors = [ (i-1, j-1), (i-1, j), (i-1, j+1),
                      (i, j-1),             (i, j+1),
                      (i+1, j-1), (i+1, j), (i+1, j+1) ]
        # if 4 or less neighbors are paper res += 1
        paper_neighbors = 0
        print_line = ""
        for ni, nj in neighbors :
            print_line += f"({ni},{nj} : {paper_map.get((ni, nj), ' ')}), "
            if (ni, nj) in paper_map and (paper_map[(ni, nj)] == PaperVal.PAPER or paper_map[(ni, nj)] == PaperVal.OK) :
                paper_neighbors += 1
        print(f"Cell ({i},{j}) neighbors: {print_line} => paper_neighbors = {paper_neighbors}")
        if paper_neighbors < 4 :
            res += 1
            paper_map[(i, j)] = PaperVal.OK
    print_map(paper_map, vals_parsed)
    print('---')
    return res

def do_map(vals_parsed) :
    print(vals_parsed)
    paper_map = {}
    for i, line in enumerate(vals_parsed) :
        for j, char in enumerate(line) :
            paper_map[(i, j)] = char
    return paper_map

def print_map(paper_map, vals_parsed) :
    max_i = len(vals_parsed)
    max_j = len(vals_parsed[0])
    for i in range(max_i) :
        line = ''
        for j in range(max_j) :
            line += paper_map[(i, j)]
        print(line)

if __name__ == "__main__" :
    vals_parsed = open('input.txt', 'r').read().splitlines()
    print(solution(vals_parsed))
