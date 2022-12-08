import math

with open('2022/Inputs/Day8.txt', 'r') as input_file:
    lines = input_file.readlines()
rows = [line.rstrip() for line in lines]

visible1 = 0;
for i in range(len(rows)):
    for j in range(len(rows[i])):
        current = rows[i][j]
        if(all(current > row[j] for row in rows[:i])):
            visible1 += 1
            continue
        if(all(current > row[j] for row in rows[:i:-1])):
            visible1 += 1
            continue
        if(all(current > tree for tree in rows[i][:j])):
            visible1 += 1
            continue
        if(all(current > tree for tree in rows[i][:j:-1])):
            visible1 += 1
            continue
print(f'1. Answer is: {visible1}') # 1832   25m 1s

visible2 = 0;
for i in range(1,len(rows)-1):
    for j in range(1,len(rows[i])-1):
        current = rows[i][j]
        score = [0,0,0,0]
        for row in rows[i-1::-1]:
            score[0] += 1
            if(row[j] >= current): break
        for row in rows[i+1:]:
            score[1] += 1
            if(row[j] >= current): break
        for tree in rows[i][j-1::-1]:
            score[2] += 1
            if(tree >= current): break
        for tree in rows[i][j+1:]:
            score[3] += 1
            if(tree >= current): break
        visible2 = max(visible2, math.prod(score))

print(f'2. Answer is: {visible2}') # 157320   58m 22s