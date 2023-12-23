import helpers

with open('2023/Inputs/Day23.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

spaces = helpers.listsToPoints(lines)
size = (len(lines), len(lines[0]))
start = (0, lines[0].index('.'))
end = (len(lines)-1, lines[-1].index('.'))

paths = [[start]]
nexts = [(0, (start[0]+1, start[1]))]
roads = {}
intersects = {start}
while len(nexts) > 0:
    next = nexts.pop(-1)
    paths[next[0]].append(next[1])
    adjs = 0
    if next[1] != end:
        adjacents = helpers.getAdjacentPoints(next[1], size)
        path = next[0]
        for dir, adj in adjacents.items():
            if adj not in paths[next[0]] and (spaces[adj] == '.' or (spaces[adj] == 'v' and dir == 'down') or (spaces[adj] == '>' and dir == 'right')):
                if path == len(paths):
                    paths.append(paths[next[0]].copy())
                nexts.append((path, adj))
                path = len(paths)
            if spaces[adj] != '#':
                adjs += 1
    if adjs >= 3 or next[1] == end:
        intersect = None
        for p in paths[next[0]][::-1]:
            if p in intersects and p != next[1]:
                intersect = p
                break
        if intersect not in roads:
            roads[intersect] = {}
        roads[intersect][next[1]] = paths[next[0]].index(next[1]) - paths[next[0]].index(intersect)
        if next[1] not in roads:
            roads[next[1]] = {}
        roads[next[1]][intersect] = paths[next[0]].index(next[1]) - paths[next[0]].index(intersect)
        intersects.add(next[1])
sum1 = max([len(path)-1 for path in paths])
print(f'1. Answer is: {sum1}') # 2174

paths = [[[start], [0]]]
nexts = [(0, list(roads[start].keys())[0], list(roads[start].values())[0])]
while len(nexts) > 0:
    next = nexts.pop()
    paths[next[0]][0].append(next[1])
    paths[next[0]][1].append(next[2])
    # Could curtail paths that share the same last two intersects, but have a shorter distance here
    if next[1] == end:
        continue
    path = next[0]
    for choice, dist in roads[next[1]].items():
        if choice not in paths[next[0]][0]:
            if path == len(paths):
                paths.append([paths[next[0]][0].copy(), paths[next[0]][1].copy()])
            nexts.append((path, choice, dist))
            path = len(paths)
sum2 = max([sum(path[1]) for path in paths])
print(f'2. Answer is: {sum2}') # 6506 takes a couple minutes to run