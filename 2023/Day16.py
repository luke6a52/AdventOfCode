import helpers

with open('2023/Inputs/Day16.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]
    
spaces = helpers.listsToPoints(lines)

def countEnergy(start):
    tips = [start]
    lights = {start[0] : [start[1]]}
    while len(tips) > 0:
        tip = tips.pop(0)
        space = spaces[tip[0]]
        dirIn = tip[1]
        adjacents = helpers.getAdjacentPoints(tip[0], (len(lines), len(lines[0])))
        if space == '\\':
            dirOuts = [{'right':'down', 'down':'right', 'left':'up', 'up':'left'}[dirIn]]
        elif space == '/':
            dirOuts = [{'right':'up', 'up':'right', 'left':'down', 'down':'left'}[dirIn]]
        elif space == '|':
            dirOuts = ['down','up']
        elif space == '-':
            dirOuts = ['right','left']
        else:
            dirOuts = [dirIn]
        for dir in dirOuts: 
            next = adjacents[dir]
            if next is not None and dir not in lights.get(next, []):
                tips.append((next, dir))
                lights[next] = lights.get(next, []) + [dir]
    return len(lights)

starts = []
for i, row in enumerate(lines):
    starts.append(((i, 0), 'right'))
    starts.append(((i, len(lines[0])-1), 'left'))
for j, col in enumerate(lines[0]):
    starts.append(((0, j), 'down'))
    starts.append(((len(lines)-1, j), 'up'))
print(f'1. Answer is: {countEnergy(starts[0])}') # 7632
print(f'2. Answer is: {max([countEnergy(start) for start in starts])}') # 8023