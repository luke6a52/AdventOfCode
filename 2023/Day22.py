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
supports = [set() for b in range(len(bricks))]
supportedBy = [set() for b in range(len(bricks))]
def checkSupports(b, brick): ######################################TODO brick 7 is not being marked unsafe
    for i in range(brick[0][2], brick[1][2]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            k = brick[0][0]
            if k != 1 and k-1 in ground[(i, j)]:
                supportedBy[b].add(ground[(i, j)][k-1])
                supports[ground[(i, j)][k-1]].add(b)
    if len(supportedBy[b]) == 1:
        safes[list(supportedBy[b])[0]] = False
for b, brick in enumerate(bricks):
    checkSupports(b, brick)
for b, safe in enumerate(safes):
    #print(safe, bricks[b])
    if safe:
        sum1 += 1
def printTower():
    for k in range(160,0,-1):
        print(f'{k}------------------------------------------------')
        for i in range(10):
            temp = ''
            for j in range(10):
                if k in ground[(i, j)]:
                    color = '\033[92m' if safes[ground[(i, j)][k]] else '\033[91m'
                    temp += f'{color}{ground[(i, j)][k]:0>4}\033[0m '
                else:
                    temp += '     '
            print(temp)
    print(f'{0}------------------------------------------------')
#printTower()
falls = []
for b, support in enumerate(supports):
    #print(support)
    nexts = support.copy()
    gone = {b}
    while len(nexts) > 0:
        next = nexts.pop()
        if all([under in gone for under in supportedBy[next]]):
            gone.add(next)
            for over in supports[next]:
                nexts.add(over)
    falls.append(len(gone)-1)
print(f'1. Answer is: {sum1}') # 405
print(f'2. Answer is: {sum(falls)}') # 61297