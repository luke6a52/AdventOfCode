import re

with open('2023/Inputs/Day5.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

seeds = [int(n) for n in lines[0].split(' ')[1:]]
maps = []
sum2 = 0
for i, line in enumerate(lines[2:]):
    if line == '':
        continue
    elif line[0].isalpha():
        maps.append([])
    else:
        maps[-1].append([int(n) for n in line.split()])

locs1 = []
for seed in seeds:
    for map in maps:
        for sect in map:
            if sect[1] <= seed < sect[1] + sect[2]:
                seed = sect[0] + seed - sect[1]
                break
    locs1.append(seed)
print(f'1. Answer is: {min(locs1)}') # 31599214

ranges = []
for i, seed in enumerate(seeds):
    if i % 2 == 0:
        ranges.append([seeds[i]])
    else:
        ranges[-1].append(seeds[i])
for map in maps:
    i = 0
    while i < len(ranges):
        for sect in map:
            pre  = [min(ranges[i][0], sect[1]          ), min(ranges[i][0] + ranges[i][1] - 1, sect[1] - 1          )]
            over = [max(ranges[i][0], sect[1]          ), min(ranges[i][0] + ranges[i][1] - 1, sect[1] + sect[2] - 1)]
            post = [max(ranges[i][0], sect[1] + sect[2]), max(ranges[i][0] + ranges[i][1] - 1, sect[1] + sect[2] - 1)]
            if over[1] > over[0]:
                ranges[i] =       [over[0] + sect[0] - sect[1], over[1] - over[0] + 1]
                if pre[1] > pre[0]:
                    ranges.append([pre[0]                     , pre[1]  - pre[0]  + 1])
                if post[1] > post[0]:
                    ranges.append([post[0]                    , post[1] - post[0] + 1])
                break
        i += 1
print(f'2. Answer is: {min(ran[0] for ran in ranges)}') # 20358599

# # Took too long
# minLoc2 = max(seeds) * 10 
# for ran in ranges:
#     for seed in range(ran[0], ran[0] + ran[1]):
#         for map in maps:
#             for sect in map:
#                 if sect[1] <= seed < sect[1] + sect[2]:
#                     seed = sect[0] + seed - sect[1]
#                     break
#         if seed < minLoc2:
#             minLoc2 = seed
# print(f'2. Answer is: {minLoc2}')