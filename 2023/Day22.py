import re
import math
import helpers

with open('2023/Inputs/Day22.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
bricks = []
for i, line in enumerate(lines):
    start, end = line.split('~')
    bricks.append(([int(n) for n in start.split(',')[-1::-1]], [int(n) for n in end.split(',')[-1::-1]])) # (z,y,x), (z,y,x)
    for j in [2,1,0]:
        if bricks[i][1][j] < bricks[i][0][j]:
            bricks[i] = bricks[i][1::-1]
bricks.sort()
ground = {}
for i in range(10):
    for j in range(10):
        ground[(i, j)] = {0: None}
for b, brick in enumerate(bricks):
    fall = brick[0][0]
    for i in range(brick[0][2], brick[1][2]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            fall = min(brick[0][0]-(max(ground[(i, j)].keys())+1), fall)
    brick[0][0] -= fall
    brick[1][0] -= fall
    for i in range(brick[0][2], brick[1][2]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            for k in range(brick[0][0], brick[1][0]+1):
                ground[(i, j)][k] = b
# for i in range(10):
#     print([ground[(i, j)] for j in range(10)])
safes = [True] * len(bricks)
def checkSupports(brick):
    support = None
    for i in range(brick[0][2], brick[1][2]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            k = brick[0][0]
            if k-1 in ground[(i, j)]:
                if support is None:
                    support = ground[(i, j)][k-1]
                else:
                    return
    if support is not None:
        safes[support] = False
for b, brick in enumerate(bricks):
    checkSupports(brick)
for b, safe in enumerate(safes):
    #print(safe, bricks[b])
    if safe:
        sum1 += 1
print(f'1. Answer is: {sum1}') # 598 is too high
print(f'2. Answer is: {sum2}') #