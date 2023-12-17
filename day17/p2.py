global grid

def read(filename='in.txt'):
    grid = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            grid.append(list(map(int, line.strip())))

    return grid

import heapq

def dijkstra(grid, min_blocks=0, max_blocks=3):
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

        # [P2] return only if min steps taken
        if (row, col) == (H - 1, W - 1) and blocks >= min_blocks:
            return cost

        for ndr, ndc in [(dr, dc), (-dc, -dr), (dc, dr)]:
            nrow, ncol = row + ndr, col + ndc

            if not (0 <= nrow < H and 0 <= ncol < W):
                continue

            # [P2] checkif we have already taken at least min steps in one direction
            if min_blocks and (dr, dc) != (ndr, ndc) and blocks < min_blocks:
                continue

            if (dr, dc) == (ndr, ndc) and blocks == max_blocks:
                continue

            nblocks = blocks + 1 if (dr, dc) == (ndr, ndc) else 1

            ncost = cost + int(grid[nrow][ncol])

            heapq.heappush(
                queue,
                (ncost, (nrow, ncol), nblocks, (ndr, ndc)),
            )



if __name__ == "__main__":

    grid = read()

    # for row in grid:
    #     print(row)
    # print("")

    ans = dijkstra(grid, min_blocks=4, max_blocks=10)

    print(ans)
