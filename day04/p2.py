with open('in.txt', 'r') as f:
    cards = {}

    for line in f.readlines():
        card_n, num = line.split(":")
        card_n = int(card_n.split(" ")[-1])

        win, yours = num.split("|")
        win, yours = list(map(int, win.split())), list(map(int, yours.split()))

        cards[card_n] = {
            "matches": len(set.intersection(set(win), set(yours))),
            "copies": 1
        }

    for id, card in cards.items():
        # increase count for next cards equal to num of matches
        start = id+1
        end = start + card['matches']
        for i in range(start, end):
            cards[i]["copies"] += card['copies']
    
    ans = 0
    # add all copies count
    for card in cards.values():
        ans += card['copies']

    print(ans)

