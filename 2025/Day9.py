import re

with open('2025/Inputs/Day9.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
tiles = []
rectangles = []
for line in lines:
    nums = [int(num) for num in re.findall('\\d+', line)]
    current = (nums[0], nums[1])
    for tile in tiles[:-1]:
        area = (abs(current[0]-tile[0])+1) * (abs(current[1]-tile[1])+1)
        rectangles.append((area, current, tile))
        if area > sum1:
            sum1 = area
    tiles.append(current)
print(f'1. Answer is: {sum1}') # 4729332959

sum2 = 0
verts = []
sides = []
for i in range(len(tiles)):
    j = (i+1) % len(tiles)
    if tiles[i][0] == tiles[j][0]:
        verts.append((tiles[i][0], (tiles[i][1], tiles[j][1])))
    elif tiles[i][1] == tiles[j][1]:
        sides.append((tiles[i][1], (tiles[i][0], tiles[j][0])))
    else:
        print(f'!!! bad edge: {tiles[i]}, {tiles[j]}')
rectangles.sort(reverse=True)
for rect in rectangles:
    green = True
    for vert in verts:
        if (min(rect[1][0], rect[2][0]) < vert[0] < max(rect[1][0], rect[2][0]) and
            not min(vert[1]) >= max(rect[1][1], rect[2][1]) and
            not max(vert[1]) <= min(rect[1][1], rect[2][1]) ):
            green = False
            break
    if not green:
        continue
    for side in sides:
        if (min(rect[1][1], rect[2][1]) < side[0] < max(rect[1][1], rect[2][1]) and
            not min(side[1]) >= max(rect[1][0], rect[2][0]) and
            not max(side[1]) <= min(rect[1][0], rect[2][0]) ):
            green = False
            break
    if green:
        sum2 = rect[0]
        break
print(f'2. Answer is: {sum2}') # 1474477524
# time: 00:59:00