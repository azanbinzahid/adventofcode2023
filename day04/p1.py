with open('in.txt', 'r') as f:
    cards = {}

    for line in f.readlines():
        card_n, num = line.split(":")
        card_n = int(card_n.split(" ")[-1])

        win, yours = num.split("|")

        cards[card_n] = {
            "win": list(map(int, win.split())),
            "yours": list(map(int, yours.split()))
        }

    total_worth = 0
    for card in cards.values():
        worth = 0
        for i in card['yours']:
            if i in card['win']:
                if worth == 0:
                    worth = 1
                else:
                    worth *= 2 if worth > 0 else 1

        total_worth += worth

    print(total_worth)

