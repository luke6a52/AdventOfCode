import re

with open('2023/Inputs/Day8.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

instructs = lines[0]
directs = {'L':0, 'R':1}
nodes = {}
for i, line in enumerate(lines[2:]):
    node = re.findall('[A-Z]{3}', line)
    nodes[node[0]] = (node[1], node[2])

node1 = 'AAA'
steps1 = 0
while node1 != 'ZZZ':
    node1 = nodes[node1][directs[instructs[steps1 % len(instructs)]]]
    steps1 += 1
print(f'1. Answer is: {steps1}') # 17141

node2s = []
for node in nodes:
    if node[2] == 'A':
        node2s.append(node)
steps2 = [0] * len(node2s)
prod2 = 1
for i, ignore in enumerate(node2s):
    while node2s[i][2] != 'Z':
        node2s[i] = nodes[node2s[i]][directs[instructs[steps2[i] % len(instructs)]]]
        steps2[i] += 1                           # How do we know there is only one repeating pattern?
    prod2 = prod2 * steps2[i] // len(instructs)  # How do we know these are prime numbers (times length of instructions)?
print(f'2. Answer is: {prod2 * len(instructs)}') # 10818234074807