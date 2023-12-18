import re
import math
import helpers

with open('2023/Inputs/Day18.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
start = (200,150)
size = (350,500)
loop = [start]
dirs = {'D':'down', 'R':'right', 'U':'up', 'L':'left'}
for i, line in enumerate(lines):
    dir, dist, color = line.split()
    dir = dirs[dir]
    for i in range(int(dist)):
        adjacents = helpers.getAdjacentPoints(loop[-1], size)
        loop.append(adjacents[dir])

inside = set()
boundary = {}
newStart = loop.index(min(loop))
newLoop = loop[newStart:-1] + loop[:newStart]
setLoop = set(loop)
for k, current in enumerate(newLoop):
    if k in (0, 1, len(newLoop)-1, len(newLoop)-2):
        boundary[current] = True # bottom-right corner is inside
        continue
    next = newLoop[k+1]
    previous = newLoop[k-1]
    prev = newLoop[k-2]
    adjacents = helpers.getAdjacentPoints(current, size)
    if ((previous == adjacents['up'] and next != adjacents['right']) or
        (previous == adjacents['left'] and next != adjacents['down']) or
        (previous == adjacents['down'] and prev != adjacents['down-right']) or
        (previous == adjacents['right'] and prev != adjacents['down-right'])):
        boundary[current] = boundary[previous]
    else:
        boundary[current] = not boundary[previous]
    if boundary[current] and adjacents['down-right'] not in setLoop:
        inside.add(adjacents['down-right'])
starts = inside.copy()

newLines = []
for i in range(size[0]):
    newLine = ''
    for j in range(size[1]):
        if (i,j) in boundary:
            newLine += '#' if boundary[(i,j)] else '.'
        else:
            newLine += ' '
    newLine += '\n'
    newLines.append(newLine)
with open('2023/Inputs/temp.txt', 'w') as output_file:
    output_file.writelines(newLines)

print(newLoop)
while len(starts) > 0:
    point = starts.pop()
    adjacents = set(helpers.getAdjacentPoints(point, size).values())
    while len(adjacents) > 0:
        next = adjacents.pop()
        if next in starts:
            starts.remove(next)
        elif next not in boundary and next not in inside:
            inside.add(next)
            for adj in helpers.getAdjacentPoints(next,size).values():
                adjacents.add(adj)
print(f'1. Answer is: {len(inside)+len(boundary)}') # 62365
print(f'2. Answer is: {sum2}') #

# rows = {}
# cols = {}
# for point in edge[1:]:
#     if point[0] in rows:
#         rows[point[0]].append(point[1])
#     else:
#         rows[point[0]] = [point[1]]
#     if point[1] in cols:
#         cols[point[1]].append(point[0])
#     else:
#         cols[point[1]] = [point[0]]
# for i, row in rows.items():
#     if i == min(rows.keys()) or i == max(rows.keys()):
#         sum1 += len(row)
#         continue
#     row.sort()
#     inside = False
#     for j in range(row[0], row[-1]+1):
#         if j in row and j-1 not in row:
#             inside = not inside
#         if inside or j in row:
#             sum1 += 1