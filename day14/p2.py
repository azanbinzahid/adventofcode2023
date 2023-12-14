import numpy as np

def read(filename='in.txt'):
    with open(filename, 'r') as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line.strip()))

        return np.array(grid)

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



def cycle(grid):
    """
    can add loop but this is more readable
    """
    
    # north
    grid = tilt(grid)

    # west 
    grid = np.rot90(grid, axes=(1, 0))
    grid = tilt(grid)
    grid = np.rot90(grid)

    # south 
    grid = np.rot90(grid, axes=(1, 0))
    grid = np.rot90(grid, axes=(1, 0))
    grid = tilt(grid)
    grid = np.rot90(grid)
    grid = np.rot90(grid)
    # east
    grid = np.rot90(grid, axes=(1, 0))
    grid = np.rot90(grid, axes=(1, 0))
    grid = np.rot90(grid, axes=(1, 0))
    grid = tilt(grid)
    grid = np.rot90(grid)
    grid = np.rot90(grid)
    grid = np.rot90(grid)
    return grid

def main():
    grid = read()
    
    # north

    grid = tilt(grid)

    cache ={}
    values={}
    max_cycle = 1000000000

    # the cycle is periodic, find the 
    for i in range(max_cycle):
        grid = cycle(grid)
        
        # arrays are unhashable
        key = tuple(grid.flatten())

        # if we have already seen the formation
        if key in cache:
            ans = values[
                cache[key] + (max_cycle-1 - cache[key]) % (i-cache[key])
            ]
            break
        else:
            cache[key] = i
            values[i] = count_load(grid)

    print(ans)

main()