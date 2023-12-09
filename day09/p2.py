with open('in.txt', 'r') as f:
    histories = []
    for line in f.readlines():
        histories.append(
            [list(map(int, line.strip().split()))]
        )

    for history in histories:
        while not all(h == 0 for h in history[-1]):
            new_history = []
            for i in range(len(history[-1])-1):
                curr, next = history[-1][i], history[-1][i+1]
                new_history.append(next-curr)
            history.append(new_history)

    # print(histories)

    ans = 0
    for history in histories:
        history = reversed(history)
        first_h = 0
        for h in history:
            
            # p2 change
            first_h = h[0] - first_h
        
        # p2 change
        ans+=first_h

    print(ans)