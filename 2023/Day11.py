with open('2023/Inputs/Day11.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
gals = []
rows1 = [2] * len(lines)
cols1 = [2] * len(lines[0])
rows2 = [1000000] * len(lines)
cols2 = [1000000] * len(lines[0])
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            gals.append((i,j))
            rows1[i] = cols1[j] = rows2[i] = cols2[j] = 1
for x, start in enumerate(gals):
    for y, end in enumerate(gals[x+1:]):
        sum1 += sum(rows1[min(start[0],end[0]):max(start[0],end[0])]) + sum(cols1[min(start[1],end[1]):max(start[1],end[1])])
        sum2 += sum(rows2[min(start[0],end[0]):max(start[0],end[0])]) + sum(cols2[min(start[1],end[1]):max(start[1],end[1])])
print(f'1. Answer is: {sum1}') # 9522407
print(f'2. Answer is: {sum2}') # 544723432977