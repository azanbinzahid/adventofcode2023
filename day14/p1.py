def read(filename='in.txt'):
    with open(filename, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line.strip()))

        return grid

def tilt(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                for x in range(i+1, len(grid)):
                    if grid[x][j] == 'O':
                        grid[i][j] = 'O'
                        grid[x][j] = '.'
                        break
                    
                    elif grid[x][j] == '#':
                        break

    return grid

def count_load(grid):
    count = 0


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                count += len(grid) - i
    
    return count



def main():
    grid = read()
    
    grid = tilt(grid)

 

    ans = count_load(grid)

    print(ans)

main()