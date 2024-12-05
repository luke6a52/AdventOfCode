import re

with open('2024/Inputs/Day5.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

rules = []
updates = []
order = {}
empty = lines.index('')
for line in lines[:empty]:
    rules.append([int(num) for num in re.findall('\d+', line)])
for line in lines[empty+1:]:
    updates.append([int(num) for num in re.findall('\d+', line)])
for rule in rules:
    if rule[0] in order:
        order[rule[0]].append(rule[1])
    else:
        order[rule[0]] = [rule[1]]
    if rule[1] not in order:
        order[rule[1]] = []

def sortUpdate(update):
    return sorted(update, key=lambda page: len(set(update).intersection(order[page])), reverse=True)

sum1 = 0
sum2 = 0
for update in updates:
    for i, page in enumerate(update):
        if not set(update[i+1:]).issubset(order[page]):
            break
    else:
        sum1 += update[(len(update)-1)//2]
        continue

    update = sortUpdate(update)
    sum2 += update[(len(update)-1)//2]
print(f'1. Answer is: {sum1}') # 4569
print(f'2. Answer is: {sum2}') # 6456