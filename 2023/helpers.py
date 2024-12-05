# helper functions for 2D grids

def listsToPoints(lists):
    points = {}
    for i, list in enumerate(lists):
        for j, value in enumerate(list):
            points[(i, j)] = value
    return points

def getAdjacentPoints(point, size):
    adjacents = {'down'      : (point[0]+1, point[1]  ),
                 'right'     : (point[0]  , point[1]+1),
                 'up'        : (point[0]-1, point[1]  ),
                 'left'      : (point[0]  , point[1]-1)}
    for dir in adjacents:
        if not (0 <= adjacents[dir][0] < size[0] and 0 <= adjacents[dir][1] < size[1]):
            adjacents[dir] = None
    return adjacents

# other functions
# Binary Search
# Min distance
# Range overlaps
# Quadratic Equation
# Chinese Remainder Theorem?
