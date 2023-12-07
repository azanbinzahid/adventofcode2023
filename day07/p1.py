from collections import Counter
from functools import cmp_to_key

card_strengths = "AKQJT98765432"
card_value = {}
for strength, card in enumerate(card_strengths):
    card_value[card] = strength


def get_hand(card):
    card = list(card)
    c = sorted(Counter(card).values(), reverse=1)

    if c == [5]:
        return 'five'
    elif c == [3, 2]:
        return 'full'
    elif c == [4, 1]:
        return 'four'
    elif c == [3, 1, 1]:
        return 'three'
    elif c == [2, 2, 1]:
        return 'two'
    elif c == [2, 1, 1, 1]:
        return 'one'
    elif c == [1, 1, 1, 1, 1]:
        return 'high'


with open('in.txt', 'r') as f:
    cards = {
        'high': [],
        'one': [],
        'two': [],
        'three': [],
        'full': [],
        'four': [],
        'five': [],
    }
    for line in f.readlines():
        card, bid = line.split()
        cards[get_hand(card)].append(
            {
                "card": card, 
                "bid": int(bid),
            }
        )


    rank = 1
    ans = 0
    for hand in cards.keys():
        cards[hand] = sorted(cards[hand], key=lambda card: [card_value[card] for card in card['card']], reverse=True)
        for c in cards[hand]:
            if 'card' in c:
                ans += (rank*c['bid'])
                c['rank'] = rank
                rank +=1
            print((hand, c['bid'], c['card']))


    print(ans)