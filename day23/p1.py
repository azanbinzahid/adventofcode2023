def read(filename='sample.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(list(line.strip()))

    return data
    

class Direction:
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    up = (-1, 0)

visited = {}

def isValid(i, j, path):
    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])):
        return False

    if (i, j) in path:
        return False

    if grid[i][j] == '#':
        return False

    return True

from collections import deque as queue

def bfs(row, col):

    ans = 0

    q = queue()
    path = []
    path.append((row, col))
    q.append(path.copy())

    while q:
        path = q.popleft()
        i, j = path[-1]

        if  i == len(grid)-1:
            ans = max(ans, len(path))

        if grid[i][j] == '>':
            directions = [Direction.right]
        elif grid[i][j] == 'v':
            directions = [Direction.down]
        elif grid[i][j] == '<':
            directions = [Direction.left]
        else:
            directions = [Direction.right, Direction.down, Direction.left, Direction.up]
     

        # move
        for d in directions:
            di, dj = d
            x, y = i+di, j+dj
            if isValid(x, y, path):
                new_path = path.copy()
                new_path.append((x, y))
                q.append(new_path)
        
    return (ans)



if __name__ == "__main__":

    grid = read()
    ans = bfs(0, 1)

    print(ans-1)