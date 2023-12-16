import sys

# didn't know I'd waste 5 hours just for (not knowing) this. 
sys.setrecursionlimit(3000)


global grid, visited


def read(filename='in.txt'):
    grid = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    return grid
            

class Direction:
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    up = (-1, 0)
    

def solve(curr=(0, 0), dir=Direction.right):

    global grid, visited

    if dir == Direction.right:
        dir_symbol = '>'
    elif dir == Direction.down:
        dir_symbol = 'v'
    elif dir == Direction.left:
        dir_symbol = '<'
    elif dir == Direction.up:
        dir_symbol = '^'

    # check if curr out of bounds of grid
    if not(0 <= curr[0] < len(grid)) \
    or not (0 <= curr[1] < len(grid[0])) \
    or dir_symbol in visited[curr]:
        return

    visited[curr] += dir_symbol
    
    # [debug] print each step
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if any(x in visited[(i, j)] for x in ['>', 'v', '<', '^']) and grid[i][j] not in ['\\', '/', '|', '-']:
    #             if len(visited[(i, j)]) > 1:
    #                 print(len(visited[(i, j)]), end='')
    #             else:
    #                 print(visited[(i, j)], end='')
    #         else:
    #             print(grid[i][j], end='')
    #     print("")
    # print("")
    # input()

    i, j = curr

    if grid[i][j] == '.':
        di, dj = dir
        curr = (i+di, j+dj)
        solve(curr, dir)
    
    elif grid[i][j] == '\\':
        if dir in [Direction.right, Direction.down]:
            dir = Direction.down if dir == Direction.right else Direction.right
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
        
        elif dir in [Direction.left, Direction.up]:
            dir = Direction.up if dir == Direction.left else Direction.left
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)

    elif grid[i][j] == '/':
        if dir in [Direction.right, Direction.up]:
            dir = Direction.up if dir == Direction.right else Direction.right
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)

        elif dir in [Direction.left, Direction.down]:
            dir = Direction.down if dir == Direction.left else Direction.left
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)

    elif grid[i][j] == '-':
        if dir in [Direction.right, Direction.left]:
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
        else:
            dir = Direction.right
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
            dir = Direction.left
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)

    elif grid[i][j] == '|':
        if dir in [Direction.up, Direction.down]:
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
        else:
            dir = Direction.down
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
            dir = Direction.up
            di, dj = dir
            curr = (i+di, j+dj)
            solve(curr, dir)
    


if __name__ == "__main__":
    grid = read()

    # for row in grid:
    #     print(row)

    visited = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            visited[(i, j)] = ''

    solve()

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if visited[(i, j)] != '':
                ans += 1

    print(ans)
