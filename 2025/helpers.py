# helper functions for 2D grids

def addBorder(lists, width=1, blank=' '):
    margin = ''.join([blank for z in lists[0]])
    border = [margin for n in range(width)]
    lists = border + lists + border
    blanks = ''.join([blank for n in range(width)])
    for i in range(len(lists)):
        lists[i] = blanks + lists[i] + blanks
    return lists

def listsToPoints(lists):
    points = {}
    for i, list in enumerate(lists):
        for j, value in enumerate(list):
            points[(i, j)] = value
    return points

def getRays(start, length=1):
    (i, j) = start
    rays = {'right': [], 'downright': [], 'down': [], 'downleft': [], 'left': [], 'upleft': [], 'up': [], 'upright': []}
    for n in range(1, length+1):
        rays['right'    ].append((i  ,j+n))
        rays['downright'].append((i+n,j+n))
        rays['down'     ].append((i+n,j  ))
        rays['downleft' ].append((i+n,j-n))
        rays['left'     ].append((i  ,j-n))
        rays['upleft'   ].append((i-n,j-n))
        rays['up'       ].append((i-n,j  ))
        rays['upright'  ].append((i-n,j+n))
    return rays

# other functions
# Binary Search
# Min distance
# Range overlaps
# Quadratic Equation
# Chinese Remainder Theorem?
