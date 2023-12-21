import helpers

with open('2023/Inputs/Day21.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

spaces = helpers.listsToPoints(lines)
size = len(lines)
origin = ((len(lines)-1)//2, (len(lines[0])-1)//2)
spaces[origin] = '.'

# for i in range(size):
#     if all([spaces[(i,j)] == '.' for j in range(size)]):
#         print(f'row {i}')
#     if all([spaces[(j,i)] == '.' for j in range(size)]):
#         print(f'col {i}')

def getStepsFromPoint(point, maxSteps):
    plots = {}
    next = set([point])
    for step in range(maxSteps+1):
        newNext = set()
        for plot in next:
            plots[plot] = step
            adjacents = helpers.getAdjacentPoints(plot, (size, size))
            for adj in adjacents.values():
                if adj is not None and adj not in plots and spaces[adj] == '.':
                    newNext.add(adj)
        next = newNext
        if len(next) == 0:
            break
    return plots

def printPlots(plots):
    print()
    for i in range(size+1):
        temp = ''
        for j in range(size+1):
            if (i,j) in plots:
                temp += f'{plots[(i,j)]:0>2} '
            else:
                temp += '   '
        print(temp)

# Part 1
sum1 = 0
maxSteps = 64
plots = getStepsFromPoint(origin, maxSteps)
#printPlots(plots)
for step in plots.values():
    if step % 2 == 0:
        sum1 += 1
print(f'1. Answer is: {sum1}') # 3716

# Part 2
sum2 = 0
maxSteps = 26501365
plots = getStepsFromPoint(origin, maxSteps)
#printPlots(plots)
for step in plots.values():
    if step % 2 == 1: # !!!maxSteps is odd!!!
        sum2 += 1
starts =  [(0, 0), (origin[0], 0), (size-1, 0), (size-1, origin[1]), (size-1, size-1), (origin[0], size-1), (0, size-1), (0, origin[1])]
sources = [(size-1, size-1), (origin[0], size-1), (0, size-1), (0, origin[1]), (0, 0), (origin[0], 0), (size-1, 0), (size-1, origin[1])]
repeatPlots = []
for i, start in enumerate(starts):
    repeatPlots.append(getStepsFromPoint(start, maxSteps))
    #printPlots(repeatPlots[i])
diagSum = 0
lineSum = 0
diagSteps = {}
lineSteps = {}
for i in range(0, len(starts), 2):
    for plot in plots.keys():
        # Diagonal Triangles
        step = repeatPlots[i][plot] + plots[sources[i]]+2
        diagSteps[step] = diagSteps.get(step, 0) + 1
        # Horizontal and Vertical Lines
        #step = min(repeatPlots[i-2][plot] + plots[sources[i]]+1, repeatPlots[i-1][plot] + plots[sources[i-1]]+1, repeatPlots[i][plot] + plots[sources[i-2]]+1)
        step = repeatPlots[i-1][plot] + plots[sources[i-1]]+1
        #step = min(repeatPlots[i-2][plot] + plots[sources[i]]+1, repeatPlots[i][plot] + plots[sources[i-2]]+1)
        lineSteps[step] = lineSteps.get(step, 0) + 1
# Diagonal Triangles
for step, count in diagSteps.items():
    repeats = (maxSteps - step) // size
    if step % 2 == 1:
        diagSum += count * sum(range(1, repeats+2, 2))
    else:
        diagSum += count * sum(range(0, repeats+2, 2))
# Horizontal and Vertical Lines
for step, count in lineSteps.items():
    repeats = (maxSteps - step) // size
    if step % 2 == 1:
        lineSum += count * (1 + repeats // 2)
    else:
        lineSum += count * ((1 + repeats) // 2)
# print(diagSum)
# print(lineSum)
sum2 += diagSum + lineSum
print(f'2. Answer is: {sum2}')  # 616583483179597 is correct


# Aternative Part 2
sum2 = 0
repeats = maxSteps // size
remains = maxSteps % size
#print(repeats, remains)
if remains != origin[0] and remains % 2 == 1:
    print('!!!ALTERNATIVE IS INVALID!!!')
odds = 0
evens = 0
for space, val in spaces.items():
    if val == '.':
        if sum(space) % 2 == 0:
            evens += 1
        else:
            odds += 1
#print(odds, evens)
for i in range(1, repeats+1):
    sum2 += 4 * i * (evens if i % 2 == 1 else odds)
plots = getStepsFromPoint(origin, remains)
#printPlots(plots)
oddCorners = odds
evenCorners = evens
for step in plots.values():
    if step % 2 == 0:
        evenCorners -= 1
    else:
        sum2 += 1
        oddCorners -= 1
print(odds, oddCorners, odds-oddCorners)
print(evens, evenCorners, evens-evenCorners)
sum2 += (oddCorners - evenCorners) * repeats
print(f'2. Alter  is: {sum2}') # 616828973622697 is wrong
