import re

with open('2023/Inputs/Day2.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
for i, line in enumerate(lines):
    reds = [int(c) for c in re.findall('\d+(?= red)', line)]
    greens = [int(c) for c in re.findall('\d+(?= green)', line)]
    blues = [int(c) for c in re.findall('\d+(?= blue)', line)]
    if max(reds) <= 12 and max(greens) <= 13 and max(blues) <= 14:
        sum1 += i + 1
    sum2 += max(reds) * max(greens) * max(blues)
print(f'1. Answer is: {sum1}') # 2256
print(f'2. Answer is: {sum2}') # 74229