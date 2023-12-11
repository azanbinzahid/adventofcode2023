import math

grid = []

with open('in.txt', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

    empty_rows = []
    empty_cols = []
    for row in range(len(grid)):
        if '#' not in grid[row]:
            empty_rows.append(row)

    trans_grid = list(map(list, zip(*grid)))
    for row in range(len(trans_grid)):
        if '#' not in trans_grid[row]:
            empty_cols.append(row)


    # number # in order of appear in new grid
    g_id = 0
    galaxy = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                g_id += 1
                galaxy[g_id] = (row, col)
    

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

# print(empty_rows, empty_cols)

dist = []

# P2: do not expand grid but just count how many empty rows/cols are in between
for i in range(1, g_id+1):
    for j in range(i+1, g_id+1):
        xi, yi = galaxy[i]
        xj, yj = galaxy[j]

        # in between empty row/col count
        rows = (min(xi, xj), max(xi, xj))
        cols = (min(yi, yj), max(yi, yj))

        r_count = sum(1 for r in range(*rows) if r in empty_rows)
        c_count = sum(1 for c in range(*cols) if c in empty_cols)
        
        d = ((r_count + c_count) * (1000000-1)) + manhattan(galaxy[i], galaxy[j])

        # print(f"galaxy ({galaxy[i]}, {galaxy[j]}): {d}; empty {rows}, {cols}")
        # print(r_count, c_count, i, j, d)
        dist.append(d)

print(sum(dist))

