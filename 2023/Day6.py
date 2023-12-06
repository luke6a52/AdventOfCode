import re

with open('2023/Inputs/Day6.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

times = [int(n) for n in re.findall('\d+', lines[0])]
dists = [int(n) for n in re.findall('\d+', lines[1])]
prod1 = 1
for i, ignore in enumerate(times):
    count1 = 0
    for j in range(1, times[i]):
        if j*(times[i]-j) > dists[i]:
            count1 = times[i]-j*2+1
            break
    prod1 = prod1 * count1
print(f'1. Answer is: {prod1}') # 4403592

time = int(''.join(re.findall('\d+', lines[0])))
dist = int(''.join(re.findall('\d+', lines[1])))
# count2 = 0
# for j in range(1, time):
#     if j*(time-j) > dist:
#         count2 = time-j*2+1
#         break
# print(f'2. Answer is: {count2}') # 38017587

# O(1) alternative
import math
cross = math.ceil((time - math.sqrt(time**2 - 4*dist))/2)
print(f'2. Answer is: {time-cross*2+1}') # 38017587