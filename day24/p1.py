from itertools import combinations

def read(filename='in.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data

def read_stones(data):
    stones = []
    for line in data:
        positon, velocity = line.split("@")
        x, y, z = map(int, positon.split(","))
        vx, vy, vz = map(int, velocity.split(","))
        stones.append([x, y, z, vx, vy, vz])

    return stones

def collide(A, B):
    ax, ay, az = A[:3]
    avx, avy, avz = A[3:]

    bx, by, bz = B[:3]
    bvx, bvy, bvz = B[3:]

    ax2, ay2 = ax+avx, ay+avy
    bx2, by2 = bx+bvx, by+bvy
    
    den = ((ax-ax2)*(by-by2)-(ay-ay2)*(bx-bx2))
    if den == 0:
        return False

    x = ( (ax*ay2 - ay*ax2)*(bx-bx2) - (ax-ax2)*(bx*by2-by*bx2)) / den
    y = ( (ax*ay2 - ay*ax2)*(by-by2) - (ay-ay2)*(bx*by2-by*bx2)) / den

    # low,high = 7,27
    low,high = 200000000000000,400000000000000
    if low <= x <=high and low <= y <= high and (x>ax)==(ax2>ax) and (x>bx)==(bx2>bx):
        return True
    return False

if __name__ == "__main__":

    data = read()
    stones = read_stones(data)

    count = 0
    for a,b in combinations(range(len(stones)),2):
        count += 1 if collide(stones[a],stones[b]) else 0
    print(count)