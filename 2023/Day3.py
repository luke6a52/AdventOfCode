import re

with open('2023/Inputs/Day3.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
parts = []
for i, line in enumerate(lines):
    nums = re.findall('\d+', line)
    j = 0
    for num in nums:
        j = line.find(num, j)
        parts.append([num, i, j, False])
        j += len(num)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char not in '.0123456789':
            gears = []
            for part in parts:
                if part[1]-1 <= i <= part[1]+1 and part[2]-1 <= j <= part[2]+len(part[0]):
                    part[3] = True
                    gears.append(int(part[0]))
            if char == '*' and len(gears) == 2:
                sum2 += gears[0]*gears[1]
for part in parts:
    if part[3]:
        sum1 += int(part[0])
print(f'1. Answer is: {sum1}') # 521601
print(f'2. Answer is: {sum2}') # 80694070

# Alternate
from .. import helpers
points = helpers.listsToPoints(lines)
print(points[-1])