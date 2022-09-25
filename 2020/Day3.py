from math import prod

with open('Day3.txt', 'r') as input_file:
    lines = input_file.readlines()

trees = [0, 0, 0, 0, 0]
position = [-1, -3, -5, -7, -1]
even = True
for line in lines:
    position[0] = (position[0] + 1) % 31
    if line[position[0]] == '#': trees[0] += 1
    
    position[1] = (position[1] + 3) % 31
    if line[position[1]] == '#': trees[1] += 1
    
    position[2] = (position[2] + 5) % 31
    if line[position[2]] == '#': trees[2] += 1
    
    position[3] = (position[3] + 7) % 31
    if line[position[3]] == '#': trees[3] += 1
    
    if even:
        position[4] = (position[4] + 1) % 31
        if line[position[4]] == '#': trees[4] += 1
        even = False
    else:
        even = True
print(f'   Trees are {trees}')
print(f'1. Answer is {trees[1]}')
print(f'2. Answer is {prod(trees)}')