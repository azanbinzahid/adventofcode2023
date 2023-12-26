def read(filename='in.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data

def sort_bricks(bricks_coord):
    bricks = []
    for brick in bricks_coord:
        c1,c2 = brick.split('~')
        p = [list(map(int, c1.split(','))), list(map(int, c2.split(',')))]
        for i in range(3): 
            if p[0][i] != p[1][i]:
                start = min(p[0][i],p[1][i])+1
                end = max(p[0][i],p[1][i])
                for j in range(start, end):
                    p.append(p[0][:i]+[j]+p[0][i+1:])
        bricks.append(p)
   
    return sorted(bricks, key=lambda b: min(p[2] for p in b)) 


def freefall(bricks):
    num = 0
    res = []
    landed = set()

    for brick in bricks:
        moved = False
        while True:
            new_brick = [ [x,y,z-1] for x,y,z in brick ]
            if any((p[2] == 0 or (tuple(p) in landed)) for p in new_brick):
                break
            else:
                brick = new_brick
                moved = True
        for p in brick:
            landed.add(tuple(p))
        res.append(brick)
        num += 1 if moved else 0
    return res,num


if __name__ == "__main__":

    bricks = read()
    bricks = sort_bricks(bricks)

    bricks, total = freefall(bricks)

    ans = 0
    for i in range(len(bricks)):
        nb = bricks[:i]+bricks[i+1:]
        nb, total = freefall(nb)

        # P2 change
        ans += total

    print(ans)
