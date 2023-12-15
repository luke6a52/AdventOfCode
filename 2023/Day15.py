import re

with open('2023/Inputs/Day15.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def elfhash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256
    return value

sum1 = 0
sum2 = 0
boxes = {}
for i in range(256):
    boxes[i] = ([],[])
for step in lines[0].split(','):
    sum1 += elfhash(step)
    label, cmd, val = re.match('([a-zA-Z]+)(=|-)(\d*)', step).groups()
    key = elfhash(label)
    if cmd == '-':
        if label in boxes[key][0]:
            j = boxes[key][0].index(label)
            boxes[key][0].pop(j)
            boxes[key][1].pop(j)
    else:
        if label in boxes[key][0]:
            j = boxes[key][0].index(label)
            boxes[key][1][j] = int(val)
        else:
            boxes[key][0].append(label)
            boxes[key][1].append(int(val))
for i, box in boxes.items():
    for j, val in enumerate(box[1]):
        sum2 += (i+1) * (j+1) * val
print(f'1. Answer is: {sum1}') # 516070
print(f'2. Answer is: {sum2}') # 244981