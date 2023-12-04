import re

with open('2023/Inputs/Day4.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
matches = [0] * len(lines)
cards = [1] * len(lines)
for i, line in enumerate(lines):
    (ignore, winLine, haveLine) = re.split(': | \| ', line)
    wins = [int(n) for n in winLine.split()]
    haves = [int(n) for n in haveLine.split()]
    for have in haves:
        if have in wins:
            matches[i] += 1
    if matches[i] > 0:
        sum1 += 2**(matches[i]-1)
    for j in range(i+1, i+1+matches[i]):
        cards[j] += cards[i]
print(f'1. Answer is: {sum1}') # 15268
print(f'2. Answer is: {sum(cards)}') # 6283755