with open('2023/Inputs/Day13.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]
    
regions = [[]]
for i, line in enumerate(lines):
    if line == '':
        regions.append([])
    else:
        regions[-1].append(line)

sum1 = 0
for k, rows in enumerate(regions):
    for i in range(1, len(rows)):
        x = 0
        while rows[i+x] == rows[i-1-x]:
            x += 1
            if i+x >= len(rows) or i-1-x < 0:
                sum1 += 100 * i
                break
    cols = []
    for j in range(len(rows[0])):
        cols.append(''.join([row[j] for row in rows]))
    for j in range(1, len(cols)):
        y = 0
        while cols[j+y] == cols[j-1-y]:
            y += 1
            if j+y >= len(cols) or j-1-y < 0:
                sum1 += j
                break
print(f'1. Answer is: {sum1}') # 34202

sum2 = 0
for k, rows in enumerate(regions):
    for i in range(1, len(rows)):
        diffs = 0
        x = 0
        for x in range(len(rows)-i):
            for j, c in enumerate(rows[i+x]):
                if c != rows[i-1-x][j]:
                    diffs += 1
                    if diffs > 1:
                        break
            if diffs == 1 and (i+x+1 >= len(rows) or i-2-x < 0):
                sum2 += 100 * i
                break
    cols = []
    for j in range(len(rows[0])):
        cols.append(''.join([row[j] for row in rows]))
    for j in range(1, len(cols)):
        diffs = 0
        y = 0
        for y in range(len(cols)-j):
            for i, c in enumerate(cols[j+y]):
                if c != cols[j-1-y][i]:
                    diffs += 1
                    if diffs > 1:
                        break
            if diffs == 1 and (j+y+1 >= len(cols) or j-2-y < 0):
                sum2 += j
                break
print(f'2. Answer is: {sum2}') # 34230

#TODO create a Transpose function, and possibly a diffs function. Then clean up this file.