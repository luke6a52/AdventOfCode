import re

with open('2022/Inputs/Day7.txt', 'r') as input_file:
    lines = input_file.readlines()
cmds = [line.rstrip() for line in lines]

dirs = {}
path = []
subDirs = [['/']]
for cmd in cmds:
    left, right = re.match('\$? ?([^ ]+) ?([^ ]+)?', cmd).groups()
    match(left):
        case('cd'):
            if(right == '..'):
                assert(len(subDirs[-1]) == 0), f'Commands are not depth-first! {subDirs[-1]} were abandoned!'
                subDirs.pop()
                lastDir = path.pop()
                dirs[' '.join(path)] += dirs[' '.join(path) + ' ' + lastDir]
            else:
                subDirs[-1].remove(right)
                path.append(right)
                dirs[' '.join(path)] = 0
                subDirs.append([])
        case('ls'):
            pass
        case('dir'):
            subDirs[-1].append(right)
        case(_):
            dirs[' '.join(path)] += int(left)
while(len(path) > 1):
    lastDir = path.pop()
    dirs[' '.join(path)] += dirs[' '.join(path) + ' ' + lastDir]

answer1 = sum([value for value in dirs.values() if value <= 100000])
print(f'1. Answer is: {answer1}') # 1555642   2h 37m
answer2 = min([value for value in dirs.values() if value >= 30000000 - (70000000 - dirs['/'])]) # '/' is 45349983
print(f'2. Answer is: {answer2}') # 5974547   2h 46m