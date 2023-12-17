global grid

def read(filename='in.txt'):
    grid = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            grid.append(list(map(int, line.strip())))

    return grid

import heapq



# just take any dijkstra impl and modify it as per your needs
def dijkstra(grid, max_blocks=3):
    H, W = len(grid), len(grid[0])

    queue = []
    (cost, start, blocks, dirs) = (0, (0, 0), 1, (0, 1))
    heapq.heappush(queue, (cost, start, blocks, dirs))

    seen = set()

    while queue:
        cost, (row, col), blocks, (dr, dc) = heapq.heappop(queue)

        if (row, col, dr, dc, blocks) in seen:
            continue

        seen.add((row, col, dr, dc, blocks))

        # we reach our destination
        if (row, col) == (H - 1, W - 1):
            return cost

        # look for next step
        for ndr, ndc in [(dr, dc), (-dc, -dr), (dc, dr)]:
            nrow, ncol = row + ndr, col + ndc

            # check if we are not going out of bound
            if not (0 <= nrow < H and 0 <= ncol < W):
                continue
            
            # break if we have already taken max steps in one direction
            if (dr, dc) == (ndr, ndc) and blocks == max_blocks:
                continue
            
            # increase count for consective direction steps else reset
            nblocks = blocks + 1 if (dr, dc) == (ndr, ndc) else 1

            ncost = cost + int(grid[nrow][ncol])

            heapq.heappush(
                queue,
                (ncost, (nrow, ncol), nblocks, (ndr, ndc))
            )



if __name__ == "__main__":

    grid = read()

    # for row in grid:
    #     print(row)
    # print("")

    ans = dijkstra(grid, max_blocks=3)

    print(ans)
