import re

with open('2022/Inputs/Day15.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def getDistance(point1, point2):
    return abs(point2[0] - point1[0]) +abs(point2[1] - point1[1])

limit = 4000000
y = limit // 2
beacons = set()
sensors = []
for line in lines:
    sensor, beacon = re.findall('x=([-\d]+), y=([-\d]+)', line)
    sensor = [int(coord) for coord in sensor]
    beacon = [int(coord) for coord in beacon]
    distance = getDistance(sensor, beacon)
    sensors.append((sensor[0], sensor[1], distance))
    if beacon[1] == y:
        beacons.add(beacon[0])

def checkRow(y):
    row = (limit, 0)
    segments = []
    for sensor in sensors:
        remainder = sensor[2] - abs(y - sensor[1])
        if remainder >= 0:
            segments.append((sensor[0] - remainder, sensor[0] + remainder))
    segments.sort() # by x (then y)
    for segment in segments:
        if segment[0] > row[1] + 1:
            print(y, row[1], segment[0])
            return segment[0] - 1
        row = (min(row[0], segment[0]), max(row[1], segment[1]))
    return row

middle = checkRow(y)
print(f'1. Answer is: {middle[1] - middle[0] + 1 - len(beacons)}') # 5108096   28m 6s

for y in range(limit+1):
    x = checkRow(y)
    if isinstance(x, int):
        break
print(f'2. Answer is: {x*4000000 + y}') # 10553942650264   ~5h

# The following part 2 takes too long to run.
# I'm not sure it is even implemented correctly, because in 10 minutes it didn't even get past the first pair of sensors.
# Even though it only checks all of the border points instead of ALL the points, there are still millions of border points per sensor.
# borders = []
# for x, y, d in sensors:
#     x_max = x + d + 1
#     x_min = x - d - 1
#     y_max = y + d + 1
#     y_min = y - d - 1
#     borders.append(
#         [(x_max - y + j, j) for j in range(max(y_min, 0), min(y, limit - x_max + y + 1))] +
#         [(x_max + y - j, j) for j in range(max(y, x_max - limit + y), min(y_max, limit + 1))] +
#         [(x_min - y + j, j) for j in range(min(y_max, limit), max(y, -x_min + y - 1), -1)] +
#         [(x_min + y - j, j) for j in range(min(y, x_min + y), max(y_min, -1), -1)] )
# for i, first in enumerate(sensors):
#     for j, second in enumerate(sensors[0:i]):
#         print(i, j, len(borders[i]), len(borders[j]))
#         if(first[2] + second[2] + 1 >= getDistance(first, second)):
#             for point in reversed(borders[i]):
#                 if(second[2] >= getDistance(second, point)): borders[i].remove(point)
#             for point in reversed(borders[j]):
#                 if(first[2] >= getDistance(first, point)): borders[j].remove(point)

# print(borders)
# for border in borders:
#     if(len(border) > 0):
#         beacon = border[0]
#         break
# print(f'2. Answer is: {beacon[0]*40000000 + beacon[1]}')