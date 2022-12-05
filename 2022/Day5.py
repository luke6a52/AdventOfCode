import re
import copy

with open('2022/Day5.txt', 'r') as input_file:
    lines = input_file.readlines()
blank = lines.index('\n')
indices = lines[blank-1].rstrip()

stacks1 = []
for j in range(len(indices)):
    if re.match('[1-9]',indices[j]):
        stacks1.append([])
        for i in reversed(range(blank-1)):
            if re.match('[A-Z]',lines[i][j]):
                stacks1[int(indices[j])-1].append(lines[i][j])
print(f'0. Before moving: {stacks1}')
stacks2 = copy.deepcopy(stacks1)

for line in lines[blank+1:]:
    count, source, dest = [int(match) for match in re.findall('\d+', line)]
    source -= 1
    dest -= 1
    for i in range(count):
        stacks1[dest].append(stacks1[source].pop())
    for i in range(-count,0):
        stacks2[dest].append(stacks2[source].pop(i)) # assumes source != dest
print(f'1. After moving : {stacks1}')
print(f'2. After moving : {stacks1}')

answer1 = ''.join([stack[-1] for stack in stacks1])
print(f'1. Answer is: {answer1}') # WCZTHTMPS
# 51m
answer2 = ''.join([stack[-1] for stack in stacks2])
print(f'2. Answer is: {answer2}') # BLSGJSDTS
# 1h 18m 12s