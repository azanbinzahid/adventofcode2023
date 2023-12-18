def read(filename='in.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data
    
dirs = { 'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0),
         '0':(0,1), '2':(0,-1), '3':(-1,0), '1':(1,0)}

# math wins
# https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
# https://cp-algorithms.com/geometry/picks-theorem.html
def theorum(steps):
    y,x = 0,0
    perimeter,inside = 0,0
    for d,l in steps:
        di, dj = dirs[d]
        di, dj = di*l, dj*l

        y,x = y+di,x+dj
        perimeter += l
        inside += x*di

    return inside+perimeter//2+1



# tried solving via graph and manual count (only works well on sample)
def solve(data):

    class Direction:
        right = (0, 1)
        down = (1, 0)
        left = (0, -1)
        up = (-1, 0)

    grid = []
    for _ in range(2000):
        grid.append(['.']*2000)

    # start
    curr = (0, 0)
    
    # max
    R, D = 0, 0
    L, U = 0, 0
    
    for dir, meters in data:
        if dir == 'R':
            di, dj = Direction.right
        elif dir == 'L':
            di, dj = Direction.left
        elif dir == 'U':
            di, dj = Direction.up
        elif dir == 'D':
            di, dj = Direction.down

        for _ in range(int(meters)):
            i, j = curr
            grid[i][j] = '#'
            curr = (i+di, j+dj)

            R = max(R, curr[0])
            D = max(D, curr[1])
            L = min(L, curr[0])
            U = min(U, curr[1])
    
    # [debug]
    # for i in range(L, R+1):
    #     for j in range(U, D+1):
    #         print(grid[i][j], end='')
    #     print('')

    ans = 0
    for i in range(L, R+1):
        start = False
        end = False

        for j in range(U, D+1):
            if grid[i][j] == '#':
                ans +=1
                x = j+1

                end = True if start else False

                if not end:
                    while x < D+1 and grid[i][x] == '.':
                        if x == j+1:
                            start = True
                        x += 1
                        ans += 1
                else:
                    start = False
                    end = False
    return ans

if __name__ == "__main__":

    data = read()
    steps = []
    for line in data:
        d, l , c = line.split()
        steps.append((d, int(l)))

    ans = theorum(steps)
    print(ans)