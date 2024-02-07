import re

with open('2023/Inputs/Day25.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

nodes = {}
for i, line in enumerate(lines):
    names = re.findall('[a-z]+', line)
    nodes[names[0]] = nodes.get(names[0], []) + names[1:]
    for name in names[1:]:
        nodes[name] = nodes.get(name, []) + [names[0]]
start = max([(len(nodes[name]), name) for name in nodes.keys()])[1]
group = {start}
wires = nodes[start]
while len(wires) > 3:
    nears = []
    for wire in wires:
        # this could fail if one of the nodes accross the 3-wire gap has very few other connections
        overlap = set(nodes[wire]).intersection(group)
        nears.append((len(nodes[wire])-len(overlap), wire))
    nextNode = min(nears)[1]
    group.add(nextNode)
    while nextNode in wires:
        wires.remove(nextNode)
    wires.extend(set(nodes[nextNode]).difference(group))     
prod1 = len(group) * (len(nodes)-len(group))
print(wires) # I could track where these came from as well
print(f'1. Answer is: {prod1}') # 591890