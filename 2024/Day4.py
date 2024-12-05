import helpers

with open('2024/Inputs/Day4.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

lines = helpers.addBorder(lines, 3)
points = helpers.listsToPoints(lines)

sum1 = 0
for point, value in points.items():
    if value == 'X':
        # (i, j) = point
        # sum1 += points[(i  ,j+1)] + points[(i  ,j+2)] + points[(i  ,j+3)] == 'MAS'
        # sum1 += points[(i+1,j+1)] + points[(i+2,j+2)] + points[(i+3,j+3)] == 'MAS'
        # sum1 += points[(i+1,j  )] + points[(i+2,j  )] + points[(i+3,j  )] == 'MAS'
        # sum1 += points[(i+1,j-1)] + points[(i+2,j-2)] + points[(i+3,j-3)] == 'MAS'
        # sum1 += points[(i  ,j-1)] + points[(i  ,j-2)] + points[(i  ,j-3)] == 'MAS'
        # sum1 += points[(i-1,j-1)] + points[(i-2,j-2)] + points[(i-3,j-3)] == 'MAS'
        # sum1 += points[(i-1,j  )] + points[(i-2,j  )] + points[(i-3,j  )] == 'MAS'
        # sum1 += points[(i-1,j+1)] + points[(i-2,j+2)] + points[(i-3,j+3)] == 'MAS'
        for dir, ray in helpers.getRays(point, 3).items():
            sum1 += ''.join([points[p] for p in ray]) == 'MAS'
print(f'1. Answer is: {sum1}') # 2554

sum2 = 0
for (i, j), value in points.items():
    if value == 'A':
        corners = points[(i+1,j+1)] + points[(i+1,j-1)] + points[(i-1,j-1)] + points[(i-1,j+1)]
        # rays = helpers.getRays((i, j))
        # corners = ''.join([points[p] for p in rays['downright'] + rays['downleft'] + rays['upleft'] + rays['upright']])
        sum2 += 'MMSS' in corners+corners
print(f'2. Answer is: {sum2}') # 1916