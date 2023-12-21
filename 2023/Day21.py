import helpers

with open('2023/Inputs/Day21.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

spaces = helpers.listsToPoints(lines)
size = len(lines)
start = ((len(lines)-1)//2, (len(lines[0])-1)//2)
spaces[start] = '.'

def getStepsFromPoints(point, maxSteps):
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

sum1 = 0
maxSteps = 64
plots = getStepsFromPoints(start, maxSteps)
for step in plots.values():
    if step % 2 == 0:
        sum1 += 1
print(f'1. Answer is: {sum1}') # 3716

sum2 = 0
maxSteps = 26501365
plots = getStepsFromPoints(start, maxSteps)
#printPlots(plots)
for step in plots.values():
    if step % 2 == 0:
        sum2 += 1
corners = [(0, 0), (size-1,0), (size-1, size-1), (0, size-1)]
repeatPlots = []
for i, start in enumerate(corners):
    repeatPlots.append(getStepsFromPoints(start, maxSteps))
    printPlots(repeatPlots[i])
sources = [(size-1, size-1), (0, size-1), (0, 0), (size-1, 0)]
for i, start in enumerate(corners):
    # diagSteps = {}
    # horVerSteps = {}
    for plot, step in repeatPlots[i].items():
        # Diagonal Triangles
        step1 = step + plots[sources[i]]+2
        repeats1 = (maxSteps - step1) // size
        temp = sum2
        if step1 % 2 == 0:
            sum2 += sum(range(1, repeats1+2, 2))
        else:
            sum2 += sum(range(0, repeats1+2, 2))
        # Horizontal and Vertical Lines
        step2 = min(repeatPlots[i-1][plot] + plots[sources[i]]+1, repeatPlots[i][plot] + plots[sources[i-1]]+1)
        repeats2 = (maxSteps - step2) // size
        if step2 % 2 == 0:
            sum2 += 1 + repeats2 // 2
        else:
            sum2 += (1 + repeats2) // 2
print(f'2. Answer is: {sum2}') # 616583450594350 is too low