import helpers

with open('2023/Inputs/Day10.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

points = helpers.listsToPoints(lines)
size = (len(lines), len(lines[0]))
pipes = {'-':('left','right'), '|':('up','down'), 'L':('up','right'), 'J':('left','up'), '7':('left','down'), 'F':('down','right')}
loop = []
for point, value in points.items():
    if value == 'S':
        loop.append(point)
        adjacents = helpers.getAdjacentPoints(point, size)
        if points[adjacents['down']] in {'|', 'L', 'J'}:
            loop.append(adjacents['down'])
        elif points[adjacents['right']] in {'-', '7', 'J'}:
            loop.append(adjacents['right'])
        else:
            loop.append(adjacents['up'])
        break
while points[loop[-1]] != 'S':
    pipe = pipes[points[loop[-1]]]
    nexts = helpers.getAdjacentPoints(loop[-1], size)
    if nexts[pipe[0]] == loop[-2]:
        loop.append(nexts[pipe[1]])
    else:
        loop.append(nexts[pipe[0]])
print(f'1. Answer is: {(len(loop)-1)//2}') # 6831

# def checkSides(point, inside, neither):
#     for next in [(point[0]-1, point[1]), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0], point[1]+1)]:
#         if next not in neither and next not in inside:
#             inside[next] = True
#             checkSides(next, inside, neither)

# inside = {}
# neither = {}
# newStart = loop.index(min(loop))
# newLoop = loop[newStart:-2] + loop[:newStart]
# setLoop = set(loop)
# for k, current in enumerate(newLoop):
#     if k == 0:
#         neither[current] = True # bottom-right corner is inside
#         continue
#     previous = newLoop[k-1]
#     if ((previous[0] < current[0] and points[current] != 'L') or
#             (previous[1] < current[1] and points[current] != '7') or
#             (previous[0] > current[0] and points[previous] != 'L') or
#             (previous[1] > current[1] and points[previous] != '7')):
#         neither[current] = neither[previous]
#     else:
#         neither[current] = not neither[previous]
#     if neither[current]:
#         if (current[0]+1, current[1]) not in setLoop and points[current] in {'-', 'L', 'J'}:
#             inside[(current[0]+1, current[1])] = True
#         if (current[0], current[1]+1) not in setLoop and points[current] in {'|', 'J', '7'}:
#             inside[(current[0], current[1]+1)] = True
#         if (current[0]-1, current[1]) not in setLoop and points[current] == '7':
#             inside[(current[0]-1, current[1])] = True
#         if (current[0], current[1]-1) not in setLoop and points[current] == 'L':
#             inside[(current[0], current[1]-1)] = True
#     else:
#         if (current[0]-1, current[1]) not in setLoop and points[current] in {'-', 'F'}:
#             inside[(current[0]-1, current[1])] = True
#         if (current[0], current[1]-1) not in setLoop and points[current] in {'|', 'F'}:
#             inside[(current[0], current[1]-1)] = True
# for point in list(inside): 
#     checkSides(point, inside, neither)
# print(f'2. Answer is: {len(inside)}') # 305