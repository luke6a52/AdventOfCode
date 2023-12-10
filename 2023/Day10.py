with open('2023/Inputs/Day10.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

points = {}
loop = []
for i, line in enumerate(lines):
    for j, value in enumerate(line):
        points[(i, j)] = value
        if value == 'S':
            loop.append((i, j))
            loop.append((i, j+1)) #cheating
pipes = {'-':((0,-1),(0,1)), '|':((-1,0),(1,0)), 'L':((-1,0),(0,1)), 'J':((0,-1),(-1,0)), '7':((0,-1),(1,0)), 'F':((0,1),(1,0))}
while points[loop[-1]] != 'S':
    back = (loop[-2][0] - loop[-1][0], loop[-2][1] - loop[-1][1])
    pipe = pipes[points[loop[-1]]]
    if pipe[0] == back:
        loop.append((loop[-1][0] + pipe[1][0], loop[-1][1] + pipe[1][1]))
    else:
        loop.append((loop[-1][0] + pipe[0][0], loop[-1][1] + pipe[0][1]))
print(f'1. Answer is: {(len(loop)-1)//2}') # 6831

def checkSides(point, inside, neither):
    for next in [(point[0]-1, point[1]), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0], point[1]+1)]:
        if next not in neither and next not in inside:
            inside[next] = True
            checkSides(next, inside, neither)

inside = {}
neither = {}
newStart = loop.index(min(loop))
newLoop = loop[newStart:-2] + loop[:newStart]
setLoop = set(loop)
for k, current in enumerate(newLoop):
    if k == 0:
        neither[current] = True # bottom-right corner is inside
        continue
    previous = newLoop[k-1]
    if ((previous[0] < current[0] and points[current] != 'L') or
            (previous[1] < current[1] and points[current] != '7') or
            (previous[0] > current[0] and points[previous] != 'L') or
            (previous[1] > current[1] and points[previous] != '7')):
        neither[current] = neither[previous]
    else:
        neither[current] = not neither[previous]
    if neither[current]:
        if (current[0]+1, current[1]) not in setLoop and points[current] in {'-', 'L', 'J'}:
            inside[(current[0]+1, current[1])] = True
        if (current[0], current[1]+1) not in setLoop and points[current] in {'|', 'J', '7'}:
            inside[(current[0], current[1]+1)] = True
        if (current[0]-1, current[1]) not in setLoop and points[current] == '7':
            inside[(current[0]-1, current[1])] = True
        if (current[0], current[1]-1) not in setLoop and points[current] == 'L':
            inside[(current[0], current[1]-1)] = True
    else:
        if (current[0]-1, current[1]) not in setLoop and points[current] in {'-', 'F'}:
            inside[(current[0]-1, current[1])] = True
        if (current[0], current[1]-1) not in setLoop and points[current] in {'|', 'F'}:
            inside[(current[0], current[1]-1)] = True
for point in list(inside): 
    checkSides(point, inside, neither)
print(f'2. Answer is: {len(inside)}') # 305

# TODO Create helper functions for importing points from a list of lists/strings and for getting adjacent points