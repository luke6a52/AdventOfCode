import re

with open('2023/Inputs/Day19.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def move(part, cmdLine):
    cmds = cmdLine.split(',')
    for j, cmd in enumerate(cmds):
        if j == len(cmds)-1:
            return cmd
        colon = cmd.index(':')
        if cmd[1] == '>':
            if part[cmd[0]] > int(cmd[2:colon]):
                return cmd[colon+1:]
        else:
            if part[cmd[0]] < int(cmd[2:colon]):
                return cmd[colon+1:]

empty = lines.index('')
flowLines = lines[:empty]
flows = {}
for i, line in enumerate(flowLines):
    name, line = line.split('{')
    flows[name] = (lambda part, cmdLine: move(part, cmdLine), line[:-1])
partLines = lines[empty+1:]
partLists = {'in': []}
for i, part in enumerate(partLines):
    nums = [int(num) for num in re.findall('\d+', part)]
    part = dict(zip(['x','m','a','s'], nums))
    partLists['in'].append(part)
nextFlows = set(['in'])
while len(nextFlows) > 0:
    current= nextFlows.pop()
    for part in partLists[current]:
        newFlow = flows[current][0](part, flows[current][1])
        partLists[newFlow] = partLists.get(newFlow, []) + [part]
        if newFlow != 'A' and newFlow != 'R':
            nextFlows.add(newFlow)
    partLists[current] = []
sum1 = sum([sum(part.values()) for part in partLists['A']])
print(f'1. Answer is: {sum1}') # 495298



def sortParts(part, cmdLine):
    newParts = {}
    cmds = cmdLine.split(',')
    for j, cmd in enumerate(cmds):
        if j == len(cmds)-1:
            newParts[cmd] = newParts.get(cmd, []) + [part]
            break
        colon = cmd.index(':')
        newPart = part.copy()
        if cmd[1] == '>':
            newPart[cmd[0]] = (int(cmd[2:colon])+1, newPart[cmd[0]][1])
            part[cmd[0]] = (part[cmd[0]][0], int(cmd[2:colon]))
        else:
            newPart[cmd[0]] = (newPart[cmd[0]][0], int(cmd[2:colon])-1)
            part[cmd[0]] = (int(cmd[2:colon]), part[cmd[0]][1])
        if newPart[cmd[0]][0] <= newPart[cmd[0]][1]:
            newParts[cmd[colon+1:]] = newParts.get(cmd[colon+1:], []) + [newPart]
        if part[cmd[0]][0] > part[cmd[0]][1]:
            break
    return newParts

flows = {}
for i, line in enumerate(flowLines):
    name, line = line.split('{')
    flows[name] = (lambda part, cmdLine: sortParts(part, cmdLine), line[:-1])
partLists = {'in': [{'x':(1,4000), 'm':(1,4000), 'a':(1,4000), 's':(1,4000)}]}
nextFlows = set(['in'])
while len(nextFlows) > 0:
    current= nextFlows.pop()
    for part in partLists[current]:
        newParts = flows[current][0](part, flows[current][1])
        for newFlow, newPart in newParts.items():
            partLists[newFlow] = partLists.get(newFlow, []) + newPart
            if newFlow != 'A' and newFlow != 'R':
                nextFlows.add(newFlow)
    partLists[current] = []
sum2 = 0
for part in partLists['A']:
    combos = 1
    for seg in part.values():
        combos *= seg[1] - seg[0] + 1
    sum2 += combos
print(f'2. Answer is: {sum2}')    # 132186256794011
print(f'      out of: {4000**4}') # 256000000000000