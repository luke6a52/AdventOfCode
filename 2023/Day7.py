with open('2023/Inputs/Day7.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
hands = []
values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
for i, line in enumerate(lines):
    cards, bid = line.split()
    bid = int(bid)
    value = 0
    occurs = {}
    for j, card in enumerate(cards):
        occurs[card] = occurs.get(card,0) + 1
        if card.isalpha():
            value += values[card] * 10**(8-j*2)
        else:
            value += int(card) * 10**(8-j*2)
    for count in occurs.values():
        value += (count-1)**2 * 10**10
    hands.append([value, cards, bid])
hands.sort()
for i, hand in enumerate(hands):
    sum1 += (i+1) * hand[2]
print(f'1. Answer is: {sum1}') # 248217452

sum2 = 0
hands = []
values = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10}
for i, line in enumerate(lines):
    cards, bid = line.split()
    bid = int(bid)
    value = 0
    occurs = {}
    for j, card in enumerate(cards):
        occurs[card] = occurs.get(card,0) + 1
        if card.isalpha():
            value += values[card] * 10**(8-j*2)
        else:
            value += int(card) * 10**(8-j*2)
    jokers = occurs.pop('J', 0)
    if jokers == 5:
        occurs['J'] = 0
    occurs[max(occurs, key=occurs.get)] += jokers
    for count in occurs.values():
        value += (count-1)**2 * 10**10
    hands.append([value, cards, bid])
hands.sort()
for i, hand in enumerate(hands):
    sum2 += (i+1) * hand[2]
print(f'2. Answer is: {sum2}') # 245576185