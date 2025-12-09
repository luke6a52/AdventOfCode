import re
import math

with open('2025/Inputs/Day8.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

circuits = []
connections = dict()
for line in lines:
    nums = [int(num) for num in re.findall('\\d+', line)]
    current = (nums[0], nums[1], nums[2])
    for circuit in circuits:
        distance = math.dist(current, circuit[0])
        connections[distance] = (current, circuit[0])
    circuits.append([current])

sum1 = 0
sum2 = 0
for k, distance in enumerate(sorted(connections.keys())):
    current = []
    for i, circuit in enumerate(circuits):
        if connections[distance][0] in circuit and connections[distance][1] not in circuit:
            current = circuits.pop(i)
            break
    for circuit in circuits:
        if connections[distance][1] in circuit:
            circuit.extend(current)
            break
    if k == 999:
        sizes = [len(circuit) for circuit in circuits]
        sizes.sort(reverse=True)
        sum1 = sizes[0] * sizes[1] * sizes[2]
    if len(circuits) == 1:
        print(connections[distance])
        sum2 = connections[distance][0][0] * connections[distance][1][0]
        break
print(f'1. Answer is: {sum1}') # 102816
print(f'2. Answer is: {sum2}') # 100011612
# time: 01:17:04