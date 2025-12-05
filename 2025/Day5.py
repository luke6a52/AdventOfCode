import re

with open('2025/Inputs/Day5.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

ranges1 = []
ids = False
sum1 = 0
empty = lines.index('')
for line in lines[:empty]:
    nums = [int(num) for num in re.findall('\d+', line)] # type: ignore
    ranges1.append([nums[0], nums[1]])
for line in lines[empty+1:]:
    num = [int(num) for num in re.findall('\d+', line)][0] # type: ignore
    for ran in ranges1:
         if ran[0] <= num <= ran[1]:
            sum1 += 1
            break
print(f'1. Answer is: {sum1}') # 848

sum2 = 0
ranges2 = []
ranges1.sort(key=lambda ran1: ran1[0])
for ran1 in ranges1:
    intersects = False
    for i, ran2 in enumerate(ranges2):
        if ran1[0] <= ran2[1]:
            ranges2[i][1] = max(ran1[1], ran2[1])
            intersects = True
            break
    if not intersects:
        ranges2.append(ran1)
for ran2 in ranges2:
    sum2 += ran2[1]-ran2[0]+1
print(f'2. Answer is: {sum2}') # 334714395325710
# time: 00:19:34