import math

with open('2022/Inputs/Day11.txt', 'r') as input_file:
    inputs = input_file.read().split('\n\n')

def inspect(old, op):
    vars = {'old': old}
    exec(op, {}, vars)
    return vars['new']

monkeys = []
for input in inputs:
    lines = input.split('\n')
    items = [int(item) for item in lines[1].split(': ')[1].split(', ')]
    op = lines[2].split(': ')[1]
    test = (int(lines[3].split()[-1]), int(lines[4][-1]), int(lines[5][-1]))
    monkeys.append({'items': items, 'op': op, 'test': test, 'count': 0})

common = math.prod([monkey['test'][0] for monkey in monkeys])

# for i in range(20):
for i in range(10000):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            monkey['count'] += 1
            item = monkey['items'].pop(0)
            item = inspect(item, monkey['op'])
            # item = item // 3
            item = item % common
            if(item > 0 and item % monkey['test'][0] == 0):
                monkeys[monkey['test'][1]]['items'].append(item)
            else:
                monkeys[monkey['test'][2]]['items'].append(item)

counts = [monkey['count'] for monkey in monkeys]
counts.sort()
# print(f'1. Answer is: {counts[-2] * counts[-1]}') # 54752   1h 33m
print(f'2. Answer is: {counts[-2] * counts[-1]}') # 13606755504   2h ~30m 