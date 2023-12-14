import helpers

with open('2023/Inputs/Day14.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

spaces = helpers.listsToPoints(lines)

sum1 = 0
rocks = {}
for point, rock in spaces.items():
    if rock == 'O' or rock == '#':
        rocks[point] = rock
starts = list(rocks.keys())
starts.sort()
for point in starts:
    if rocks[point] == 'O':
        x = point[0]
        for i in range(point[0]-1,-1,-1):
            if (i, point[1]) in rocks:
                break
            else:
                x = i
                rocks[(i, point[1])] = rocks.pop((i+1, point[1]))
        sum1 += len(lines) - x
print(f'1. Answer is: {sum1}') # 105784

sum2 = 0
rocks = {}
for point, rock in spaces.items():
    if rock == 'O' or rock == '#':
        rocks[point] = rock
snaps = {}
iters = mod = 1000000000
for k in range(iters):
    #North
    starts = list(rocks.keys())
    starts.sort()
    for point in starts:
        if rocks[point] == 'O':
            for i in range(point[0]-1,-1,-1):
                if (i, point[1]) in rocks:
                    break
                else:
                    rocks[(i, point[1])] = rocks.pop((i+1, point[1]))
    #West
    starts = list(rocks.keys())
    starts.sort()
    for point in starts:
        if rocks[point] == 'O':
            for j in range(point[1]-1,-1,-1):
                if (point[0], j) in rocks:
                    break
                else:
                    rocks[(point[0], j)] = rocks.pop((point[0], j+1))
    #South
    starts = list(rocks.keys())
    starts.sort(reverse=True)
    for point in starts:
        if rocks[point] == 'O':
            for i in range(point[0]+1, len(lines)):
                if (i, point[1]) in rocks:
                    break
                else:
                    rocks[(i, point[1])] = rocks.pop((i-1, point[1]))
    #East
    starts = list(rocks.keys())
    starts.sort(reverse=True)
    for point in starts:
        if rocks[point] == 'O':
            for j in range(point[1]+1, len(lines[0])):
                if (point[0], j) in rocks:
                    break
                else:
                    rocks[(point[0], j)] = rocks.pop((point[0], j-1))
    snap = list(rocks.keys())
    snap.sort()
    if tuple(snap) in snaps:
        mod = k - snaps[tuple(snap)]
        print(k, snaps[tuple(snap)])
    snaps[tuple(snap)] = k
    if (iters-1 - k) % mod == 0:
        break
    # if k % 1000 == 0:
    #     print(k)
for point, rock in rocks.items():
    if rock == 'O':
        sum2 += len(lines) - point[0]
print(f'2. Answer is: {sum2}') #91286

#TODO This feels ridiculously messy, but maybe that's just because North, West, South, and East are so redundant.