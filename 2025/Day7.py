import helpers

with open('2025/Inputs/Day7.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]
points = helpers.listsToPoints(lines)

start = None
for point, value in points.items():
    if value == 'S':
        start = point
        break

sum1 = 0
splits = dict()
splits[start] = 1
for i in range(1, len(lines)):
    nexts = dict()
    for split, count in splits.items():
        next = (split[0]+1, split[1])
        if next not in points:
            continue
        elif points[next] == '.':
            nexts[next] = count  + nexts.get(next, 0)
        elif points[next] == '^':
            sum1 += 1
            nexts[(next[0], next[1]-1)] = count + nexts.get((next[0], next[1]-1), 0)
            nexts[(next[0], next[1]+1)] = count + nexts.get((next[0], next[1]+1), 0)
    splits = nexts
    print(splits)
print(f'1. Answer is: {sum1}') # 1662
sum2 = sum(splits.values())
print(f'2. Answer is: {sum2}') # 40941112789504
# time: 00:36:40