import helpers

with open('2023/Inputs/Day17.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

spaces = helpers.listsToPoints(lines)
size = (len(lines), len(lines[0]))

sum1 = 0
start = (0,0)
end = (size[0]-1, size[1]-1)
fill = {(start, ('', '', '')): 0}
edge = {(start, ('', '', '')): 0}
while sum1 == 0:
    point, dirs = min(edge, key=edge.get)
    loss = edge.pop((point, dirs))
    nexts = helpers.getAdjacentPoints(point, size)
    for dir, next in nexts.items():
        if next == None or all([dir == d for d in dirs]) or (dirs[2] and dir == {'down':'up', 'up':'down', 'right':'left', 'left':'right'}[dirs[2]]):
            continue
        nextLoss = loss + int(spaces[next])
        nextKey = (next, (dirs[1], dirs[2], dir))
        if nextKey not in fill or nextLoss < fill[nextKey]:
            edge[nextKey] = nextLoss
            fill[nextKey] = nextLoss
        if next == end:
            sum1 = nextLoss
            break
print(f'1. Answer is: {sum1}') # 1256 takes a few minutes

sum2 = 0
start = (0,0)
end = (size[0]-1, size[1]-1)
fill = {(start, ('right', 0)): 0}
edge = {(start, ('right', 0)): 0}
while sum2 == 0:
    point, dirIn = min(edge, key=edge.get)
    loss = edge.pop((point, dirIn))
    nexts = helpers.getAdjacentPoints(point, size)
    for dirOut, next in nexts.items():
        if (next == None or 
            (dirOut == dirIn[0] and dirIn[1] >= 10) or
            (dirOut != dirIn[0] and dirIn[1] < 4) or
            dirOut == {'down':'up', 'up':'down', 'right':'left', 'left':'right'}[dirIn[0]]):
            continue
        nextLoss = loss + int(spaces[next])
        nextKey = (next, (dirOut, 1 if dirOut != dirIn[0] else dirIn[1] + 1))
        if nextKey not in fill or nextLoss < fill[nextKey]:
            edge[nextKey] = nextLoss
            fill[nextKey] = nextLoss
        if next == end and nextKey[1][1] >= 4:
            sum2 = nextLoss
            break
print(f'2. Answer is: {sum2}') # 1382 takes a few minutes