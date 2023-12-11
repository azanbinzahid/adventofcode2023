import math

grid = []

with open('in.txt', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

    # expands universer, find rows with no galaxy
    # given 2 by 2 grid with . as empty and # as non empty, get all the rows which are empty
    empty_rows = []
    empty_cols = []
    for row in range(len(grid)):
        if '#' not in grid[row]:
            empty_rows.append(row)

    trans_grid = list(map(list, zip(*grid)))
    for row in range(len(trans_grid)):
        if '#' not in trans_grid[row]:
            empty_cols.append(row)

    expanded_grid = []
    for row in range(len(grid)):
        if row in empty_rows:
            expanded_grid.append(grid[row])
            expanded_grid.append(grid[row])
        else:
            expanded_grid.append(grid[row])

    # add new empty columns in new grid
    for row in range(len(expanded_grid)):
        c = 0
        for col in empty_cols:
            # pad
            c += 1 
            expanded_grid[row] = expanded_grid[row][:col+c] + '|' + expanded_grid[row][col+c:]

    # convert each row to list in new grid
    for row in range(len(expanded_grid)):
        expanded_grid[row] = list(expanded_grid[row])


    # # number # in order of appear in new grid
    counter = 0
    galaxy = {}

    for row in range(len(expanded_grid)):
        for col in range(len(expanded_grid[row])):
            if expanded_grid[row][col] == '#':
                counter += 1
                expanded_grid[row][col] = counter
                galaxy[counter] = (row, col)
    

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

# print(empty_rows, empty_cols)
# for g in expanded_grid:
#     print("".join(str(r) for r in g))

# print("==")
# for g in grid:
#     print(g)


dist = []
for i in range(1, counter+1):
    for j in range(i+1, counter+1):
         dist.append(manhattan(galaxy[i], galaxy[j]))
      

# print(len(dist))
# print(galaxy)

print(sum(dist))

