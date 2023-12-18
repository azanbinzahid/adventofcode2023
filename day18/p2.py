from p1 import read, theorum

if __name__ == "__main__":

    data = read()
    steps = []
    for line in data:
        d, l , c = line.split()

        # P2 [just changed input reading]
        d,l = c[-2],c[-7:-2]
        steps.append((d,int(l,16)))

    ans = theorum(steps)
    print(ans)