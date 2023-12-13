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


def get_mirror_position(grid):
    for i in range(len(grid)-1):
        count = True
        j = 0
        while i-j >=0 and i+j+1 < len(grid) and count:
            if grid[i-j] != grid[i+j+1]:
                count = False
            j+=1
            
        if count:
            return i+1

def find_reflection(grid):
    transpose = list(map(list, zip(*grid)))

    row = get_mirror_position(grid)
    col = get_mirror_position(transpose)

    if row:
        return row, 0
    elif col:
        return 0, col

def main():
    grids = read()
    
    ans = 0
    for grid in grids:
        r, c = find_reflection(grid)
        ans += (c+r*100)

    print(ans)

main()