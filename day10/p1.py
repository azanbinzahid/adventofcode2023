grid = []
start = None
visited = {}
from collections import deque as queue

with open('in.txt', 'r') as f:
    for line in f.readlines():
        row = list(line.strip())

        # find start index
        if 'S' in row:
            start = (len(grid), row.index('S'))
        
        grid.append(row)


    # figure out start pipe shape or do it manually
    a, b = start
    up, down, left, right = False, False, False, False

    if grid[a-1][b] in ['|', '7', 'F']:
        up = True
    if grid[a+1][b] in ['|', 'L', 'J']:
        down = True
    if grid[a][b+1] in ['-', '7', 'J']:
        right = True
    if grid[a][b-1] in ['-', 'L', 'F']:
        left = True

    if up and down:
        grid[a][b] = '|'
    elif left and right:
        grid[a][b] = '-'
    elif up:
        grid[a][b] = 'J' if left else 'L'
    elif down:
        grid[a][b] = '7' if left else 'F'

    # end start find

    def directions(i, j):
        c = grid[i][j]

        if c == '|': 
            return [(i-1,j),(i+1,j)]
        if c == '-': 
            return [(i,j-1),(i,j+1)]
        if c == 'L': 
            return [(i-1,j),(i,j+1)]
        if c == 'J': 
            return [(i-1,j),(i,j-1)]
        if c == '7': 
            return [(i, j-1),(i+1,j)]
        if c == 'F': 
            return [(i,j+ 1),(i+1,j)]

    # ================== BFS ==========

    def isValid(i, j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])):
            return False
    
        if (i, j) in visited:
            return False

        return True
    
    def bfs(row, col):
        q = queue()
        ans = 0

        # mark starting location
        q.append(( row, col, 0 ))
        visited[(row, col)] = 0


        while (len(q) > 0):
            i, j, step = q.popleft()

            # move
            for (x, y) in directions(i, j):
                if (isValid(x, y)):
                    q.append((x, y, step+1))
                    visited[(x, y)] = step+1
                    ans = max(ans, step+1)
        print(ans)
    # ======= BFS end

    bfs(*start)

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         print(visited.get((i, j), '.'), end = " ")
    #     print()

