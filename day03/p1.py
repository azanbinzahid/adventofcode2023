with open('in.txt', 'r') as f:
    grid = []
    log = set()

    for line in f.readlines():
        row = line.strip()
        grid.append(row)

    def valid_index(i, j):
        return 0 <= i <= len(grid) and  0 <= j <= len(grid[0])

    def get_num(i, j):
        if not valid_index(i, j) or not grid[i][j].isdigit():
            return 0
        
        num = []
        start_i, start_j = 0, 0
        found = False
        for idx, value in enumerate(grid[i]+"."):
            
            if idx == j:
                found = True
            if value.isdigit():
                if num == []:
                    start_i, start_j = i, idx
                num.append(value)
                print(num)
            
            else:
                if found:
                    if (start_i, start_j) in log:
                        return 0
                    
                    log.add((start_i, start_j))
                    # print(int("".join(num)))
                    return int("".join(num))
                num = []
                start_i, start_j = 0,0
    

    def add_adjecent(i, j):
        print(grid[i][j], i, j)
        ans = 0

        # check all sides including diagonal
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                ans += get_num(x, y)

        return ans

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "." and not grid[i][j].isdigit():
                ans += add_adjecent(i, j)

    print(ans)