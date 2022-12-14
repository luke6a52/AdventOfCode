with open('2022/Inputs/Day14.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def show_formation():
    minx = 500
    maxx = 500
    for layer in rocks.values():
        minx = min(minx, min(layer))
        maxx = max(maxx, max(layer))
    for y in range(max(rocks.keys()) + 1):
        layer = []
        for x in range(minx, maxx+1):
            if x in rocks.get(y, {}): layer.append('#')
            elif x in sands.get(y, {}): layer.append('o')
            else: layer.append(' ')
        print(''.join(layer))

rocks = {}
for line in lines:
    ends = line.split(' -> ')
    for i in range(len(ends)-1):
        x1, y1 = [int(num) for num in ends[i].split(',')]
        x2, y2 = [int(num) for num in ends[i+1].split(',')]
        if(y1 == y2):
            rocks[y1] = rocks.get(y1, set()).union(range(min(x1,x2), max(x1,x2)+1))
        elif(x1 == x2):
            for y in range(min(y1,y2), max(y1,y2)+1):
                rocks[y] = rocks.get(y, set()).union({x1})
        else:
            assert(False), 'Implement Diagonals.'

sands = {}
count = 0
bottom = max(rocks.keys())
show_formation()
while True:
    sand = [500, 0]
    for y in range(bottom):
        layer = rocks.get(y+1, set()).union(sands.get(y+1, set()))
        if(  sand[0]   not in layer): sand[1] += 1;               continue
        elif(sand[0]-1 not in layer): sand[1] += 1; sand[0] -= 1; continue
        elif(sand[0]+1 not in layer): sand[1] += 1; sand[0] += 1; continue
        else: 
            sands[y] = sands.get(y, set()).union({sand[0]})
            count += 1
            break
    if(sand[1] == bottom):
        break
show_formation()
print(f'1. Answer is: {count}') # 858  1h 34m

bottom = bottom + 2
rocks[bottom] = {*range(500-bottom, 500+bottom+1)}
while True:
    sand = [500, 0]
    for y in range(bottom):
        layer = rocks.get(y+1, set()).union(sands.get(y+1, set()))
        if(  sand[0]   not in layer): sand[1] += 1;               continue
        elif(sand[0]-1 not in layer): sand[1] += 1; sand[0] -= 1; continue
        elif(sand[0]+1 not in layer): sand[1] += 1; sand[0] += 1; continue
        else: 
            sands[y] = sands.get(y, set()).union({sand[0]})
            count += 1
            break
    if(sand[1] == 0):
        break
show_formation()
print(f'2. Answer is: {count}') # 858  1h 34m