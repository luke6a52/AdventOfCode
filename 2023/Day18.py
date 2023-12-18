import helpers

with open('2023/Inputs/Day18.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
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

# newLines = []
# for i in range(size[0]):
#     newLine = ''
#     for j in range(size[1]):
#         if (i,j) in boundary:
#             newLine += '#' if boundary[(i,j)] else '.'
#         else:
#             newLine += ' '
#     newLine += '\n'
#     newLines.append(newLine)
# with open('2023/Inputs/temp.txt', 'w') as output_file:
#     output_file.writelines(newLines)

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

# Should probably do part 1 like this as well
sum2 = 0
horizontals = {}
verticals = {}
current = (0,0)
for i, line in enumerate(lines):
    dir, dist, color = line.split()
    dist = int(color[2:7], 16)
    dir = int(color[7])
    if dir == 0:
        horizontals[current[0]] = horizontals.get(current[0], []) + [(current[1], current[1]+dist)]
        current = (current[0], current[1]+dist)
    elif dir == 1:
        verticals[current[1]] = verticals.get(current[1], []) + [(current[0], current[0]+dist)]
        current = (current[0]+dist, current[1])
    elif dir == 2:
        horizontals[current[0]] = horizontals.get(current[0], []) + [(current[1]-dist, current[1])]
        current = (current[0], current[1]-dist)
    elif dir == 3:
        verticals[current[1]] = verticals.get(current[1], []) + [(current[0]-dist, current[0])]
        current = (current[0]-dist, current[1])
    else:
        print(f'ERROR: {line}')
horKeys = list(horizontals.keys())
horKeys.sort()
verKeys = list(verticals.keys())
verKeys.sort()
for i, horKey in enumerate(horKeys):
    # sum first row
    if i == 0:
        sum2 += sum([seg[1] - seg[0] + 1 for seg in horizontals[horKey]])
        continue
    # sum all rows since the last horizontal segment(s)
    height = horKey-1 - horKeys[i-1]
    walls = []
    for j, verKey in enumerate(verKeys):
        for seg in verticals[verKey]:
            if seg[0] <= horKey-1 <= seg[1]:
                walls.append(verKey)
                break
    sum2 += height * sum([walls[j+1] - walls[j] + 1 for j in range(0, len(walls), 2)])
    # sum this row
    walls = []
    lastCorner = ''
    for j, verKey in enumerate(verKeys):
        for seg in verticals[verKey]:
            if seg[0] < horKey < seg[1]:
                walls.append(verKey)
                break
            elif seg[0] == horKey:
                if lastCorner == 'bottom':
                    if len(walls) % 2 == 0:
                        walls[-1] = verKey
                    lastCorner = ''
                elif lastCorner == 'top':
                    if len(walls) % 2 == 0:
                        walls[-1] = verKey-1
                    lastCorner = ''
                    walls.append(verKey)
                else:
                    lastCorner = 'top'
                    walls.append(verKey)
                break
            elif horKey == seg[1]:
                if lastCorner == 'top':
                    if len(walls) % 2 == 0:
                        walls[-1] = verKey
                    lastCorner = ''
                elif lastCorner == 'bottom':
                    if len(walls) % 2 == 0:
                        walls[-1] = verKey-1
                    lastCorner = ''
                    walls.append(verKey)
                else:
                    lastCorner = 'bottom'
                    walls.append(verKey)
                break
    print(horKey, walls)
    sum2 += sum([walls[j+1] - walls[j] + 1 for j in range(0, len(walls), 2)])
print(f'2. Answer is: {sum2}') # 159485361249806
