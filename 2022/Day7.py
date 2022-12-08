with open('2022/Inputs/Day7.txt', 'r') as input_file:
    lines = input_file.readlines()
cmds = [line.rstrip() for line in lines]
dirs = {}

def getSize(dir):
    i = cmds.index(f'$ cd {dir}') + 2
    dirs[dir] = 0
    while i < len(cmds) and cmds[i][0] != '$':
        size, name = cmds[i].split()
        if(size.isnumeric()):
            dirs[dir] += int(size)
        else:
            dirs[dir] += getSize(name)
        i += 1
    return dirs[dir]

getSize('/')
answer1 = sum([value for value in dirs.values() if value <= 100000])
print(f'1. Answer is: {answer1}') #    1h
#print(f'2. Answer is: {answer2}') # 2308   25m 38s