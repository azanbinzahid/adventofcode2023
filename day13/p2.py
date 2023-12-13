def read(filename='in.txt'):
    with open(filename, 'r') as f:
        grids = []
        grid = []
        for line in f.readlines():
            if line.strip() == '':
                grids.append(grid)
                grid = []

            else:
                grid.append(line.strip())

            # print(grid)

        grids.append(grid)
        return grids

def get_mirror_position(grid, prev):
    for i in range(len(grid)-1):
        count = True
        j = 0
        while i-j >=0 and i+j+1 < len(grid) and count:
            if grid[i-j] != grid[i+j+1]:
                count = False
            j+=1
            
        if count and i+1!=prev:
            return i+1


def find_reflection(grid, prev):

    prev_r, prev_c = prev
    transpose = list(map(list, zip(*grid)))


    row = get_mirror_position(grid, prev_r)
    col = get_mirror_position(transpose, prev_c)

    if row:
        return row, 0
    elif col:
        return 0, col

def find_reflection_with_smudge(grid):

    for i in range(len(grid)):
        grid[i] = list(grid[i])

    prev = find_reflection(grid, (-1, -1))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # replace the smudge
            grid[i][j] = '.' if grid[i][j] == '#' else '#'

            res = find_reflection(grid, prev)
            if res:
                return res

            # replace it back
            grid[i][j] = '.' if grid[i][j] == '#' else '#'


def main():
    grids = read()
    
    ans = 0
    for grid in grids:
        r, c = find_reflection_with_smudge(grid)
        ans += (c+r*100)

    print(ans)


main()