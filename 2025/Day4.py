import helpers

with open('2025/Inputs/Day4.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

lines = helpers.addBorder(lines)
points = helpers.listsToPoints(lines)

sum1 = 0
for point, value in points.items():
    if value == '@':
        around = 0
        for ray in helpers.getRays(point).values():
            if points[ray[0]] == '@':
                around += 1
        if around < 4:
            sum1 += 1
print(f'1. Answer is: {sum1}') # 1397

def checkRoll(point):
    if points[point] == '@':
        around = 0
        rays = helpers.getRays(point)
        for ray in rays.values():
            if points[ray[0]] == '@':
                around += 1
        if around < 4:
            points[point] = 'x' # remove Roll
            for ray in rays.values():
                checkRoll(ray[0])

sum2 = 0
for point, value in points.items():
    checkRoll(point)
# helpers.printPoints(points)
for point, value in points.items():
    if value == 'x':
        sum2 += 1
print(f'2. Answer is: {sum2}') # 8758
# time: 00:26:37