import re

with open('2022/Inputs/Day4.txt', 'r') as input_file:
    lines = input_file.readlines()
pairs = [line.rstrip() for line in lines]

count1 = 0
count2 = 0
for pair in pairs:
    l1, l2, r1, r2 = [int(area) for area in re.split(',|-', pair)]
    if (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2):
        count1 += 1
    if l2 >= r1 and l1 <= r2:
        count2 += 1
print(f'1. Answer is: {count1}') # 605   12m 30s
print(f'2. Answer is: {count2}') # 914   16m 7s